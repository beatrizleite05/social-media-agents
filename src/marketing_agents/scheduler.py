from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import pytz, asyncio
from .pipeline import generate_post
from .config import TIMEZONE, POST_HOUR

scheduler = BlockingScheduler(timezone=pytz.timezone(TIMEZONE))

@scheduler.scheduled_job(CronTrigger(hour=POST_HOUR, minute=0))
def daily_job():
    asyncio.run(generate_post(publish=False))


def start_scheduler():
    print(f"Scheduler started - daily post at {POST_HOUR}:00 ({TIMEZONE})")
    sched.start() 