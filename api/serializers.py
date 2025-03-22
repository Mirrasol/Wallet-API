from rest_framework import serializers
from .models import Wallets


class WalletsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallets
        fields = ['uuid', 'balance']


class OperationSerializer(serializers.Serializer):
    operation_type = serializers.ChoiceField(choices=['DEPOSIT', 'WITHDRAW'])
    amount = serializers.DecimalField(max_digits=10, min_value=0.000, decimal_places=3)
