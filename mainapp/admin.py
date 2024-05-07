from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Contact

# Register your models here.

admin.site.register(Contact)


# **************************************
# Newsletter
from .models import NewsletterUser
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email','date_added')

admin.site.register(NewsletterUser, NewsletterAdmin)