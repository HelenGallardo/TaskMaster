from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["name"]   

    #Esto hace que en el panel admin aparezcan nombres legibles.
    def __str__(self):
        return self.name

class Task(models.Model):
    class Status(models.TextChoices):
        PENDIENTE = "PE","Pendiente"
        PROCESO = "PR", "Proceso"
        PAUSADA = "PA", "Pausada"
        FINALIZADA = "FI", "Finalizada"

    class Priority(models.TextChoices):
        BAJA = "B", "Baja"
        MEDIA = "M", "Media"
        ALTA = "A", "Alta"

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True) 
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.PENDIENTE)       
    priority = models.CharField(max_length=1, choices=Priority.choices, default=Priority.MEDIA)
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #claves foraneas
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="tasks")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
        ordering = ["-created_at"]  # más recientes primero    
    #Esto hace que en el panel admin aparezcan nombres legibles.
    def __str__(self):
        return self.title


