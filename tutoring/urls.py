from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, url
from tutoring import views

urlpatterns = patterns('',
    url(r'^$', views.ListProject.as_view(), name='project_list_all'),
    url(r'^mentor/$', views.ListMentor.as_view(), name='mentor_list_all'),
    url(r'^mentor/add/$', login_required(views.AddMentor.as_view()), name='new_mentor'),
    url(r'^mentor/update/(?P<pk>[0-9]+)/$', login_required(views.UpdateMentor.as_view()), name='update_mentor'),
    url(r'^mentor/delete/(?P<pk>[0-9]+)/$', login_required(views.DeleteMentor.as_view()), name='delete_mentor'),
    url(r'^mentor/(?P<pk>[0-9]+)/$', views.DisplayMentor.as_view(), name='display_mentor'),
    url(r'^apprentice/$', views.ListApprentice.as_view(), name='apprentice_list_all'),
    url(r'^apprentice/add/$', views.AddApprentice.as_view(), name='new_apprentice'),
    url(r'^apprentice/update/(?P<pk>[0-9]+)/$', login_required(views.UpdateApprentice.as_view()),
        name='update_apprentice'),
    url(r'^apprentice/delete/(?P<pk>[0-9]+)/$', login_required(views.DeleteApprentice.as_view()),
        name='delete_apprentice'),
    url(r'^apprentice/(?P<pk>[0-9]+)/$', views.DisplayApprentice.as_view(), name='display_apprentice'),
    url(r'^project/add/$', login_required(views.AddProject.as_view()), name='new_project'),
    url(r'^project/update/(?P<pk>[0-9]+)/$', login_required(views.UpdateProject.as_view()),
        name='update_project'),
    url(r'^project/delete/(?P<pk>[0-9]+)/$', login_required(views.DeleteProject.as_view()),
        name='delete_project'),
    url(r'^project/(?P<pk>[0-9]+)/$', views.DisplayProject.as_view(), name='display_project'),
    url(r'^mentorship/$', views.ListMentorship.as_view(), name='mentorship_list_all'),
    url(r'^mentorship/add/$', login_required(views.AddMentorship.as_view()), name='new_mentorship'),
    url(r'^mentorship/(?P<pk>[0-9]+)/$', views.DisplayMentorship.as_view(), name='display_mentorship'),
)