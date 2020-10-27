# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Question


def index(request) -> HttpResponse:
    '''Retorna uma lista das 5 questões publicadas recentemente

    :return: Lista das 5 questões mais recentes

    '''
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    context = {
        'latest_question_list': latest_question_list
    }

    return render(request, 'polls/index.html', context)


def detail(request, question_id: int) -> HttpResponse:
    '''Retorna o código da questão

    :param question_id: Número de identificação da questão
    :return: Resposta com uma mensagem

    '''
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'polls/detail.html', context)


def results(request, question_id: int) -> HttpResponse:
    '''Retorna os resultados encontrados pelo número da questão

    :param question_id: Número de identificação da questão
    :return: Resposta com uma mensagem

    '''
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id: int) -> HttpResponse:
    '''Retorna uma mensagem sobre o voto a ser realizado

    :param question_id: Número de identificação da questão
    :return: Resposta com uma mensagem

    '''
    return HttpResponse("You're voting on question %s." % question_id)


# Create your views here.
