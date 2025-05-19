from dill.tests.test_recursive import Model
from rest_framework.serializers import ModelSerializer

from core.models import Modelo

class ModeloSerializer(ModelSerializer):
    class meta:
        model = Modelo
        fields = "__all__"