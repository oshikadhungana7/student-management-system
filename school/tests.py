from audioop import reverse
from pydoc import resolve
from django.test import TestCase
from django.views import View
import test  
import schoolmanagement

import school.tests


from School.school.views import home_view

# Create your tests here.

class Testurls(TestCase):
    def test_url_home(self):
        url=reverse('')
        self.assertEquals(resolve(url).func,'admin/')