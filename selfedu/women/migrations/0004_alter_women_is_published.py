# Generated by Django 5.0.1 on 2024-01-31 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0003_women_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='women',
            name='is_published',
            field=models.BooleanField(choices=[(0, 'draft'), (1, 'published')], default=1),
        ),
    ]