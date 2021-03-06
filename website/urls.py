from django.urls import path
from django.conf.urls import url

from . import views
from .views import SearchResultsView

urlpatterns = [
    path('', views.index, name="index"),
    path('asked_questions/', views.asked_questions),
    path('FAQ/', views.FAQ),
    path('help_form/', views.help_form),
    path('thanks/', views.thanks),
    path('videos/', views.video),
    path('dashboard/', views.team_homepage),
    path('video_upload/', views.video_upload),
    path('FAQ_upload/', views.FAQ_upload),
    path('about_us', views.about_us),
    path('search/', SearchResultsView.as_view(), name='search_results'),

]
