from rest_framework import serializers

from subscription.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):

    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Subscription
        fields = "__all__"

    def get_is_subscribed(self, obj):
        if self.context['request'].user == obj.user:
            return True
        return False
