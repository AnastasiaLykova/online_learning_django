import stripe
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from config import settings
from payments.models import Payments
from payments.serializers import PaymentsSerializer


class PaymentsListAPIView(ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ('course', 'lesson', 'payment_method',)
    ordering_fields = ['datetime']
#     permission_classes = [IsAuthenticated]


class PaymentsCreateAPIView(generics.CreateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer

    def perform_create(self, serializer):
        payment = serializer.save()
        payment.user = self.request.user
        payment.save()
        stripe.api_key = settings.DJANGO_STRIPE_API_KEY
        pay = stripe.PaymentIntent.create(
            amount=payment.payment_amount,
            currency="usd",
            automatic_payment_methods={"enabled": True},
        )
        pay.save()
        return super().perform_create(serializer)


class GetPaymentsView(APIView):
    def get(self, request, payment_id):
        stripe.api_key = settings.DJANGO_STRIPE_API_KEY
        payment_intent = stripe.PaymentIntent.retrieve(payment_id)
        return Response({
            'status': payment_intent.status,
            'body': payment_intent})
