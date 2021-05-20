from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Billing)
admin.site.register(Client)
admin.site.register(Project)
admin.site.register(PaymentType)
admin.site.register(Account)