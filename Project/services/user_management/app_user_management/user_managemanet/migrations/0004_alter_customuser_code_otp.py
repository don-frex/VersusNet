# Generated by Django 4.2.16 on 2024-12-16 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_managemanet', '0003_friendship_blocked_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='code_otp',
            field=models.CharField(max_length=64, null=True),
        ),
    ]