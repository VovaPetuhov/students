from django.shortcuts import render
from django.http import HttpResponse


# Views for Journal

def journal_list(request):
    journal = ({'id': 1, 'first_name': 'Корост', 'last_name': 'Андрій', 'ticket': 2123, 'image': 'img/images.jpeg'},
               {'id': 2, 'first_name': 'Зінкевич', 'last_name': 'Петро', 'ticket': 2124, 'image': 'img/images.jpeg'},
               {'id': 3, 'first_name': 'Простий', 'last_name': 'Микола', 'ticket': 2125, 'image': 'img/images.jpeg'})
    return render(request, 'students/journal.html', {'journal': journal})
