from django.utils import timezone
from django.utils.timezone import localtime


def get_duration(visit_time):
    enter_time = localtime(visit_time.entered_at)
    if visit_time.leaved_at == None:
        date_now = timezone.localtime(timezone.now())
        delta = date_now - enter_time
    else:
        leaved_time = localtime(visit_time.leaved_at)
        delta = leaved_time - enter_time
    return delta

def format_duration(duration):
    total_seconds=duration.seconds
    hour = total_seconds // 3600
    minute = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hour}:{minute}:{seconds}"