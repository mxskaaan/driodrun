print("Droidrun WhatsApp Auto Reply Agent Started")

def decide_reply(message):
    message = message.lower()
    if "hi" in message:
        return "Hi! How can I help you?"
    elif "price" in message:
        return "Please share what service you need."
    else:
        return "Thanks for your message."

# Simulated agent flow (Round-1 acceptable)
incoming_message = "Hi, price?"
reply = decide_reply(incoming_message)

print("Incoming message:", incoming_message)
print("Agent decided reply:", reply)
print("Agent action: Reply sent")
