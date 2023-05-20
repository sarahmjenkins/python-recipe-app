from django.test import TestCase
from .models import User

# Tests to run:
# username value and max length
# password value and max length
# bio value, max length, and default
# __str__ function
class UserModelTest(TestCase):
    def setUpTestData():
        User.objects.create(
            username='sarah',
            password='password',
            bio='I like cooking.'
        )

    def test_user_username(self):
        user = User.objects.get(id=1)
        user_username = user._meta.get_field('username').verbose_name
        self.assertEqual(user_username, 'username')

    def test_user_username_max_length(self):
        user = User.objects.get(id=1)
        user_username_max_length = user._meta.get_field('username').max_length
        self.assertEqual(user_username_max_length, 12)
    
    def test_user_password(self):
        user = User.objects.get(id=1)
        user_password = user._meta.get_field('password').verbose_name
        self.assertEqual(user_password, 'password')

    def test_user_password_max_length(self):
        user = User.objects.get(id=1)
        user_password_max_length = user._meta.get_field('password').max_length
        self.assertEqual(user_password_max_length, 12)

    def test_user_bio(self):
        user = User.objects.get(id=1)
        user_bio = user._meta.get_field('bio').verbose_name
        self.assertEqual(user_bio, 'bio')

    def test_user_bio_max_length(self):
        user = User.objects.get(id=1)
        user_bio_max_length = user._meta.get_field('bio').max_length
        self.assertEqual(user_bio_max_length, 250)
    
    def test_user_bio_default(self):
        user = User.objects.get(id=1)
        user_bio_default = user._meta.get_field('bio').default
        self.assertEqual(user_bio_default, 'no bio')

    def test_user_str(self):
      user = User.objects.get(id=1)
      self.assertEqual(str(user), f'Profile of {user.username}') 
