import unittest

from hidetext.filters import Email


class EmailTest(unittest.TestCase):
    def test_just_emails(self) -> None:
        email = Email()
        self.assertTrue(email.is_valid("hola@hi.com"))
        self.assertFalse(email.is_valid("hola@hi.com "))
        self.assertTrue(email.is_valid("email.home5@hi.com"))
        self.assertFalse(email.is_valid("hello"))
