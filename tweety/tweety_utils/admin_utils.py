from django.contrib import admin


class AbstractModelAdmin(admin.ModelAdmin):
    list_display = ()
    list_filter = ()
    search_fields = ()
    sortable_by = ()
    ordering = ("-created_at",)

    class Meta:
        abstract = True
