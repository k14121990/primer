# Generated by Django 3.2.4 on 2021-06-22 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210622_0534'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='categoria_libro',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.categoria_libro'),
            preserve_default=False,
        ),
    ]
