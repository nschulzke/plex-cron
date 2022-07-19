import os
dir_path = os.path.dirname(os.path.realpath(__file__))
from crontab import CronTab

with CronTab(user=True) as cron:
    cron.remove_all()

    # Example with 
    job = cron.new(command=f'python {dir_path}/plex.py "Kitchen Display" "Christmas Music"')
    job.dow.on('SUN', 'MON', 'TUE')
    job.hour.on(17)
    job.minute.on(0)

    # Example with shuffle and specifying the month
    job = cron.new(command=f'python {dir_path}/plex.py "Kitchen Display" "Christmas Music" --shuffle')
    job.month.on('DEC')
    job.hour.on(8)
    job.minute.on(0)
