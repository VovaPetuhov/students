from django.forms import ModelForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.views.generic import DeleteView, UpdateView, CreateView
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions
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


class GroupsAddForm(ModelForm):

    class Meta:
        model = Group
        fields = ['title',
                  'notes',
                  'leader']

    def __init__(self, *args, **kwargs):
        super(GroupsAddForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_action = reverse('groups_add')
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        self.helper.layout[-1] = FormActions(Submit('add_button', 'Зберегти', css_class='btn btn-primary'),
                                             Submit('cancel_button', 'Скасувати', css_class='btn btn-link'),)


class GroupsAddView(CreateView):
    model = Group
    template_name = 'contact_admin/form.html'
    form_class = GroupsAddForm

    def get_context_data(self, **kwargs):
        context = super(GroupsAddView, self).get_context_data(**kwargs)
        context['tittle'] = 'Додати Групу'
        return context

    def get_success_url(self):
        messages.success(self.request, 'Групу успішно додано!')
        return reverse('groups')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.info(request, 'Додавання групи відмінено!')
            return HttpResponseRedirect(reverse('groups'))
        else:
            return super(GroupsAddView, self).post(request, *args, **kwargs)


class GroupsUpdateForm(ModelForm):

    class Meta:
        model = Group
        fields = ['title',
                  'notes',
                  'leader']

    def __init__(self, *args, **kwargs):
        super(GroupsUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_action = reverse('groups_edit', kwargs={'pk': kwargs['instance'].id})
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        self.helper.layout[-1] = FormActions(Submit('add_button', 'Зберегти', css_class='btn btn-primary'),
                                             Submit('cancel_button', 'Скасувати', css_class='btn btn-link'),)


class GroupsUpdateView(UpdateView):
    model = Group
    template_name = 'contact_admin/form.html'
    form_class = GroupsUpdateForm

    def get_context_data(self, **kwargs):
        context = super(GroupsUpdateView, self).get_context_data(**kwargs)
        context['tittle'] = 'Редагувати Групу'
        return context

    def get_success_url(self):
        messages.success(self.request, 'Групу успішно збережено!')
        return reverse('groups')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.info(request, 'Редагування групи відмінено!')
            return HttpResponseRedirect(reverse('groups'))
        else:
            return super(GroupsUpdateView, self).post(request, *args, **kwargs)


class GroupsDeleteView(DeleteView):
    model = Group
    template_name = 'students/confirm_delete.html'

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.info(request, 'Видалення групи скасовано!')
            return HttpResponseRedirect(reverse('groups'))
        else:
            return super(GroupsDeleteView, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GroupsDeleteView, self).get_context_data(**kwargs)
        context['tittle'] = 'Видалити Групу'
        return context

    def get_success_url(self):
        messages.success(self.request, 'Групу успішно видалено!')
        return reverse('groups')
