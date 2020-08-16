from django.contrib import admin
from .models import FacebookUser
# Register your models here.


class FaceBookUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active',)


admin.site.register(FacebookUser, FaceBookUserAdmin)
