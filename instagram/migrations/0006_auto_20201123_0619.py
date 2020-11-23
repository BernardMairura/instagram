# Generated by Django 3.1.3 on 2020-11-23 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0005_auto_20201122_1949'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-date_created']},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-last_update']},
        ),
        migrations.AddField(
            model_name='profile',
            name='last_update',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]