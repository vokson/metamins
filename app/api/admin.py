from django.contrib import admin

from .forms import AccountAdminForm, TransactiontAdminForm
from .models import Account, Transaction


class AccountAdmin(admin.ModelAdmin):
    form = AccountAdminForm

    list_display = ('pk', 'card', 'name', 'surname', 'balance', 'phone', 'created',)
    search_fields = ('card', 'surname', 'phone',)
    list_filter = ('created',)
    empty_value_display = '-пусто-'

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('card', 'balance',)
        return ()


class TransactionAdmin(admin.ModelAdmin):
    form = TransactiontAdminForm

    list_display = ('pk', 'account', 'type', 'amount', 'date',)
    list_filter = ('type', 'date',)
    empty_value_display = '-пусто-'

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)
