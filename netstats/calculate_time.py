from datetime import datetime, timedelta
import time


def schedule_ping(date, start_time, finish_time):
    split_start_time = (date.split("-"))+(start_time.split(":"))

    start_time = datetime(int(split_start_time[0]), int(split_start_time[1]), int(
        split_start_time[2]), int(split_start_time[3]), int(split_start_time[4]))

    split_finish_time = (date.split("-"))+(finish_time.split(":"))
    finish_time = datetime(int(split_finish_time[0]), int(split_finish_time[1]), int(
        split_finish_time[2]), int(split_finish_time[3]), int(split_finish_time[4]))

    seconds_to_execution = (start_time - datetime.now()).total_seconds()

    duration = (finish_time-start_time).total_seconds()

    return seconds_to_execution, duration
