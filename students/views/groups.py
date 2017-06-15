from django.shortcuts import render
from django.http import HttpResponse


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