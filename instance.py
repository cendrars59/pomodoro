__author__ = 'Cyril Leroux'

ELAPSED_TIME_IN_SECOND = 1
REMAINING_ITERATIONS = 2

from time import sleep


def counting_down(remaining_duration_in_seconds):

    while remaining_duration_in_seconds != 0:
        remaining_duration_in_seconds = remaining_duration_in_seconds - ELAPSED_TIME_IN_SECOND
        sleep(ELAPSED_TIME_IN_SECOND)


def converting_minutes_in_seconds(duration_in_minutes):
    return int(duration_in_minutes*60)


while REMAINING_ITERATIONS != 0:
    counting_down(converting_minutes_in_seconds(1))
    REMAINING_ITERATIONS -= 1

print('time is up')
