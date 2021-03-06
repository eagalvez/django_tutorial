#from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import render
#from django.template import loader
from django.http import HttpResponse
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    # That code loads the template called polls/index.html and passes it a context. The context is a dictionary mapping template variable names to Python objects.
    context = {
        'latest_question_list': latest_question_list,
    }
    
    #return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html',context)
def detail(request,question_id):
#    return HttpResponse("You are looking at question %s" % question_id)
    """try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    """
    # Some controlled coupling is introduced in the django.shortcuts module.
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request,question_id):
    #response = "You are looking at the results of question %s."
    #return HttpResponse(response % question_id)
    try :
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question doe not exist")
    return render(request, 'polls/result.html', {'question',question})
def vote(request, question_id):
    return HttpResponse("You are voting on question %s" % question_id)