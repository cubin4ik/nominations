from django.db import models
from django.shortcuts import reverse


class Nominations(models.Model):
    title = models.CharField(max_length=45, null=False, blank=False, unique=True, verbose_name='Номинация')
    description = models.CharField(max_length=500, null=False, blank=False, verbose_name='Описание')

    def __str__(self):
        return self.title


class Votes(models.Model):
    nomination = models.ForeignKey('Nominations',
                                   on_delete=models.CASCADE,
                                   null=False,
                                   blank=False,
                                   verbose_name='Номинация')
    voter = models.ForeignKey('account.User', on_delete=models.CASCADE, null=False, related_name='vote',
                              verbose_name='Голосующий')
    nominee = models.ForeignKey('account.User', on_delete=models.CASCADE, null=False, related_name='nominee',
                                verbose_name='Кандидат')
    reason = models.CharField(max_length=500, null=False, blank=False, verbose_name='Причина')

    class Meta:
        unique_together = ('voter', 'nomination')
        verbose_name_plural = 'votes'

    def __str__(self):
        return f"{self.nomination} - {self.voter} - {self.nominee}"

    @staticmethod
    def get_absolute_url(self):
        return reverse('index')
