# Generated by Django 4.1.7 on 2023-03-13 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bike", "0003_alter_customer_city_alter_customer_country"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="phone_number",
            field=models.CharField(max_length=50),
        ),
    ]
