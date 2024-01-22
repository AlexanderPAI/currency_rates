from django.db import models


class RateRequest(models.Model):
    """Модель запроса курса валюты."""
    request_date = models.DateTimeField(
        verbose_name='Дата и время запроса',
        auto_now_add=True,
        db_index=True,
    )
    currency_name = models.CharField(
        verbose_name='Название валюты 1',
        help_text='Полное название валюты 1 (например, "Доллар США")',
        max_length=200,
    )
    currency_code = models.CharField(
        verbose_name='Код валюты 1',
        help_text='Международный код валюты 1 в соответствии с ISO 4217 (Общепринятый стандарт)',
        max_length=3,
    )
    target_currency = models.CharField(
        verbose_name='Название валюты 2',
        help_text='Полное название валюты 2 (например, "Российский рубль")',
        max_length=200,
    )
    target_currency_code = models.CharField(
        verbose_name='Код валюты 2',
        help_text='Международный код целевой валюты в соответствии с ISO 4217 (Общепринятый стандарт)',
        max_length=3,
    )
    rate = models.FloatField(
        verbose_name='Курс',
    )

    class Meta:
        ordering = ('-request_date',)
        verbose_name = 'Запрос курса валюты'
        verbose_name_plural = 'Запросы курсов валют'

    def __str__(self):
        return f'{self.currency_code}/{self.target_currency_code}'
