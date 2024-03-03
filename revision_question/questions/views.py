from django.http import HttpResponse
from django.template import loader
from .models import Gradessubjects,Gradelessons,Questions

def questions(request):
    template = loader.get_template('first.html')
    return HttpResponse(template.render())

def grades(request):
    grdessubjects = Gradessubjects.objects.values_list('grade', flat=True).distinct()
    template = loader.get_template('grades.html')
    context = {
        'grades' : grdessubjects
    }
    return HttpResponse(template.render(context,request))


def grade6subjects(request):
    grdessubjects = Gradessubjects.objects.filter(grade = 6).values_list('subject',flat=True).distinct()
    template = loader.get_template('grade6subjects.html')
    context = {
        'grade6subjects' : grdessubjects
    }
    return HttpResponse(template.render(context,request))

def grade11subjects(request):
    grdessubjects = Gradessubjects.objects.filter(grade = 11).values_list('subject',flat=True).distinct()
    template = loader.get_template('grade11subjects.html')
    context = {
        'grade11subjects' : grdessubjects
    }
    return HttpResponse(template.render(context,request))

def grade6maths(request):
    grdessubjects = Gradelessons.objects.filter(id = 1).values('lesson_name')
    template = loader.get_template('grade6maths.html')
    context = {
        'grade6maths' : grdessubjects
    }
    return HttpResponse(template.render(context,request))

def m6circlequestions(request):
    grdessubjects = Questions.objects.filter(lesson_id = 1).values()
    template = loader.get_template('m6circlequestions.html')
    context = {
        'm6circlequestions' : grdessubjects
    }
    return HttpResponse(template.render(context,request))
