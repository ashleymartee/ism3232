from my_assistant import GroomingAssistant
from my_tool import GroomingSchedule


def make_assistant():
    """Build a fresh assistant with a schedule tool for each test."""
    schedule_tool = GroomingSchedule(
        {
            "monday": "9:00 am and 2:30 pm",
            "wednesday": "11:00 am",
            "friday": "none",
        }
    )
    return GroomingAssistant("Bella", "Be helpful.", schedule_tool)


def test_availability_question_uses_schedule_tool():
    assistant = make_assistant()
    reply = assistant.respond("What times are open on Monday?")
    assert reply == "Available grooming times on monday: 9:00 am and 2:30 pm."


def test_question_without_known_day_asks_for_day():
    assistant = make_assistant()
    assert "Which day?" in assistant.respond("What times are available?")


def test_booking_request_goes_to_staff():
    assistant = make_assistant()
    assert "staff member" in assistant.respond("Please book me for Monday")


def test_unknown_request_gets_safe_reply():
    assistant = make_assistant()
    assert "not sure" in assistant.respond("Do you validate parking?")


def test_history_records_both_messages():
    assistant = make_assistant()
    assistant.respond("hello")
    assistant.respond("What is open on Friday?")
    assert len(assistant.history) == 4
