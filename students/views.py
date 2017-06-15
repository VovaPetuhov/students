from django.shortcuts import render
from django.http import HttpResponse


# Views for Students

def students_list(request):
    students = ({'id': 1, 'first_name': 'Корост', 'last_name': 'Андрій', 'ticket': 2123, 'image': 'img/images.jpeg'},
                {'id': 2, 'first_name': 'Зінкевич', 'last_name': 'Петро', 'ticket': 2124, 'image': 'img/images.jpeg'},
                {'id': 3, 'first_name': 'Простий', 'last_name': 'Микола', 'ticket': 2125, 'image': 'img/images.jpeg'})
    return render(request, 'students/students_list.html', {'students': students})


def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)


# Views for Groups

def groups_list(request):
    groups = ({'id': 1, 'group_name': 'МтМ - 21', 'group_starosta': 'Корост Андрій'},
              {'id': 2, 'group_name': 'МтМ - 22', 'group_starosta': 'Зінкевич Петро'},
              {'id': 3, 'group_name': 'МтМ - 23', 'group_starosta': 'Простий Микола'})
    return render(request, 'students/groups.html', {'groups': groups})


def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
