import os
dir_path = os.path.dirname(os.path.realpath(__file__))
from crontab import CronTab

with CronTab(user=True) as cron:
    cron.remove_all()

    # Example with setting days of the week
    job = cron.new(command=f'python {dir_path}/plex.py "Kitchen Display" --playlist="Christmas Music"')
    job.dow.on('SUN', 'MON', 'TUE')
    job.hour.on(17)
    job.minute.on(0)

    # Example with setting volume to 50%
    job = cron.new(command=f'python {dir_path}/plex.py "Kitchen Display" --playlist="Christmas Music" --volume=50')
    job.hour.on(17)
    job.minute.on(0)

    # Example with shuffle and specifying the month
    job = cron.new(command=f'python {dir_path}/plex.py "Kitchen Display" --playlist="Christmas Music" --shuffle')
    job.month.on('DEC')
    job.hour.on(8)
    job.minute.on(0)

    # Example with track
    job = cron.new(command=f'python {dir_path}/plex.py "Kitchen Display" --track="Also Sprach"')
    job.hour.on(17)
    job.minute.on(0)
