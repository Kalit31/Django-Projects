from django.shortcuts import render, redirect
from .models import Survey, SurveyAnswer, QuestionAnswer,Choice


# Create your views here.

def index(request):
    ctx = {}
    return render(request, 'main.html', ctx)


def survey_view(request, survey_id=None):
    try:
        survey = Survey.objects.get(id=survey_id)
        questions = survey.question_set.all()
        ctx = {'survey': survey, 'questions': questions}
    except:
        return render(request, 'surveynotfound-error.html', {'sv_id': survey_id})

    return render(request, 'survey-take.html', ctx)


def load_survey(request):
    sv_to_load = request.POST['survey_view']
    return redirect('survey-detail', survey_id=sv_to_load)

def survey_fill(request):
    answer = SurveyAnswer()
    orig_survey = Survey.objects.get(id = request.POST['survey_id'])
    answer.orig_survey = orig_survey
    answer.save()
    questions = orig_survey.question_set.all()
    for question in questions:
        question_post = request.POST['question'+str(question.id)]
        QA = QuestionAnswer()
        QA.answer.answer = Choice.objects.get(id=int(question_post))
        QA.survey_answer = answer
        QA.save()
    answer.save()
    return render(request,'survey-complete.html',{})