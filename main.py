from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from plyer import notification
import datetime

class AlarmApp(App):
    def build(self):
        self.base_hour = 7
        self.base_minute = 0
        self.offset = 0
        self.check_alarm()
        return Label(text="⏰ Smart Alarm Running")

    def check_alarm(self):
        now = datetime.datetime.now()
        alarm_time = now.replace(
            hour=self.base_hour, minute=self.base_minute, second=0, microsecond=0
        ) - datetime.timedelta(minutes=self.offset)

        if now.hour == alarm_time.hour and now.minute == alarm_time.minute:
            notification.notify(title="Wake Up!", message="⏰ Alarm ringing!")
            self.offset += 1  # Next day earlier

        Clock.schedule_once(lambda dt: self.check_alarm(), 30)

if __name__ == "__main__":
    AlarmApp().run()
