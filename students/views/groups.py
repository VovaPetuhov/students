from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.views.generic import DeleteView

from students.models import Group


# Views for Groups


def groups_list(request):
    groups = Group.objects.all()

    # try to order/reverse groups list
    order_by = request.GET.get('order_by', '')
    if order_by in ('id', 'title'):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            groups = groups.reverse()
    else:
        groups = groups.order_by('title')

    # paginate groups
    paginator = Paginator(groups, 3)
    page = request.GET.get('page')
    try:
        groups = paginator.page(page)
    except PageNotAnInteger:
        groups = paginator.page(1)
    except EmptyPage:
        groups = paginator.page(paginator.num_pages)

    return render(request, 'students/groups.html', {'groups': groups})


def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)


class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'students/confirm_delete.html'

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.info(request, 'Видалення групи скасовано!')
            return HttpResponseRedirect(reverse('groups'))
        else:
            return super(GroupDeleteView, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GroupDeleteView, self).get_context_data(**kwargs)
        context['tittle'] = 'Видалити Групу'
        return context

    def get_success_url(self):
        messages.success(self.request, 'Групу успішно видалено!')
        return reverse('groups')
