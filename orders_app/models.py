from django.db import models

from fabrics_app.models import Fabric

class Order(models.Model):
    PROCESS_STATUS_CHOICES = [
        ('completed', 'Выполнен'),
        ('refusal', 'Отказ'),
        ('in_progress', 'В процессе'),
        ('new', 'Новый'),
    ]
    last_name = models.CharField(
        'Фамилия',
        max_length=50
    )
    first_name = models.CharField(
        'Имя',
        max_length=50
    )
    phone_number = models.CharField(
        'Номер телефона',
        max_length= 12
    )
    email = models.EmailField(
        'Электронная почта',
        max_length=100
    )
    address = models.CharField(
        max_length=255,
        verbose_name="Адрес доставки"
    )
    comment = models.TextField(
        verbose_name='Комментарий'
    )
    process_status = models.CharField(
        max_length=30,
        choices=PROCESS_STATUS_CHOICES,
        default='new',
        verbose_name="Статус заявки"
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ {self.id} от {self.process_status}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='order_items'
    )
    fabric = models.ForeignKey(
        Fabric,
        on_delete=models.CASCADE
    )
    

    def __str__(self):
        return f"{self.fabric.name} "
