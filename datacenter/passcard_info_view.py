from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils.timezone import localtime
from .localtime_duration import get_duration, format_duration


def is_visit_long(visit, minutes=60):
    time = minutes*60
    long_visit = visit.seconds>time
    return long_visit
    
    
def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard,passcode=passcode)
    one_passcard_visits = Visit.objects.filter(passcard=passcard)
    visits_info = []
    for visit in one_passcard_visits:
        duration = get_duration(visit)
        entry_time = localtime(visit.entered_at)
        visit_time = format_duration(duration)
        long_visit = is_visit_long(duration)
        
        visits_info.append(
            {
                'entered_at': entry_time,
                'duration': visit_time,
                'is_strange': long_visit
            }
        )
        
    context = {
        'passcard': passcard,
        'this_passcard_visits': visits_info
    }
    return render(request, 'passcard_info.html', context)
