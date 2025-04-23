from django.contrib import admin
from django.db import transaction
from django.shortcuts import redirect
from django.urls import path, reverse

from report.models import Report
from report.tasks import generate_report_task


from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.admin.apps import AdminConfig
from celery.result import AsyncResult


class ReportAdmin(admin.ModelAdmin):
    list_display = ["__str__", "created_at", "updated_at", "is_ready"]
    change_list_template = "admin/report/change_list.html"
    readonly_fields = ["created_at", "updated_at"]

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "generate/",
                self.admin_site.admin_view(self.admin_generate_report_view),
                name="reports_generate",
            ),
        ]
        return custom_urls + urls

    def admin_generate_report_view(self, request):
        with transaction.atomic():
            report = Report.objects.create()

        redirect_url = reverse("admin:reports_report_change", kwargs={
            "object_id": report.id,
        })
        result = generate_report_task.delay(
            report_id=report.id,
            redirect_url=redirect_url,
        )

        self.message_user(request, "Started generating a report...")
        return redirect("admin:task_status", result.id)


admin.site.register(Report, ReportAdmin)


class CustomAdminSite(admin.AdminSite):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "task-status/<str:task_id>/",
                self.admin_view(self.admin_task_status_view),
                name="task_status",
            )
        ]
        return custom_urls + urls

    def admin_task_status_view(self, request, task_id):
        task = AsyncResult(task_id)
        task_data = {
            "id": task.id,
            "name": task.name,
            "args": task.args,
            "kwargs": task.kwargs,
            "state": task.state,
        }

        # Return JSON response if requested
        if request.headers.get("Accept", "").startswith("application/json"):
            return JsonResponse(task_data)

        # Otherwise, render HTML response
        return render(
            request,
            "admin/task_status.html",
            {
                "title": "Task Status",
                "task": task_data,
            },
        )
