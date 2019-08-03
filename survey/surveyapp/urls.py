from django.contrib import admin
from django.urls import path
from survey.surveyapp import views

urlpatterns = [
    path('', views.index,name="root"),
    path('survey_load/',views.load_survey,name="load-survey"),
    path('survey/<int:id>/',views.survey_view,name="survey-detail")
]
