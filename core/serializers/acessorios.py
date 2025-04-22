
from rest_framework.serializers import ModelSerializer

from core.models import Acessorio

class AcessorioSerializer(ModelSerializer):
    class meta:
        model = Acessorio
        fields = "__all__"