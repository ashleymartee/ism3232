# my_main.py
# Author: Ashley Marte

from my_assistant import GroomingAssistant
from my_tool import GroomingSchedule

OPEN_TIMES = {
    "monday": "9:00 am and 2:30 pm",
    "wednesday": "11:00 am",
    "friday": "none",
}

schedule_tool = GroomingSchedule(OPEN_TIMES)

assistant = GroomingAssistant(
    "Bella",
    "You help customers of Paws & Polish check grooming availability.",
    schedule_tool,
)

print("Type a message, or type quit to stop.")
user_message = input("You: ")

while user_message.lower() != "quit":
    print(f"{assistant.name}: {assistant.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(assistant.history)}")
