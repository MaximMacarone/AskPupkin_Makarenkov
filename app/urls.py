from app import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('ask', views.ask, name='ask'),
    path('question/<int:question_id>', views.question, name='question'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('tag/<str:tag_name>', views.tagged, name='tagged'),
    path('settings', views.settings, name='settings'),
    path('hot', views.hot, name='hot'),
    path('logout', views.logout, name='logout'),
    path('<int:question_id>/like_question', views.like_question, name='like_question'),
    path('like_answer/<int:answer_id>', views.like_answer, name='like_answer'),
    path('answers/<int:answer_id>/mark_as_correct/', views.mark_as_correct, name='mark_as_correct'),
]
