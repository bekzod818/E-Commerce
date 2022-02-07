from django.urls import path
from .views import coupon_apply

urlpatterns = [
    path("apply/", coupon_apply, name="apply"),
]
