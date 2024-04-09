from django.utils.timezone import localtime
from datacenter.models import Visit
from django.shortcuts import render
from .localtime_duration import get_duration, format_duration


def storage_information_view(request):
    visiters_inside = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in visiters_inside:
        duration = get_duration(visit)
        entry_time = localtime(visit.entered_at)
        visit_time = format_duration(duration) 
        visiter = visit.passcard

        non_closed_visits.append( 
            {
                'who_entered': visiter,
                'entered_at': entry_time,
                'duration': visit_time,
            }
        )
    context = {
        'non_closed_visits': non_closed_visits, 
    }
    return render(request, 'storage_information.html', context)
