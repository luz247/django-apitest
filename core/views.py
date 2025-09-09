from django.shortcuts import render
from django.http import HttpResponse
from .models import Deuda
# Create your views here.

def index(request):
    latest_question_list = Deuda.objects.order_by('monto')[:4]
    output = ", ".join([q.monto for q in latest_question_list])
    return HttpResponse(output)



def detail(request, id):
    
    return HttpResponse("you're loking at question %s. " % id)



def reult(request, id):
    response = "you're loking at the results of questions %$."
    return HttpResponse(response % id)


def vote(request, id):
    return HttpResponse("You're voting on question %s." % id)