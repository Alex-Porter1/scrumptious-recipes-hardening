from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.core.paginator import Paginator


from meal_plans.models import MealPlan


class MealPlanListView(ListView):
    model = MealPlan
    template_name = "meal_plan/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = MealPlan
    template_name = "meal_plan/new.html"
    fields = ["name", "date", "recipes"]
    success_url = reverse_lazy("meal_plan_detail")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class DetailView(LoginRequiredMixin, DetailView):
    model = MealPlan
    template_name = "meal_plan/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
