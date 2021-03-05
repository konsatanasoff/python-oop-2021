from datetime import datetime, timedelta


class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.datetime_obj = datetime(100, 1, 1, hour=hours, minute=minutes, second=seconds)

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return self.datetime_obj.strftime("%H:%M:%S")

    def next_second(self):
        self.datetime_obj = self.datetime_obj + timedelta(seconds=1)
        self.hours = self.datetime_obj.hour
        self.minutes = self.datetime_obj.minute
        self.seconds = self.datetime_obj.second
        return self.datetime_obj.strftime("%H:%M:%S")


time = Time(9, 30, 59)
print(time.next_second())

time = Time(10, 59, 59)
print(time.next_second())

time = Time(23, 59, 59)
print(time.next_second())
