from django.test import TestCase
from .models import Account
from django.contrib.auth.hashers import make_password, check_password

from django.test import TestCase
from django.db import IntegrityError, transaction
from django.contrib.auth.hashers import make_password, check_password
from .models import Account

class TestAccount(TestCase):
    @classmethod
    def setUpClass(cls):
      super().setUpClass()
      # Create an initial user
      cls.initial_user = Account(
          full_name='Test User',
          email='testuser@example.com',
          password=make_password('testpassword'),
          phone_number='1234567890',
          address='Test Address',
          gender='Male'
      )
      cls.initial_user.save()

    def test_login(self):
      test_user_object = Account.account_repository.filter(email='testuser@example.com', is_deleted=False).first()
      encrypted_password = make_password('testpassword')
      self.assertEqual(test_user_object.password, encrypted_password, "Password check failed")

    def test_update_profile(self):
      test_user_object = Account.account_repository.filter(email='testuser@example.com').first()
      
      test_user_object.full_name = 'Updated Test User'
      test_user_object.phone_number = '12345672890'
      test_user_object.address = 'Updated Test Address'
      test_user_object.gender = 'Male'
      test_user_object.save()
      self.assertEqual(test_user_object.full_name, 'Updated Test User')
      self.assertEqual(test_user_object.phone_number, '12345672890')
      self.assertEqual(test_user_object.address, 'Updated Test Address')
      self.assertEqual(test_user_object.gender, 'Male')

    def test_invalid_password(self):
      test_user_object = Account.account_repository.filter(email='testuser@example.com', is_deleted=False).first()
      self.assertTrue(check_password('testpassword', test_user_object.password), "Password ccccheck failed")

    def test_delete_user(self):
      new_test_user = Account(
      full_name='New Test User',
      email='testuser1234@example.com',
      password=make_password('testpassword'),
      phone_number='12345672890',
      address='Test Address',
      gender='Female')
      new_test_user.save()
      test_user_object = Account.account_repository.filter(email=new_test_user.email).first()
      test_user_object.is_deleted = True
      test_user_object.save()

      retest_user_object = Account.account_repository.filter(email=new_test_user.email).first()
      self.assertEqual(retest_user_object.is_deleted, True)


