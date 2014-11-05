from django.contrib import admin
# Register your models here.
from students.models import Student, Group, SignalEvent


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


class SignalEventAdmin(admin.ModelAdmin):
    fields = ['sender', 'event', 'additional_info', 'time_stamp']
    list_display = ['sender', 'event', 'time_stamp']
    readonly_fields = ['time_stamp']


admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(SignalEvent, SignalEventAdmin)