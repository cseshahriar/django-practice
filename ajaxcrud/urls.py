from django.urls import path

from ajaxcrud import views

urlpatterns = [
    path('books/', views.book_list, name='ajaxcrud_books'),
    path('books/create/', views.book_create, name='ajaxcrud_book_create'),
    path(
        'books/<int:pk>/update/', views.book_update,
        name='ajaxcrud_book_update'
    ),
    path(
        'books/<int:pk>/delete/', views.book_delete,
        name='ajaxcrud_book_delete'
    ),
]