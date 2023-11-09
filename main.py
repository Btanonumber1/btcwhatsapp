from twilio.rest import Client

# Twilio credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
whatsapp_from = 'whatsapp:+14155238886'  # Twilio's WhatsApp number
whatsapp_to = 'whatsapp:+1234567890'  # Your WhatsApp number

# Create a Twilio client
client = Client(account_sid, auth_token)

# Send a WhatsApp message
def send_whatsapp_message(message):
    message = client.messages.create(
                              from_=whatsapp_from,
                              body=message,
                              to=whatsapp_to
                          )

    print(f"Message sent successfully. SID: {message.sid}")

# Example usage
if __name__ == "__main__":
    notification_message = "Hello! This is a notification from your Python script."
    send_whatsapp_message(notification_message)
