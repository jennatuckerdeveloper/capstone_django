$('#gameplay').bind("enterKey", function (e) {
    e.preventDefault();

    $.ajax({
        type: 'POST',
        url: '/game/gameplay_entry/',
        data: {
            choice: $('#gameplay').val()
        },
        success: function (data) {
            console.log(data);
            if (data.choice === "1" || data.choice === "2" || data.choice === "3") {
                window.location.href = "/game/names/";
            } else {
                $('#try_again').html("Please choose from menu.")
            }
        }
    })
});
$('#gameplay').keyup(function (e) {
    if (e.keyCode == 13) {
        $(this).trigger("enterKey");
    }
});

$("#names").click(function () {
    var choice2 = $('#name2').val();
    var choice3 = $('#name3').val();
    var choice4 = $('#name4').val();
    var choice5 = $('#name5').val();

    if (choice2 !== "" && choice3 !== "" && choice4 !== "" && choice5 !== "") {
            $.ajax({
                type: 'POST',
                url: '/game/names_entry/',
                data: {
                    choice2: choice2,
                    choice3: choice3,
                    choice4: choice4,
                    choice5: choice5
                },
                success: function (data) {
                    console.log(data);
                    $('#retry').html("");
                    window.location.href = "/game/packing/";
                }
                })
    } else {
        $('#retry').html("Please enter names.")
    }
});

$('#pack').bind("enterKey", function (e) {
    e.preventDefault();

    $.ajax({
        type: 'POST',
        url: '/game/packing_entry/',
        data: {
            choice: $('#pack').val()
        },
        success: function (data) {
            console.log(data);
            $('#to_pack').html("");
            $.each(data.packed, function(index, ob) {
                $('#to_pack').append("<li>" + ob + "</li>")
            })

        }
    })
});

$('#pack').keyup(function (e) {
    if (e.keyCode == 13) {
        $(this).trigger("enterKey");
    }
});

$("#done").click(function () {
    window.location.href = "/game/depart/";
});

$('#unpack').bind("enterKey", function (e) {
    e.preventDefault();

    $.ajax({
        type: 'POST',
        url: '/game/depart_entry/',
        data: {
            unpack: $('#unpack').val()
        },
        success: function (data) {
            console.log(data);
            $('#pack_final').html("");
            $.each(data.packed, function(index, ob) {
                $('#pack_final').append("<li>" + ob + "</li>")
            })
        }
    })
});
$('#unpack').keyup(function (e) {
    if (e.keyCode == 13) {
        $(this).trigger("enterKey");
    }
});

$("#gotopack").click(function () {
    window.location.href = "/game/packing/";
});

$("#depart").click(function (e) {
    e.preventDefault();

    $.ajax({
        type: 'POST',
        url: '/game/depart_check/',
        data: {
        },
        success: function (data) {
            if (data.packed <= data.limit) {
                window.location.href = "/game/play/";
            } else {
                $('#overfilled').html("You cannot carry this many items.")
            }
            }
    })
});

$('#play').bind("enterKey", function (e) {
    e.preventDefault();

    var move = $('#play').val();

    if (move === "1" || move === "2" || move === "3" || move === "5") {

        $.ajax({
            type: 'POST',
            url: '/game/play_entry/',
            data: {
                move: move
            },
            success: function (data) {
                console.log(data);
                $('#inventory').hide();
                $('#game_info').show();
                $('#day_counter').html(data.day_counter);
                $('#mile_counter').html(data.mile_counter);
                $('#food_warning').html(data.food_warning);
                $('#death').html(data.death);
                $('#happening').html(data.happening);
                $('#find').html(data.find);
                $('#landmark').html(data.landmark);
                $('#play_message').html(data.play_message);
                if (data.status === "win") {
                    $('#play').prop('disabled', true);
                    setTimeout(function () {
                        window.location.href = "/game/win/";
                    }, 8000)
                }
                if (data.status === "dead") {
                    $('#play').prop('disabled', true);
                    setTimeout(function () {
                        window.location.href = "/game/gameplay/";
                    }, 8000)
                }
            }
        })
    }

    if (move === "4") {

        $.ajax({
            type: 'POST',
            url: '/game/play_entry/',
            data: {
                move: move
            },
            success: function (data) {
                console.log(data);
                $('#game_info').hide();
                $('#inventory').show();
                $('#items').html("");
                $('#characters').html("");
                $('#char').html("Here is an overview of your team:");
                $.each(data.characters, function (index, ob) {
                    $('#characters').append("<li>" + ob + "</li>")
                });
                $('#tems').html("Here is what is in your packs:");
                $.each(data.packs, function (index, ob) {
                    $('#items').append("<li>" + ob + "</li>")
                })
            }

        })
    }
});


$('#play').keyup(function (e) {
    if (e.keyCode == 13) {
        $(this).trigger("enterKey");
    }
});

