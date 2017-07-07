from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.core.urlresolvers import reverse
from django.views.generic import FormView

from studentsdb.settings import ADMIN_EMAIL
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ContactForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('contact_admin')

        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        self.helper.add_input(Submit('send_button', 'Надіслати'))

    from_email = forms.EmailField(label='Ваша емейл адреса')
    subject = forms.CharField(label='Заголовок листа', max_length=128)
    message = forms.CharField(label='Текст повідомлення', max_length=2560, widget=forms.Textarea)


# def contact_admin(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']
#             from_email = form.cleaned_data['from_email']
#             try:
#                 send_mail(subject, message, from_email, [ADMIN_EMAIL])
#             except Exception:
#                 messages.warning(request, 'Під час відправки листа виникла непередбачувана помилка.'
#                                           ' Спробуйте скористатись даною формою пізніше.')
#             else:
#                 messages.success(request, 'Повідомлення успішно надіслане!')
#             return HttpResponseRedirect(reverse('contact_admin'), message)
#     else:
#         form = ContactForm()
#     return render(request, 'contact_admin/form.html', {'form': form})


class ContactView(FormView):
    template_name = 'contact_admin/form.html'
    form_class = ContactForm
    success_url = '/contact_admin/'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['tittle'] = 'Редагувати Студента'
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        from_email = form.cleaned_data['from_email']
        try:
            send_mail(subject, message, from_email, [ADMIN_EMAIL])
        except Exception:
            messages.warning(self.request, 'Під час відправки листа виникла непередбачувана помилка.'
                                           ' Спробуйте скористатись даною формою пізніше.')
        else:
            messages.success(self.request, 'Повідомлення успішно надіслане!')

        return super(ContactView, self).form_valid(form)
