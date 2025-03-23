from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Wallets
from .repository import WalletsRepository
from .serializers import WalletsSerializer


class WalletsViewSet(viewsets.ModelViewSet):
    queryset = Wallets.objects.all()
    serializer_class = WalletsSerializer
    repository = WalletsRepository()
    http_method_names = ['get', 'post']

    @action(detail=True, methods=['post'])
    def operation(self, request, pk=None):
        data = request.data
        wallet_uuid = pk
        response = self.repository.conduct_operation(wallet_uuid, data)
        return response
