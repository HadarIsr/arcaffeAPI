from apscheduler.schedulers.blocking import BlockingScheduler
import requests

URL_FOR_UPDATE_MENU = 'http://127.0.0.1:8000/admin/update_menu/admin/admin'


def update_menu():
    requests.get(URL_FOR_UPDATE_MENU)


scheduler = BlockingScheduler()
scheduler.add_job(update_menu, 'interval', hour=24)
scheduler.start()
