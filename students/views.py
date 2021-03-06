# Create your views here.
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse
from django.views.generic import CreateView
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView

from students.forms import StudentForm, GroupForm
from students.models import Group, Student


class IndexView(TemplateView):
    template_name = 'students/index.html'
    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        kwargs = super(IndexView, self).get_context_data(**kwargs)
        kwargs['groups_information_list'] = self.get_groups_information_list()
        return kwargs

    def get_groups_information_list(self):
        groups_information_list = []
        for group in Group.objects.all():
            group_students_amount = Student.objects.filter(group=group).count()
            group_information_tuple = (group, group_students_amount)
            groups_information_list.append(group_information_tuple)
        return groups_information_list


class HomeRedirectView(RedirectView):
    url = 'index'

    def get_redirect_url(self, *args, **kwargs):
        return reverse(self.url)


class StudentCreateView(SuccessMessageMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student/create.html'
    success_url = 'student_detail'
    success_message = "Student %s successfully added."
    pk_url_kwarg = 'student_id'

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data['surname']

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['action'] = reverse('create_student')
        context['title'] = "create student"
        return context

    def get_success_url(self):
        return reverse(self.success_url, kwargs={self.pk_url_kwarg: str(self.object.id)})

    def form_invalid(self, form):
        response = super(StudentCreateView, self).form_invalid(form)
        for error in form.errors:
            error_message = form.errors[error][0]
            messages.error(self.request, "%s %s" % (error.title(), error_message))
        return response


class StudentEditView(SuccessMessageMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student/create.html'
    success_url = 'student_detail'
    success_message = "Student %s information successfully updated."
    pk_url_kwarg = 'student_id'

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data['surname']

    def get_context_data(self, **kwargs):
        context = super(StudentEditView, self).get_context_data(**kwargs)
        context['action'] = reverse('edit_student', kwargs={self.pk_url_kwarg: str(self.object.id)})
        context['title'] = "edit student #%d" % self.object.id
        return context

    def get_success_url(self):
        return reverse(self.success_url, kwargs={self.pk_url_kwarg: str(self.object.id)})

    def form_invalid(self, form):
        response = super(StudentEditView, self).form_invalid(form)
        for error in form.errors:
            error_message = form.errors[error][0]
            messages.error(self.request, "%s %s" % (error.title(), error_message))
        return response


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student/delete.html'
    success_url = 'index'
    success_message = "Student '%s' successfully deleted."
    pk_url_kwarg = 'student_id'

    def get_success_message(self, cleaned_data):
        return self.success_message % self.object.surname

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['action'] = reverse('delete_student', kwargs={self.pk_url_kwarg: str(self.object.id)})
        context['title'] = "delete student #%d" % self.object.id
        return context

    def get_success_url(self):
        success_message = self.get_success_message(None)
        if success_message:
            messages.success(self.request, success_message)
        return reverse(self.success_url)


class StudentDetailView(DetailView):
    http_method_names = ['get', 'head']
    model = Student
    template_name = 'students/student/detail.html'
    pk_url_kwarg = 'student_id'


class GroupCreateView(SuccessMessageMixin, CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'students/group/create.html'
    success_url = 'group_detail'
    success_message = "Group %s successfully added."
    pk_url_kwarg = 'group_id'

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data['title']

    def get_context_data(self, **kwargs):
        context = super(GroupCreateView, self).get_context_data(**kwargs)
        context['action'] = reverse('create_group')
        context['title'] = "create group"
        return context

    def get_success_url(self):
        return reverse(self.success_url, kwargs={self.pk_url_kwarg: str(self.object.id)})

    def form_invalid(self, form):
        response = super(GroupCreateView, self).form_invalid(form)
        for error in form.errors:
            error_message = form.errors[error][0]
            messages.error(self.request, "%s %s" % (error.title(), error_message))
        return response


class GroupEditView(SuccessMessageMixin, UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'students/group/create.html'
    success_url = 'group_detail'
    success_message = "Group %s information successfully updated."
    pk_url_kwarg = 'group_id'

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data['title']

    def get_context_data(self, **kwargs):
        context = super(GroupEditView, self).get_context_data(**kwargs)
        context['action'] = reverse('edit_group', kwargs={self.pk_url_kwarg: str(self.object.id)})
        context['title'] = "edit group #%d" % self.object.id
        return context

    def get_success_url(self):
        return reverse(self.success_url, kwargs={self.pk_url_kwarg: str(self.object.id)})

    def form_invalid(self, form):
        response = super(GroupEditView, self).form_invalid(form)
        for error in form.errors:
            error_message = form.errors[error][0]
            messages.error(self.request, "%s %s" % (error.title(), error_message))
        return response


class GroupDeleteView(SuccessMessageMixin, DeleteView):
    model = Group
    template_name = 'students/group/delete.html'
    success_url = 'index'
    success_message = "Group '%s' successfully deleted."
    pk_url_kwarg = 'group_id'

    def get_success_message(self, cleaned_data):
        return self.success_message % self.object.title

    def get_context_data(self, **kwargs):
        context = super(GroupDeleteView, self).get_context_data(**kwargs)
        context['action'] = reverse('delete_group', kwargs={self.pk_url_kwarg: str(self.object.id)})
        context['title'] = "delete group #%d" % self.object.id
        return context

    def get_success_url(self):
        success_message = self.get_success_message(None)
        if success_message:
            messages.success(self.request, success_message)
        return reverse(self.success_url)


class GroupDetailView(DetailView):
    http_method_names = ['get', 'head']
    model = Group
    template_name = 'students/group/detail.html'
    pk_url_kwarg = 'group_id'

    def get_context_data(self, **kwargs):
        kwargs = super(GroupDetailView, self).get_context_data(**kwargs)
        kwargs['group_students'] = self.get_group_students()
        return kwargs

    def get_group_students(self):
        group_students = Student.objects.filter(group=self.object)
        return group_students