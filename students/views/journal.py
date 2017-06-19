from django.shortcuts import render
from django.http import HttpResponse


# Views for Journal

def journal_list(request):
    journals = ({'id': 1, 'student_name': 'Корост Андрій'},
                {'id': 2, 'student_name': 'Зінкевич Петро'},
                {'id': 3, 'student_name': 'Простий Микола'})
    return render(request, 'students/journal.html', {'journals': journals})
