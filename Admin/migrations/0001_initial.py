# Generated by Django 4.2.1 on 2023-05-19 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name="Product_Sub_Cat",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("product_price", models.CharField(max_length=100)),
                (
                    "product_pic",
                    models.FileField(default="happy.jpg", upload_to="product_pic"),
                ),
                ("product_model", models.CharField(max_length=100)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Admin.product"
                    ),
                ),
            ],
        ),
    ]
