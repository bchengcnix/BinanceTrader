from django.contrib import admin

# Register your models here.
from payload.balances.models import Balance

admin.site.register(Balance)