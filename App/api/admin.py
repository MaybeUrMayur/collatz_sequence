from django.contrib import admin
from .models import CollatzHistory

@admin.register(CollatzHistory)
class CollatzHistoryAdmin(admin.ModelAdmin):
    list_display = ('starting_number', 'total_steps', 'max_value', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('starting_number',)
    readonly_fields = ('created_at', 'sequence')
    
    fieldsets = (
        ('Sequence Information', {
            'fields': ('starting_number', 'total_steps', 'max_value')
        }),
        ('Sequence Data', {
            'fields': ('sequence',)
        }),
        ('Metadata', {
            'fields': ('created_at',)
        }),
    )
