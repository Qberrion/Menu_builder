from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def main_menu(request, menu_path):
    print(menu_path)
    return render(request, 'index.html', {"menu_path": menu_path})


def main_index(request):
    return HttpResponse('<a href="menu/0">>>Переход к основной части<<</a>')
