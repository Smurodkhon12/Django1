from django.urls import path

from . import views

# urlpatterns = [
    # path('', views.index, name='index'),
    # path('second/', views.second),
    # path('',  views.index, name='index'),
    # path('index/', views.index),
    # # path('HOME/', views.index, 'HOME'),
    # path('birinchi/', views.birinchi),
    # path('ikkinchi/', views.ikkinchi),
    # path('uchinchi/', views.uchinchi),
    # path('tortinchi/', views.tortinchi),
    # path('beshinchi/', views.beshinchi),
    # path('oltinchi/', views.oltinchi),
    # path('yettinchi/', views.yettinchi),
    # path('sakkizinchi/', views.sakkizinchi),
    # path('toqqizinchi/', views.toqqizinchi),
    # path('oningchi/', views.oningchi),
    # ]


urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('', views.index, name='index'),
]