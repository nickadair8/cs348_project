from django.contrib import admin
from .models import LegoSet
from .models import Customer
from .models import Reviews
from .models import Theme
# Register your models here.
admin.site.register(LegoSet)
admin.site.register(Customer)
admin.site.register(Reviews)
admin.site.register(Theme)