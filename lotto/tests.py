from django.test import TestCase
from .models import GuessNumbers

# Create your tests here.
class GuessNumbersTestCase(TestCase):

    def test_generate(self):

        g = GuessNumbers(name='Test numers', text= 'selected numbers')

        pring('Pre-generate : ', g.lottos)

        g.generate()

        print(g.update_date)
        print(g.lottos)

        self.assertTrue(len(g.lottos) > 20)
