# booking/serializers.py
from rest_framework import serializers
from .models import Booking
from .utils.trail_api_client import get_trail  # Função que busca a trilha via API
from .utils.trail_api_client import get_users # Função que busca o usuário via API

class BookingSerializer(serializers.ModelSerializer):
    trail_details = serializers.SerializerMethodField()  # Campo customizado
    user_details = serializers.SerializerMethodField()  # Campo customizado

    class Meta:
        model = Booking
        fields = ['id', 'user_id', 'user_details', 'trail_id', 'trail_details', 'status']  # Inclui os detalhes
    
    def validate_trail_id(self, value):
        # Verifica se a trilha existe antes de criar a review
        if not get_trail(value):
            raise serializers.ValidationError("Trilha não encontrada")
        return value

    def get_trail_details(self, obj):
        return get_trail(obj.trail_id)  # Busca os dados da trilha via API
    
    def validate_user_id(self, value):
        if not get_users(value):
            raise serializers.ValidationError("Usuário não encontrado")
        return value
    
    def get_user_details(self, obj):
        return get_users(obj.user_id)  # Campo correto: user_id