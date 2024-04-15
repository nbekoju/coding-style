"""
Create a function that validates email addresses based on following set of rules:

- Proper email format such as presence of “@”, no space in the address
- Presence of valid email providers such as yahoo, gmail and outlook. 
- Make sure there are no disposable email providers such as yopmail.
- Write unit tests to validate different email addresses against the rules, 
including valid and invalid addresses (Use unittest module).
"""

import re
import unittest


def validate_email(email):
    """
    validate the email through regex and check if the email provider is valid or not

    Parameters:
        email: str

    """
    email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
    valid_providers = ["gmail", "yahoo", "outlook"]
    invalid_providers = ["yopmail"]

    if re.match(email_regex, email):
        if any(provider in email for provider in valid_providers) and not any(
            provider in email for provider in invalid_providers
        ):
            return True
    return False


class TestValidateEmail(unittest.TestCase):
    """
    contains all validation functions for valid and invalid emails
    """

    def test_valid_emails(self):
        """
        test the valid emails
        """
        self.assertTrue(validate_email("nirajan@gmail.com"))
        self.assertTrue(validate_email("nirajan@yahoo.com"))
        self.assertTrue(validate_email("nir%ajan@outlook.com"))

    def test_invalid_emails(self):
        """
        test the invalid emails
        """
        self.assertFalse(validate_email("nirajan@yopmail.com"))
        self.assertFalse(validate_email("nirajan@ yahoo.com"))


if __name__ == "__main__":
    unittest.main()
