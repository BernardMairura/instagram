# Generated by Django 3.1.3 on 2020-11-26 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0009_auto_20201123_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_commented',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='instagram.image'),
        ),
    ]