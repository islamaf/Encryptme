from django import template
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse

from django.views.decorators.csrf import csrf_exempt

from .models import Choice, Question
from .vernam import vernam_cipher, vernam_cipher_decoder
from .caesar import caesar_cipher
from .vigenere import vigenere_cipher, vigenere_cipher_decoder

def index(request):
    return render(request, 'encryption/index.html')

def caesar(request):
    return render(request, 'encryption/caesar.html')

def vernam(request):
    return render(request, 'encryption/vernam.html')

def vigenere(request):
    return render(request, 'encryption/vigenere.html')

def get_params(request):
    text = request.POST['to_encrypt']
    key = request.POST['key']
    return text, key

def check_string(s):
    s = s.strip()
    s = s.replace(" ", "")
    s = " ".join(s.split())
    return s

def encrypt_vernam(request):
    if request.method == "POST":
        text, key = get_params(request)
        if (not key.isspace()) and (key.isalpha()):
            en_text = vernam_cipher(text, key)
        else:
            en_text = "Invalid key."
        return HttpResponse(en_text)

def decrypt_vernam(request):
    if request.method == "POST":
        text, key = get_params(request)
        if (not key.isspace()) and (key.isalpha()):
            en_text = vernam_cipher_decoder(text, key)
        else:
            en_text = "Invalid key."
        return HttpResponse(en_text)

def encrypt_vigenere(request):
    if request.method == "POST":
        text, key = get_params(request)
        if(not key.isspace()) and (key.isalpha()):
            en_text = vigenere_cipher(text, key)
        else:
            en_text = "Invalid key."
        return HttpResponse(en_text)

def decrypt_vigenere(request):
    if request.method == "POST":
        text, key = get_params(request)
        if(not key.isspace()) and (key.isalpha()):
            en_text = vigenere_cipher_decoder(text, key)
        else:
            en_text = "Invalid key."
        return HttpResponse(en_text)

def encrypt_decrypt_caesar(request):
    if request.method == "POST":
        text, key = get_params(request)
        signal = request.POST['signal']
        if signal == "encrypt":
            if (not key.isspace()) and (not key.isalpha()) and (int(key) >=1 and int(key) <= 26):
                en_text = caesar_cipher(text, int(key))
            else:
                en_text = "Invalid key."
        else:
            if (not key.isspace()) and (not key.isalpha()) and (int(key) >=1 and int(key) <= 26):
                en_text = caesar_cipher(text, -int(key))
            else:
                en_text = "Invalid key."
        return HttpResponse(en_text)    