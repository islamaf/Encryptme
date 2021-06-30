from django.urls import path

from . import views

app_name = 'encryption'
urlpatterns = [
    path('', views.index, name='index'),
    path('caesar/', views.caesar, name='caesar'),
    path('vernam/', views.vernam, name='vernam'),
    path('vigenere/', views.vigenere, name='vigenere'),
    path('encrypt_vernam', views.encrypt_vernam, name='encrypt_vernam'),
    path('decrypt_vernam', views.decrypt_vernam, name='decrypt_vernam'),
    path('encrypt_vigenere', views.encrypt_vigenere, name='encrypt_vigenere'),
    path('decrypt_vigenere', views.decrypt_vigenere, name='decrypt_vigenere'),
    path('encrypt_decrypt_caesar', views.encrypt_decrypt_caesar, name='encrypt_decrypt_caesar')
]