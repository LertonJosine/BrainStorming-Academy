# Generated by Django 4.1.7 on 2023-02-16 13:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0002_alter_curso_professores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='professores',
            field=models.ManyToManyField(related_name='professores', to=settings.AUTH_USER_MODEL),
        ),
    ]
