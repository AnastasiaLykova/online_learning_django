from subscription.apps import SubscriptionConfig
from django.urls import path

from subscription.views import SubscriptionListAPIView, SubscriptionCreateAPIView, SubscriptionDestroyAPIView

app_name = SubscriptionConfig.name

urlpatterns = [
    path('', SubscriptionListAPIView.as_view(), name='list'),
    path('create/', SubscriptionCreateAPIView.as_view(), name='create'),
    path('delete/<int:pk>/', SubscriptionDestroyAPIView.as_view(), name='delete'),
]