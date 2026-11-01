# my_tool.py
# Author: Ashley Marte


class GroomingSchedule:
    """A tool that stores available grooming appointment times."""

    def __init__(self, open_times):
        """Store the available times for each day."""
        self.open_times = open_times

    def find_day(self, text):
        """Return the first known day mentioned, or None."""
        for day in self.open_times:
            if day in text.lower():
                return day
        return None

    def times_for(self, day):
        """Return available times for a day, or None if unknown."""
        if day in self.open_times:
            return self.open_times[day]
        return None
