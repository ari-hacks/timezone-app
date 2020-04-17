import rumps
import datetime
import pytz
import os 
import sys
import importlib

class TimeZone(object):
    def __init__(self):
        super(TimeZone, self)
        self.config = {
            "app_name": "TimeZone",
            "ld_current_time" : "London 🇬🇧  " +  datetime.datetime.now(pytz.timezone('Europe/London')).strftime('%I:%M:%S %p'),
            "ny_current_time" : "New York  🗽 " + datetime.datetime.now(pytz.timezone('US/Eastern')).strftime('%I:%M:%S %p') ,
            "la_current_time" : "Los Angeles 🏠 " + datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('%I:%M:%S %p'),
         }
        self.app = rumps.App(self.config["app_name"],icon='tz.icns')
        self.ld = rumps.MenuItem(title=self.config["ld_current_time"],callback='')
        self.ny = rumps.MenuItem(title=self.config["ny_current_time"],callback='')
        self.la = rumps.MenuItem(title=self.config["la_current_time"],callback='')
        self.set_up_menu()


    def set_up_menu(self):
        self.app.menu = [self.ld,self.ny,self.la]


    @rumps.clicked('Restart')
    def about(self):
            print('restarted')
            os.execl(sys.executable, sys.executable, * sys.argv)



    def run(self):
        self.app.run()

if __name__ == '__main__':
    app = TimeZone()
    app.run()