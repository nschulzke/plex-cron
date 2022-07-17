from crontab import CronTab

with CronTab(user=True) as cron:
    cron.remove_all()

    job = cron.new(command='python /home/nathan/personal/cast/plex.py "Kitchen Display" "Christmas Music"')
    job.dow.every('SUN', 'MON', 'TUE')
    job.hour.on(16)
    job.minute.on(17)
