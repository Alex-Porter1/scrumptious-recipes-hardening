from django.contrib import admin

# Register your models here.
from meal_plans.models import MealPlan


class MealPlanAdmin(admin.ModelAdmin):
    pass


admin.site.register(MealPlan, MealPlanAdmin)
