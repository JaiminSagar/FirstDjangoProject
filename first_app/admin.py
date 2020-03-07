from django.contrib import admin
from first_app.models import AccessRecord,Topic,Webpage,User_Model,UserProfileInfo
# Register your models here.
admin.site.register(Topic)
admin.site.register(AccessRecord)
admin.site.register(Webpage)
admin.site.register(User_Model)
admin.site.register(UserProfileInfo)