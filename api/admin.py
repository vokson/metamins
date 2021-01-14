from django.contrib import admin

from .models import Account
from .forms import AccountAdminForm


class AccountAdmin(admin.ModelAdmin):
    form = AccountAdminForm

    list_display = ('pk', 'card', 'name', 'surname', 'balance', 'phone', 'created')
    search_fields = ('card', 'surname', 'phone')
    list_filter = ('created',)
    empty_value_display = '-пусто-'

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('card', 'balance',)
        return ()


admin.site.register(Account, AccountAdmin)
