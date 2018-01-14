from django.contrib import admin
from djapp.models import Performer, Album, Genre, Track
# Register your models here.

class MyModelAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields if field.name != "id"]
        super(MyModelAdmin, self).__init__(model, admin_site)

admin.site.register(Performer, MyModelAdmin)
admin.site.register(Album, MyModelAdmin)
admin.site.register(Genre, MyModelAdmin)
admin.site.register(Track, MyModelAdmin)

