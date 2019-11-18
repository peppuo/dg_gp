import datetime
import pytz

from django.test import RequestFactory, TestCase
from django.utils import timezone

from dummyApp.models import Category, Department, Log, Status, Task, User
from dummyApp.views import edit_log, render_base


class RenderBaseViewTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_page_renders(self):
        request = self.factory.get('')
        response = render_base(request)
        self.assertEqual(response.status_code, 200)


class EditLogViewTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.started_dt = timezone.now().replace(microsecond=0)
        Category.objects.create(name='dummy_category')
        Department.objects.create(name='dummy_department')
        Status.objects.create(name='dummy_status')
        Task.objects.create(
            name='dummy_task',
            category=Category.objects.get(name='dummy_category'),
            )
        User.objects.create(
            first_name='dummy_user',
            email_address='dummy_email@address.com',
            department=Department.objects.get(name='dummy_department'),
            )
        Log.objects.create(
            task=Task.objects.get(name='dummy_task'),
            user=User.objects.get(email_address='dummy_email@address.com'),
            status=Status.objects.get(name='dummy_status'),
            started=self.started_dt,
            )
        self.log_id = Log.objects.get(started=self.started_dt).id
        print('\n\nLOG_ID', self.log_id)

    def test_loads_right_object(self):
        request = self.factory.get(f'/edit-log/{self.log_id}')
        response = edit_log(request, self.log_id)
        self.assertEqual(response.status_code, 200)
        self.assertIn('dummy_task', str(response.content))
        self.assertIn(self.started_dt.strftime('%Y-%m-%d %H:%M:%S'),
                      str(response.content))
