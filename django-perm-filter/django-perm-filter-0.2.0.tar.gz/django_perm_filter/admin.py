from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.utils.module_loading import import_string

from django_perm_filter.mixins import PermissionFilterMixin
from django_perm_filter.settings import api_settings

User = get_user_model()

user_admin = import_string(api_settings.USER_ADMIN)
group_admin = import_string(api_settings.GROUP_ADMIN)


class UserAdmin(PermissionFilterMixin, user_admin):
    pass


class GroupAdmin(PermissionFilterMixin, group_admin):
    pass


# Override default registered Admin for User and Group
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)
