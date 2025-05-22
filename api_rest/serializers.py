from rest_framework import serializers
from .models import Monografia

class MonografiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monografia
        fields = '__all__'
        extra_kwargs = {
            'titulo': {'help_text': 'Título completo da monografia'},
            'arquivo': {'help_text': 'Envie um PDF de até 5MB'}
        }
