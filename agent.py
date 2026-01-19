print("Droidrun WhatsApp Auto Reply Agent Started")

def decide_reply(message):
    message = message.lower()

    if "hi" in message or "hello" in message:
        return "Hi! How can I help you today?"
    elif "price" in message:
        return "Please share what service you are interested in."
    elif "location" in message:
        return "We are located in Patna."
    else:
        return "Thanks for your message. I will get back to you soon."

# Simulated incoming message (demo purpose)
incoming_message = "Hi, price?"
reply = decide_reply(incoming_message)

print("Incoming message:", incoming_message)
print("Agent decided reply:", reply)
print("Agent action: Reply sent successfully")
