from django.conf.urls import url
from django.views.generic import RedirectView

import views

urlpatterns = [
    # AJAX: Request projects to be added to locale
    url(r'^request/(?P<request_type>[A-Za-z0-9\-\@\.]+)/(?P<code>[A-Za-z0-9\-\@\.]+)/$',
        views.request_item,
        name='pontoon.teams.request.projects'),

    # Localization teams
    url(r'^teams/$',
        views.teams,
        name='pontoon.teams'),

    # AJAX: Request team to be added to Pontoon
    url(r'^request/team/$',
        views.request_item,
        name='pontoon.teams.request.locale'),

    # Redirect to a team page
    url(r'^teams/(?P<locale>[A-Za-z0-9\-\@\.]+)/$',
        RedirectView.as_view(url="/%(locale)s/", permanent=True)),

    # Team contributors
    url(r'^(?P<locale>[A-Za-z0-9\-\@\.]+)/contributors/$',
        views.team,
        name='pontoon.teams.contributors'),

    # Team bugs
    url(r'^(?P<locale>[A-Za-z0-9\-\@\.]+)/bugs/$',
        views.team,
        name='pontoon.teams.bugs'),

    # Team info
    url(r'^(?P<locale>[A-Za-z0-9\-\@\.]+)/info/$',
        views.team,
        name='pontoon.teams.info'),

    # Team permissions
    url(r'^(?P<locale>[A-Za-z0-9\-\@\.]+)/permissions/$',
        views.team,
        name='pontoon.teams.permissions'),

    # Legacy url for permissions management
    url(r'^(?P<locale>[A-Za-z0-9\-\@\.]+)/manage/$',
        RedirectView.as_view(url='/%(locale)s/permissions/', permanent=True),
        name='pontoon.teams.manage'),

    # AJAX view: Team projects
    url(r'^(?P<locale>[A-Za-z0-9\-\@\.]+)/ajax/$',
        views.ajax_projects,
        name='pontoon.teams.ajax.projects'),

    # AJAX view: Team contributors
    url(r'^(?P<code>[A-Za-z0-9\-\@\.]+)/ajax/contributors/$',
        views.LocaleContributorsView.as_view(),
        name='pontoon.teams.ajax.contributors'),

    # AJAX view: Team info
    url(r'^(?P<locale>[A-Za-z0-9\-\@\.]+)/ajax/info/$',
        views.ajax_info,
        name='pontoon.teams.ajax.info'),

    # AJAX view: Update team info
    url(r'^(?P<locale>[A-Za-z0-9\-\@\.]+)/ajax/update-info/$',
        views.ajax_update_info,
        name='pontoon.teams.ajax.update-info'),

    # AJAX view: Team permissions
    url(r'^(?P<locale>[A-Za-z0-9\-\@\.]+)/ajax/permissions/$',
        views.ajax_permissions,
        name='pontoon.teams.ajax.permissions'),
]
