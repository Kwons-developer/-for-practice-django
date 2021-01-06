from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

"""admin.site.register(models.User, CustomUserAdmin) 이 코드랑 아래 코드 똑같은것 어드민 에 등록하는것임"""


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "gender",
                    "avatar",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
