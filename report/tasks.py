import time

from celery import shared_task

from report.models import Report


@shared_task
def generate_report_task(report_id, **kwargs):
    report = Report.objects.get(id=report_id)

    # Simulate a long-running report generation
    time.sleep(15)
    report.content = "testdriven.io is cool!"
    report.is_ready = True
    report.save()

    return "The report has been successfully generated!"


"""
/report/generate-report/
{
"status": "The report is being generated...",
"task_id": "c75f226c-6860-446a-9231-2bd0b89e495c"
}
"""
