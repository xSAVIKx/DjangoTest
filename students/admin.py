from django.contrib import admin
# Register your models here.
from students.models import Student, Group


class StudentAdmin(admin.ModelAdmin):
    fields = ['first_name', 'surname', 'middle_name', 'birthday_date', 'student_card_id', 'group']
    list_display = ['surname', 'first_name', 'group']
    readonly_fields = ['student_card_id']


class StudentInline(admin.TabularInline):
    model = Student
    extra = 0
    can_delete = False


class GroupAdmin(admin.ModelAdmin):
    fields = ['title', 'praepostor']
    list_display = ['title', 'praepostor']
    inlines = [StudentInline]


admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)