from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Github, Language, Media
from datetime import datetime, timedelta


@api_view(["GET"])
def language(request, keyword):
    repository = request.GET.get('repository', '')
    start_date = request.GET.get('start_date', datetime.today() - timedelta(days=7))
    end_date = request.GET.get('end_date', datetime.today())
    try:
        github = Github.objects.get(repository=repository)
    except Github.DoesNotExist:
        return JsonResponse({'message': 'Repository does not exist!'})

    if keyword == 'file_and_folder':
        try:
            item = Media.objects \
                .filter(github=github, date__range=[start_date, end_date]) \
                .order_by('date') \
                .values()
        except Language.DoesNotExist:
            return JsonResponse({'message': 'Media does not exist!'})
    else:
        try:
            item = Language.objects \
                .filter(type=keyword, github=github, date__range=[start_date, end_date]) \
                .order_by('date') \
                .values()
        except Language.DoesNotExist:
            return JsonResponse({'message': 'Language does not exist!'})

    return JsonResponse(list(item), safe=False)


@api_view(["GET"])
def cron(request):
    from api.cron import scheduled_job
    scheduled_job()
    return JsonResponse({'message': 'success'})


@api_view(["GET"])
def dump(request):
    from api.dump import dump_data
    dump_data()
    return JsonResponse({'message': 'success'})
