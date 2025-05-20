from django.contrib import admin
from .models import Adoption, Donation, Volunteer, Contact

admin.site.register(Adoption)
admin.site.register(Donation)
admin.site.register(Volunteer)
admin.site.register(Contact)
