# WhatsApp Auto Reply Agent using Droidrun

from droidrun import MobileAgent

agent = MobileAgent(
    device="android",
    app="com.whatsapp"
)

def decide_reply(message):
    message = message.lower()

    if "hi" in message or "hello" in message:
        return "Hi! How can I help you today?"
    elif "price" in message:
        return "Please share what service you are interested in."
    elif "location" in message or "address" in message:
        return "We are located in Patna."
    else:
        return "Thanks for your message. I will get back to you soon."

agent.launch_app()
agent.tap(index=0)   # open latest chat

last_message = agent.read_text(position="last")
reply = decide_reply(last_message)

agent.type_text(reply)
agent.tap(description="Send")

print("Reply sent successfully")
