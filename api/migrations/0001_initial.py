# Generated by Django 5.1.7 on 2025-03-22 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wallets',
            fields=[
                ('uuid', models.UUIDField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('balance', models.DecimalField(decimal_places=3, default=0.0, max_digits=15)),
            ],
        ),
    ]
