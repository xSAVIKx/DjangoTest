# Create your tests here.
import datetime

from django.contrib.auth.models import User

from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.select import Select

from students.models import Student, Group


class IntegrationTests(LiveServerTestCase):
    selenium = None

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(IntegrationTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(IntegrationTests, cls).tearDownClass()

    def setUp(self):
        User.objects.create_user(username='test', email='test@test.test', password='test')

    def test_add_student(self):
        student_first_name = "Valera"
        student_middle_name = "Sergiyovich"
        student_surname = "Petrenko"
        student_birthday_date = "10/01/2014"
        group_title = 'Test group'

        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        self.selenium.implicitly_wait(2)
        # LOGIN
        self.selenium.find_element_by_link_text("Login").click()
        self.selenium.implicitly_wait(2)
        self.selenium.find_element_by_id("id_username").send_keys('test@test.test')
        self.selenium.find_element_by_id('id_password').send_keys('test')
        self.selenium.find_element_by_css_selector("button[type='submit']").click()
        self.selenium.implicitly_wait(2)
        # CREATE_GROUP
        self.selenium.find_element_by_link_text("Create group").click()
        self.selenium.implicitly_wait(2)
        self.selenium.find_element_by_id("id_title").send_keys(group_title)
        self.selenium.find_element_by_css_selector("button[type='submit']").click()
        self.selenium.implicitly_wait(2)
        # CREATE_STUDENT
        self.selenium.find_element_by_link_text("Create student").click()
        self.selenium.find_element_by_id('id_first_name').send_keys(student_first_name)
        self.selenium.find_element_by_id('id_middle_name').send_keys(student_middle_name)
        self.selenium.find_element_by_id('id_surname').send_keys(student_surname)
        self.selenium.find_element_by_id('id_birthday_date').send_keys(student_birthday_date)
        group_select = Select(self.selenium.find_element_by_id('id_group'))
        group_select.select_by_value('1')
        self.selenium.find_element_by_css_selector("button[type='submit']").click()
        self.selenium.implicitly_wait(2)
        # ASSERTS
        groups = Group.objects.all()
        self.assertEqual(len(groups), 1, "There is not one group!")
        actual_group = groups[0]
        self.assertEqual(actual_group.title, group_title)
        students = Student.objects.all()
        self.assertEqual(len(students), 1, "There is not one student!")
        actual_student = students[0]
        self.assertEqual(actual_student.first_name, student_first_name)
        self.assertEqual(actual_student.middle_name, student_middle_name)
        self.assertEqual(actual_student.surname, student_surname)
        self.assertEqual(actual_student.birthday_date, datetime.date(year=2014, month=10, day=01))
        self.assertEqual(actual_student.group, actual_group)