from django.contrib import admin

from apps.gcd.models import Indexer

class IndexerAdmin(admin.ModelAdmin):
    search_fields = ('user__first_name', 'user__last_name',
                     'user__username', 'user__email')
    readonly_fields = ('registration_key',)
    list_display = ('id', 'user', 'registration_expires', 'registration_key')
    list_display_links = ('id', 'user')
    list_filter = ('is_new', 'registration_expires')
    list_editable = ('registration_expires',)
    fieldsets = (
        (None, {
            'fields': ('user', 'is_banned',
                       'registration_key', 'registration_expires'),
        }),
        ('Indexing', {
            'fields': ('mentor', 'is_new', 'max_reservations', 'max_ongoing'),
        }),
        ('Profile', {
            'fields': ('country', 'languages', 'interests', 'deceased'),
        }),
    )
    filter_horizontal = ('languages',)

admin.site.register(Indexer, IndexerAdmin)

