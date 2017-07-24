from datetime import datetime
from django.contrib import messages
from django.forms import ModelForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.views.generic import UpdateView, DeleteView
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions
from students.models import Student, Group


# Views for Students


def students_list(request):
    students = Student.objects.all()

    # try to order/reverse students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('id', 'first_name', 'last_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()
    else:
        students = students.order_by('last_name')

    # paginate students
    paginator = Paginator(students, 3)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)

    return render(request, 'students/students_list.html', {'students': students})


def students_add(request):

    if request.method == 'POST':

        if request.POST.get('add_button') is not None:
            errors = {}
            data = {'middle_name': request.POST.get('middle_name'), 'notes': request.POST.get('notes')}
            first_name = request.POST.get('first_name', ' ').strip()
            if not first_name:
                errors['first_name'] = 'Ім’я є обов’язковим'
            else:
                data['first_name'] = first_name
            last_name = request.POST.get('last_name', ' ').strip()
            if not last_name:
                errors['last_name'] = 'Прізвище є обов’язковим'
            else:
                data['last_name'] = last_name
            birthday = request.POST.get('birthday', ' ').strip()
            if not birthday:
                errors['birthday'] = 'Дата народження є обов’язковою'
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    errors['birthday'] = 'Введіть коректний формат дати(напр. 1984-12-30)'
                else:
                    data['birthday'] = birthday
            ticket = request.POST.get('ticket', ' ').strip()
            if not ticket:
                errors['ticket'] = 'Номер білета є обов’язковим'
            else:
                data['ticket'] = ticket
            student_group = request.POST.get('student_group', ' ').strip()
            if not student_group:
                errors['student_group'] = 'Оберіть групу для студента'
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) != 1:
                    errors['student_group'] = 'Оберіть коректну групу'
                else:
                    data['student_group'] = groups[0]
            photo = request.FILES.get('photo')
            if photo:
                try:
                    file = request.FILES['photo'].name
                    file_dict = file.split('.')
                    file_size = request.FILES['photo'].size
                except Exception:
                    errors['photo'] = 'Проблема з фото'
                else:
                    if (file_dict[1] in ['jpg', 'jpeg']) and file_size <= 2000000:
                        data['photo'] = photo
                    else:
                        errors['photo'] = "Виберіть файл формату 'jpg' або 'jpeg' розміром не більше 2 Мбайт"
            if not errors:
                student = Student(**data)
                student.save()
                messages.success(request, 'Студента %s %s успішно додано!' % (data['first_name'], data['last_name']))
                return HttpResponseRedirect(reverse('home'))
            else:
                messages.warning(request, 'Будь-ласка, виправте наступні помилки ...')
                return render(request, 'students/students_add.html',
                              {'groups': Group.objects.all().order_by('title'), 'errors': errors})
        elif request.POST.get('cancel_button') is not None:
            messages.info(request, 'Додавання студента скасовано!')
            return HttpResponseRedirect(reverse('home'))
    else:
        return render(request, 'students/students_add.html', {'groups': Group.objects.all().order_by('title')})


class StudentUpdateForm(ModelForm):

    class Meta:
        model = Student
        fields = ['first_name',
                  'last_name',
                  'middle_name',
                  'birthday',
                  'photo',
                  'ticket',
                  'notes']

    def __init__(self, *args, **kwargs):
        super(StudentUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_action = reverse('students_edit', kwargs={'pk': kwargs['instance'].id})
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        self.helper.layout[-1] = FormActions(Submit('add_button', 'Зберегти', css_class='btn btn-primary'),
                                             Submit('cancel_button', 'Скасувати', css_class='btn btn-link'),)


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'contact_admin/form.html'
    form_class = StudentUpdateForm

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['tittle'] = 'Зв’язок із Адміністратором'
        return context

    def get_success_url(self):
        messages.success(self.request, 'Студента успішно збережено!')
        return reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.info(request, 'Редагування студента відмінено!')
            return HttpResponseRedirect(reverse('home'))
        else:
            return super(StudentUpdateView, self).post(request, *args, **kwargs)


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/confirm_delete.html'

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.info(request, 'Видалення студента скасовано!')
            return HttpResponseRedirect(reverse('home'))
        else:
            return super(StudentDeleteView, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['tittle'] = 'Видалити Студента'
        return context

    def get_success_url(self):
        messages.success(self.request, 'Студента успішно видалено!')
        return reverse('home')