from django.db import transaction
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response
from .models import Wallets
from .serializers import OperationSerializer


class WalletsRepository:
    """
    A repository that handles allowed wallet operations
    within the database.
    """
    def conduct_operation(self, wallet_uuid, data):
        serializer = OperationSerializer(data=data)
        if serializer.is_valid():
            operation_type = serializer.validated_data['operation_type']
            amount = serializer.validated_data['amount']

            with transaction.atomic():
                try:
                    wallet = Wallets.objects.select_for_update().get(uuid=wallet_uuid)
                except ValidationError:
                    return Response(
                        {"detail": "Wallet not found."},
                        status=status.HTTP_404_NOT_FOUND,
                    )

                if operation_type == 'DEPOSIT':
                    wallet.balance += amount
                elif operation_type == 'WITHDRAW':
                    if wallet.balance < amount:
                        return Response(
                            {"detail": "Insufficient funds."},
                            status=status.HTTP_400_BAD_REQUEST,
                        )
                    wallet.balance -= amount
                wallet.save()

            return Response(
                {"detail": "Operation successful."},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"detail": "Invalid operation or amount."},
            status=status.HTTP_400_BAD_REQUEST,
        )
