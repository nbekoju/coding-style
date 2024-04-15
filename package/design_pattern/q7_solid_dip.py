# [Dependency Inversion Principle (DIP)] Download the python file from this link. Suppose we have a NotificationService class that is responsible for sending notifications. The NotificationService class directly depends on the EmailSender class to send emails.

# In this implementation, the NotificationService class directly depends on the EmailSender class, which violates the Dependency Inversion Principle. The high-level NotificationService should not depend on the low-level EmailSender, as it tightly couples the classes together.

# Redesign this program to follow the  Dependency Inversion Principle (DIP) principle which represents that “Abstractions should not depend upon details. Details should depend upon abstractions.”
from abc import ABC, abstractmethod


class MessageSender(ABC):
    @abstractmethod
    def send_message(self, recipient, message):
        pass


class EmailSender(MessageSender):
    def send_message(self, recipient, message):
        print(f"Sending email to {recipient}: {message}")


class SMSSender(MessageSender):
    def send_message(self, recipient, message):
        print(f"Sending SMS to {recipient}: {message}")


class NotificationService:
    def __init__(self, sender: MessageSender) -> None:
        self.sender = sender

    def send_notification(self, recipient, message):
        self.sender.send_message(recipient, message)


email_sender = EmailSender()
notification_service = NotificationService(email_sender)
notification_service.send_notification(
    "abcd@fusemachines.com", "this is a notification"
)

sms_sender = SMSSender()
notification_service = NotificationService(sms_sender)
notification_service.send_notification("9843123122", "this is a notification")

"""
# This code violates the Dependency Inversion Principle
class EmailSender:
    def send_email(self, recipient, subject, message):
        # Code to send an email
        print(f"Sending email to {recipient}: {subject} - {message}")


class NotificationService:
    def __init__(self):
        self.email_sender = EmailSender()

    def send_notification(self, recipient, message):
        self.email_sender.send_email(recipient, "Notification", message)


# Using the NotificationService to send a notification
notification_service = NotificationService()
notification_service.send_notification(
    "user@example.com", "Hello, this is a notification!"
)

"""
