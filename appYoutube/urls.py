
from django.contrib import admin
from django.urls import path
from task import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sigup/', views.sigup, name='sigup'),
    path('', views.sigin, name='sigin'),
    path('sair/', views.sair, name='sair'),
    path('tasks/', views.tasks, name='tasks'),
    path('criando/tarefa/', views.criando_tarefa, name='criando_tarefa'),
    path('criando/<int:task_id>/', views.task_detalhe, name='task_detalhe'), 
    path('criando/<int:task_id>/complete', views.complete_tarefa, name='complete_tarefa'), 
    path('criando/<int:task_id>/delete', views.deletar_tarefa, name='deletar_tarefa'), 
    path('exibir_tarefas_completadas', views.exibir_tarefas_completadas, name='exibir_tarefas_completadas'), 
]
