# my_assistant.py
# Author: Ashley Marte

HANDOFF_WORDS = ["book", "cancel", "reschedule"]


class GroomingAssistant:
    """A mock grooming appointment assistant."""

    def __init__(self, name, instructions, schedule_tool):
        """Store the assistant's details, tool, and conversation history."""
        self.name = name
        self.instructions = instructions
        self.schedule_tool = schedule_tool
        self.history = []

    def respond(self, user_message):
        """Record the user message and assistant reply."""
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """Choose a reply using simple keyword rules."""
        text = user_message.lower()

        if self.needs_human(text):
            return (
                "I can't change the grooming schedule. "
                "I'm passing you to a staff member."
            )

        if "open" in text or "available" in text:
            return self.times_reply(user_message)

        if "hello" in text or "hi" in text:
            return f"Hello! I'm {self.name}. Ask me which grooming times are available."

        return (
            "I'm not sure how to help with that. I can check available grooming times."
        )

    def needs_human(self, text):
        """Return True when a request requires staff to change the schedule."""
        return any(word in text for word in HANDOFF_WORDS)

    def times_reply(self, user_message):
        """Use the schedule tool to answer availability questions."""
        day = self.schedule_tool.find_day(user_message)

        if day is None:
            return "Which day? I can check Monday, Wednesday, or Friday."

        times = self.schedule_tool.times_for(day)
        return f"Available grooming times on {day}: {times}."
