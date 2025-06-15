# order/viwesets.py

from rest_framework import viewsets
from rest_framework.exceptions import ParseError, NotFound
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication # autenticação
from rest_framework.permissions import IsAuthenticated # permissoes

from .serializers import OrderSerializer
from .models import Order

class OrderViewSet(viewsets.ModelViewSet):
    # serializers
    serializer_class = OrderSerializer

    authentication_classes = [
        SessionAuthentication, 
        BasicAuthentication, 
        TokenAuthentication,
        ]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Order.objects.all()

        # filtro por usuario
        user_filter = self.request.query_params.get('user', None)
        if user_filter is not None:
            try: # mostra o filtro por usuario caso seja valido
                queryset = queryset.filter(user=user_filter)
            except ValueError: # Informa que o formato colocado não e valido
                raise ParseError(detail=f'User [{user_filter}] not valid')
            if not User.objects.filter(id=user_filter).exists(): # verifica se o usuario existe
                raise NotFound(detail=f'User [{user_filter}] not exists')
        return queryset