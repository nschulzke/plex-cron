import os
dir_path = os.path.dirname(os.path.realpath(__file__))
from crontab import CronTab

with CronTab(user=True) as cron:
    cron.remove_all()

    job = cron.new(command=f'python {dir_path}/plex.py "Kitchen Display" "Christmas Music"')
    job.dow.on('SUN', 'MON', 'TUE')
    job.hour.every(16)
    job.minute.on(41)
