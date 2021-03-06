# Generated by Django 2.2.3 on 2019-11-28 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SuccessNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InvId', models.IntegerField(db_index=True, verbose_name='Номер заказа')),
                ('OutSum', models.CharField(max_length=15, verbose_name='Сумма')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время получения уведомления')),
            ],
            options={
                'verbose_name': 'Уведомление об успешном платеже',
                'verbose_name_plural': 'Уведомления об успешных платежах (ROBOKASSA)',
            },
        ),
    ]
