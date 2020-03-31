import rumps 
import datetime
from datetime import datetime
from pytz import timezone
import pendulum
import logging
logging.basicConfig(level = logging.DEBUG)

class TimeZone(object):
    def __init__(self):
        now_in_london = pendulum.now('Europe/London')
        now_in_newyork = pendulum.now('US/Eastern')
        now_in_losangeles = pendulum.now('America/Los_Angeles')
 
        self.config = {
            "app_name": "TimeZone",
            "ld_current_time" : "London " + str(now_in_london.to_day_datetime_string()),
            "ny_current_time" : "New York " + str(now_in_newyork.to_day_datetime_string()),
            "la_current_time" : "Los Angeles " + str(now_in_losangeles.to_day_datetime_string())
         }
        self.app = rumps.App(self.config["app_name"])
        self.set_up_menu()
        self.la_time = rumps.MenuItem(title=self.config["la_current_time"], callback=exit)
        self.ld_time = rumps.MenuItem(title=self.config["ld_current_time"], callback=exit)
        self.ny_time = rumps.MenuItem(title=self.config["ny_current_time"], callback=exit)
        self.app.menu = [self.la_time, self.ny_time, self.ld_time]

    def set_up_menu(self):
        #logging.debug()
        self.app.title = "⏳"

    def run(self):
        self.app.run()

if __name__ == '__main__':
    app = TimeZone()
    app.run()