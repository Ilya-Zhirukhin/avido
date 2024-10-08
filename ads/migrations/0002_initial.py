# Generated by Django 4.2.15 on 2024-08-23 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("locations", "0001_initial"),
        ("categories", "0001_initial"),
        ("ads", "0001_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="admoderation",
            name="moderator",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="users.user"
            ),
        ),
        migrations.AddField(
            model_name="ad",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="categories.category"
            ),
        ),
        migrations.AddField(
            model_name="ad",
            name="city",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="locations.city"
            ),
        ),
        migrations.AddField(
            model_name="ad",
            name="seller",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="users.user"
            ),
        ),
    ]
