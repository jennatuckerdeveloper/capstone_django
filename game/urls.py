from django.conf.urls import url

from game import views

app_label = "game"
urlpatterns = [
    url(r'^gameplay/$', views.gameplay, name="gameplay"),
    url(r'^names/$', views.names, name="names"),
    url(r'^packing/$', views.packing, name="packing"),
    url(r'^depart/$', views.depart, name="depart"),
    url(r'^play/$', views.play, name="play"),
    url(r'^win/$', views.win, name="win"),
    url(r'^gameplay_entry/$', views.gameplay_entry, name="gameplay_entry"),
    url(r'^names_entry/$', views.names_entry, name="names_entry"),
    url(r'^depart_entry/$', views.depart_entry, name="depart_entry"),
    url(r'^depart_check/$', views.depart_check, name="depart_check"),
    url(r'^packing_entry/$', views.packing_entry, name="packing_entry"),
    url(r'^play_entry/$', views.play_entry, name="play_entry"),

]

#What's the name for again?