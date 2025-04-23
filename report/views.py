from django.http import JsonResponse

from report.models import Report
from report.tasks import generate_report_task


def generate_report_view(request):
    report = Report.objects.create()
    task = generate_report_task.delay(report.pk)

    return JsonResponse({
        "status": "The report is being generated...",
        "task_id": task.id,
    })
