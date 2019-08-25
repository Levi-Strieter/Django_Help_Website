from django.urls import path
from django.conf.urls import url



from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('asked_questions/', views.asked_questions),
    path('FAQ/', views.FAQ),
    path('help_form/', views.help_form),
    path('thanks/', views.thanks),
    path('asked_questions/<int:id>/delete/', views.delete_model),
    path('videos', views.video)

]