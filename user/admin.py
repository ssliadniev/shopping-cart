from django.contrib import admin
from django.contrib.auth.models import User, Group


class UserAdmin(admin.ModelAdmin):

    fieldsets = [
        ("General info:", {"fields": ["username", "first_name", "last_name"]}),
        ("Contact info:", {"fields": ["phone", "address", "email"]}),
        (
            "Confidence info:",
            {
                "fields": [
                    "is_superuser",
                    "is_staff",
                    "is_active",
                    "password",
                    "last_login",
                    "date_joined",
                ]
            },
        ),
    ]

    list_display_links = ("first_name", "last_name", "email")
    list_filter = ["last_name"]
    search_fields = (
        "first_name",
        "last_name"
    )


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

