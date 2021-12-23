import json
from typing import Any, Dict, List, cast
# django import
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.http.request import HttpRequest

from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django_filters.views import FilterView
# app import
from .filters import TaskListFilter
from .forms import TaskListCreateForm
from .models import TaskList


class TaskListListView(ListView):
    template_name = "pyhtmx/tasklist_list.html"
    model = TaskList

    def get_context_data(self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        print('-' * 50)
        return super().get_context_data(
            form=TaskListCreateForm(), filterset=TaskListFilter, **kwargs
        )


class TaskListFilterView(FilterView):
    filterset_class = TaskListFilter


class TaskListCreateView(CreateView):
    template_name = "htmx/create_form.html"
    model = TaskList
    form_class = TaskListCreateForm

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        task_list = form.save()
        response = HttpResponse()
        response["HX-Trigger"] = json.dumps(
            {"redirect": {"url": task_list.get_absolute_url()}}
        )
        return response


class TaskListDetailView(DetailView):
    model = TaskList


class TaskListTasksView(DetailView):
    model = TaskList


class TaskListAddTaskView(DetailView):
    model = TaskList
    template_name = "htmx/tasklist_tasks.html"

    def post(
        self, request: HttpRequest, *args: List[Any], **kwargs: Dict[str, Any]
    ) -> HttpResponse:
        cast(TaskList, self.get_object()).tasks.create()
        return self.get(request, *args, **kwargs)