# Generated by Django 3.2.4 on 2021-06-22 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_libro_categoria_libro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria_libro',
            name='id',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='id',
        ),
        migrations.AddField(
            model_name='categoria_libro',
            name='id_categoria',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='libro',
            name='id_libro',
            field=models.IntegerField(default=2, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
