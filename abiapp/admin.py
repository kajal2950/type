from django.contrib import admin
from.models import Banner,Video,Category
from embed_video.admin import AdminVideoMixin


# Register your models here.
admin.site.register(Banner)

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Video, MyModelAdmin)
admin.site.register(Category)

