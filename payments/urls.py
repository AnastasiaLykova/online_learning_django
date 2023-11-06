from django.urls import path

from payments.apps import PaymentsConfig
from payments.views import PaymentsListAPIView, GetPaymentsView, PaymentsCreateAPIView

app_name = PaymentsConfig.name

urlpatterns = [
      path('list/', PaymentsListAPIView.as_view(), name='payment_list'),
      path('payment/<str:payment_id>/', GetPaymentsView.as_view(), name='payment_get'),
      path('create/', PaymentsCreateAPIView.as_view(), name='payment_create'),
]
