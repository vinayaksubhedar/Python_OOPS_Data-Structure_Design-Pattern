"""
Design_pattern_S3_Facade.py
Django is a great example of the Facade Pattern, 
making web development easy by hiding complexities behind intuitive APIs.
"""

# notifications/email_service.py
class EmailService:
    def send_email(self, email, message):
        print(f"Sending email to {email}: {message}")

# notifications/sms_service.py
class SMSService:
    def send_sms(self, phone, message):
        print(f"Sending SMS to {phone}: {message}")

# notifications/push_service.py
class PushService:
    def send_push_notification(self, device_id, message):
        print(f"Sending Push Notification to {device_id}: {message}")


class NotificationFacade:
    def __init__(self):
        self.email_service = EmailService()
        self.sms_service = SMSService()
        self.push_service = PushService()

    def send_notification(self, user, message):
        print("\n--- Sending Notification ---")
        self.email_service.send_email(user["email"], message)
        self.sms_service.send_sms(user["phone"], message)
        self.push_service.send_push_notification(user["device_id"], message)


if __name__ == "__main__":
    user = {"email": "test@example.com", "phone": "+1234567890", "device_id": "abc123"}
    notifier = NotificationFacade()
    notifier.send_notification(user, "Hello, you have a new update!")



