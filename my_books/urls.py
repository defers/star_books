from django.urls import path
import my_books.views as views

urlpatterns = [
    path('books/', views.list_users, name='books')
]

