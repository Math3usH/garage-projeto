from rest_framework.viewsets import ModelViewSet

from core.serializers import AcessorioSerializer

from core.models import Acessorio

class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer  