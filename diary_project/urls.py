"""
URL configuration for diary_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from diary_app import views
from diary_app.views import save_diary
from diary_app.views import edit_diary_entry

urlpatterns = [
    path('', views.diary_entries, name='diary_entries'),
    path('diary_entry/<int:entry_id>/edit/', views.edit_diary_entry, name='edit_diary_entry'),
    path('create_entry/', views.create_entry, name='create_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('save-diary/<int:entry_id>/', views.save_diary, name='save_diary'),
    path('diary_entry/<int:entry_id>/', views.diary_entry_detail, name='diary_entry_detail'),
    # path('diary_entry/<int:entry_id>/edit/', edit_diary_entry, name='edit_diary_entry'),

]



