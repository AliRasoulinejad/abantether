# Generated by Django 5.0.6 on 2024-07-07 18:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('coin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='coin.coin')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]