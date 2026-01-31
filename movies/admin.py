from django.contrib import admin, messages
from .models import Movie, Review
from django.utils.translation import ngettext
class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']
class ReviewAdmin(admin.ModelAdmin):
    list_filter = [('is_reported', admin.BooleanFieldListFilter)]
    actions = ["unreport"]
    
    @admin.action(description="Unhide selected reviews")
    def unreport(self, request, queryset):
        updated = queryset.update(is_reported=False)
        self.message_user(
            request,
            ngettext(
                "%d story was successfully marked as published.",
                "%d stories were successfully marked as published.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)
# Register your models here.
