# Generated by Django 4.2.3 on 2023-07-12 16:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("supercats", "0002_cat_upload"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cat",
            name="upload",
            field=models.ImageField(upload_to="media/"),
        ),
    ]