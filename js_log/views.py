import hashlib
from datetime import datetime

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from js_log.models import JSError as Error

@csrf_exempt
def log_error(request):
    if not request.POST.keys():
        return HttpResponse('')
    details = 'url: %(url)s \nuser agent:%(user_agent)s  \nline number:%(line)s  \nerror message:%(message)s' % request.POST
    short_message = request.POST.get('message', '')[:128]
    user_agent = request.POST.get('user_agent', '')[:256]
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
            short_message = short_message,
            user_agent = user_agent,
        )
        error.save()
    else:
        error = error_query[0]
        error.number += 1
        error.last_happened = now
        error.save()
    return HttpResponse('OK')

