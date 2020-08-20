from django.contrib import admin
from .models import (FacebookUser, FacebookDevice,
                     User, PaymentHistory, RegisterService, FacebookAction, FacebookActionScript, FaceActScri
                     )

# Register your models here.


class FaceBookUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active',)


class RegisterServiceAdmin(admin.ModelAdmin):
    list_display = ('user', 'facebook_package', 'youtube_package', 'tiktok_package', 'shoppe_package',)


class PaymentHistoryAdmin(admin.ModelAdmin):
    def time_seconds(self, obj):
        return obj.created_at.strftime("%d-%m-%Y %H:%M:%S")

    time_seconds.admin_order_field = 'created_at'
    time_seconds.short_description = 'Created time'
    list_display = ('user', 'price', 'source', 'time_seconds', )


admin.site.register(User)
admin.site.register(FacebookDevice)
admin.site.register(FacebookUser, FaceBookUserAdmin)
admin.site.register(PaymentHistory, PaymentHistoryAdmin)
admin.site.register(RegisterService, RegisterServiceAdmin)
admin.site.register(FacebookAction)
admin.site.register(FacebookActionScript)
admin.site.register(FaceActScri)

