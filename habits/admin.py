from django.contrib import admin
from habits.models import Habits

# Register your models here.


@admin.register(Habits)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "owner",
        "last_remind",
        "is_nice_habit",
        "related_habit",
    )
    search_fields = ("owner", "name")
    ordering = ("id", "name")
    list_filter = ("id", "owner")
