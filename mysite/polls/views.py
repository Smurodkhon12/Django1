from django.shortcuts import render, HttpResponse
from .models import Question, Choice
from django.template import loader

from django.shortcuts import render, HttpResponse
#
#
# # def index(request):
# #     return HttpResponse('<a href="http://127.0.0.1:8000/second/">Salom salom!</a>')
#
#
# # def second(request):
# #     return HttpResponse('Xayr Guruh!<button>Button</button>')
#
#
# def index(request):
#
#     return HttpResponse('  <a href="http://127.0.0.1:8000/birinchi/"> 1 saxifa</a>     <a href="http://127.0.0.1:8000/ikkinchi/"> 2 saxifa</a>'
#                         '<a href="http://127.0.0.1:8000/uchinchi/"> 3 saxifa</a>     <a href="http://127.0.0.1:8000/tortinchi/"> 4 saxifa</a>    <a href="http://127.0.0.1:8000/beshinchi/"> 5 saxifa</a> '
#                         '<a href="http://127.0.0.1:8000/oltinchi/"> 6 saxifa</a>     <a href="http://127.0.0.1:8000/yettinchi/"> 7 saxifa</a>    <a href="http://127.0.0.1:8000/sakkizinchi/"> 8 saxifa</a>  '
#                         '<a href="http://127.0.0.1:8000/toqqizinchi/"> 9 saxifa</a>       <a href="http://127.0.0.1:8000/oningchi/"> 10 saxifa</a>' )
#
#
#
#
#
#
#
# def birinchi(request):
#     return HttpResponse('bu 1 chi saxifa'
#                         '<a href="http://127.0.0.1:8000/index/">HOME</a>'
#                          '<a href="http://127.0.0.1:8000/ikkinchi/">NEXT</a>' )
#
#
# def ikkinchi(request):
#     return HttpResponse('bu 2 chi saxifa'
#                         '<a href="http://127.0.0.1:8000/index/">HOME</a>'
#                         '<a href="http://127.0.0.1:8000/uchinchi/">NEXT</a>'
#                         )
#
# def uchinchi(request):
#     return HttpResponse('bu 3 chi saxifa'
#                         '<a href="http://127.0.0.1:8000/index/">HOME</a>'
#                         '<a href="http://127.0.0.1:8000/tortinchi/">NEXT</a>'
#                         )
#
# def tortinchi(request):
#     return HttpResponse('bu 4 chi saxifa'
#                         '<a href="http://127.0.0.1:8000/index/">HOME</a>'
#                         '<a href="http://127.0.0.1:8000/beshinchi/">NEXT</a>'
#                         )
#
# def beshinchi(request):
#     return HttpResponse('bu 5 chi saxifa'
#                         '<a href="http://127.0.0.1:8000/index/">HOME</a>'
#                         '<a href="http://127.0.0.1:8000/oltinchi/">NEXT</a>'
#                         )
#
# def oltinchi(request):
#     return HttpResponse('bu 6 chi saxifa'
#                         '<a href="http://127.0.0.1:8000/index/">HOME</a>'
#                         '<a href="http://127.0.0.1:8000/yettinchi/">NEXT</a>'
#                         )
#
# def yettinchi(request):
#     return HttpResponse('bu 7 chi saxifa'
#                         '<a href="http://127.0.0.1:8000/index/">HOME</a>'
#                         '<a href="http://127.0.0.1:8000/sakkizinchi/">NEXT</a>'
#                         )
#
# def sakkizinchi(request):
#     return HttpResponse('bu 8 chi saxifa'
#                         '<a href="http://127.0.0.1:8000/index/">HOME</a>'
#                         '<a href="http://127.0.0.1:8000/toqqizinchi/">NEXT</a>'
#                         )
#
# def toqqizinchi(request):
#     return HttpResponse('bu 9 chi saxifa'
#                         '<a href="http://127.0.0.1:8000/index/">HOME</a>'
#                         '<a href="http://127.0.0.1:8000/oningchi/">NEXT</a>'
#                         )
#
# def oningchi(request):
#     return HttpResponse('bu 10 chi saxifa'
#                         '<a href="http://127.0.0.1:8000/index/">HOME</a>'
#                         )



def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}s.")


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)







