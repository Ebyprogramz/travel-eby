from django.contrib import admin

from .models import brochure
from .models import testimonials
# Register your models here.

admin.site.register(brochure)
admin.site.register(testimonials)
