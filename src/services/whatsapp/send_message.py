import pywhatkit as kit

def send_whatsapp_message():
    # Send a WhatsApp message to a specific number at 13:30 (1:30 PM)
    kit.sendwhatmsg_instantly("+1234567890", "Hello, this is an automated message.")
