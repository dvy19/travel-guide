from firebase_admin import messaging

# Import to ensure Firebase is initialized
from .firebase import *


def send_notification(token, title, body):
    """
    Send notification to a single device token.
    """

    try:
        message = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=body,
            ),
            token=token,
        )

        response = messaging.send(message)

        print(f"Notification sent successfully: {response}")

        return {
            "success": True,
            "response": response
        }

    except Exception as e:
        print(f"Notification failed: {str(e)}")

        return {
            "success": False,
            "error": str(e)
        }