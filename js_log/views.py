import hashlib
from datetime import datetime

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from js_log.models import Error

@csrf_exempt
def log_error(request):
    details =  request.POST.get('details')
    if not details:
        return HttpResponse('')
    m = hashlib.md5()
    m.update(details)
    md5_digest = m.hexdigest()
    error_query = Error.objects.filter(hexdigest=md5_digest)
    now = datetime.now()
    if not error_query.exists():
        error = Error(
            hexdigest = md5_digest,
            first_happened = now,
            last_happened = now,
            details = details,
            number = 1,
        )
        error.save()
    else:
        error = error_query[0]
        error.number += 1
        error.last_happened = now
        error.save()
    return HttpResponse('OK')

