# Create your views here.
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView

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


class StudentCreateView(CreateView):
    pass


class StudentUpdateView(UpdateView):
    pass


class StudentDeleteView(DeleteView):
    pass


class StudentDetailView(DetailView):
    pass


class GroupCreateView(CreateView):
    pass


class GroupUpdateView(UpdateView):
    pass


class GroupDeleteView(DeleteView):
    pass


class GroupDetailView(DetailView):
    http_method_names = ['get', 'head']
    model = Group
    template_name = 'students/group.html'
    pk_url_kwarg = 'group_id'

    def get_context_data(self, **kwargs):
        kwargs = super(GroupDetailView, self).get_context_data(**kwargs)
        kwargs['group_students'] = self.get_group_students()
        return kwargs

    def get_group_students(self):
        group_students = Student.objects.filter(group=self.object)
        return group_students