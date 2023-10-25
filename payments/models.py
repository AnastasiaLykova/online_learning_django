from django.db import models

from course.models import Course, Lesson
from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Payments(models.Model):

    PAYMENT_CHOICES = [
        ('cash', 'наличные'),
        ('card', 'перевод на счет'),
    ]

    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE, **NULLABLE)
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='дата оплаты', **NULLABLE)
    course = models.ForeignKey(Course, verbose_name='курс', on_delete=models.CASCADE, **NULLABLE)
    lesson = models.ForeignKey(Lesson, verbose_name='урок', on_delete=models.CASCADE, **NULLABLE)
    payment_amount = models.IntegerField(verbose_name='сумма оплаты', **NULLABLE)
    payment_method = models.CharField(max_length=10, verbose_name='способ оплаты', choices=PAYMENT_CHOICES, **NULLABLE)

    def __str__(self):
        return f'{self.user} {self.payment_amount}'

    class Meta:
        verbose_name = 'оплата'
        verbose_name_plural = 'оплаты'
