from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('book/<int:book_id>/pdf/', views.generate_pdf, name='generate_pdf'),
    path('book/<int:book_id>/email/', views.send_email, name='send_email'),
]
