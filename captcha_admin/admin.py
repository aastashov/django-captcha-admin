from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.models import Group, User

from .forms import AdminAuthenticationForm
from .mixins import AdminSiteRegistryFix


class AdminSite(admin.AdminSite, AdminSiteRegistryFix):
    login_form = AdminAuthenticationForm
    login_template = 'admin/captcha_login.html'


site = AdminSite()
admin.site = site

admin.site.register(Group, GroupAdmin)
admin.site.register(User, UserAdmin)
