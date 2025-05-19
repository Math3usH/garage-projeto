from rest_framework.serializers import ModelSerializer

from core.models import Veiculo

class VeiculoSerializer(ModelSerializer):
    class meta:
        model = Veiculo
        fields = "__all__"