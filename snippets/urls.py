from django.urls import path, include

from . import views



urlpatterns = [
    path('', views.SnippetList.as_view(), name='index'),
    
    path('snippets/language/', views.SnippetLangList.as_view(), name='language'),
    path('snippets/user/<str:user>/', views.UserSnippetList.as_view(), name='user_snippets'),
    #path('snippets/snippet/', views.snippet, name='snippet'),
    #path('snippets/add/', views.snippet_add, name='snippet_add'),
    #path('snippets/edit/', views.snippet_edit, name='snippet_edit'),
    #path('snippets/delete/', views.snippet_delete, name='snippet_delete'),
    path('snippets/add/', views.SnippetCreate.as_view(), name='snippet_add'), 
    path('snippets/snippet/<pk>/', views.SnippetDetail.as_view(), name='snippet'),
    path('snippets/edit/<pk>/', views.SnippetUpdate.as_view(), name='snippet_edit'),
    path('snippets/delete/<pk>/', views.SnippetDelete.as_view(), name='snippet_delete'),
    
]