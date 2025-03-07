from django.db import models

class Booking(models.Model):
    user_id = models.IntegerField()  # ID do usuário (vindo do users_service)
    trail_id = models.IntegerField()  # ID da trilha (vindo do trails_service)
    status = models.CharField(
        max_length=50,
        choices=[('pending', 'Pendente'), ('confirmed', 'Confirmado'), ('canceled', 'Cancelado')], 
        default='pending'
    )  # Status do agendamento

    def __str__(self):
        return f"Booking {self.id} - Trail ID: {self.trail_id}"
    