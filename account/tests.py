from django.test import TestCase
from .models import Account
from django.contrib.auth.hashers import make_password, check_password

class TestAccount(TestCase):
  def setUp(self):
        # Create an initial user
        self.initial_user = Account(
            full_name='Test User',
            email='testuser@example.com',
            password=make_password('testpassword'),
            phone_number='1234567890',
            address='Test Address',
            gender='Male'
        )
        self.initial_user.save()

  # def test_signup_with_same_email(self):
  #   # Use the initial user created in setUp
  #   new_test_user = Account(
  #       full_name='New Test User',
  #       email='testuser@example.com',
  #       password=make_password('testpassword'),
  #       phone_number='12345672890',
  #       address='Test Address',
  #       gender='Female')
    
  #   # Expecting IntegrityError due to unique constraint violation
  #   with self.assertRaises(IntegrityError):
  #       new_test_user.save()

  def test_login(self):
    # Use the initial user created in setUp
    test_user_object = Account.account_repository.filter(email='testuser@example.com', is_deleted=False).first()

    self.assertTrue(check_password('testpassword', test_user_object.password))
    # self.assertFalse(check_password('SomeMushkiltestpassword1', test_user_object.password))
