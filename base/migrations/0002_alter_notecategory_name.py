# Generated by Django 5.1.2 on 2024-11-10 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notecategory',
            name='name',
            field=models.TextField(),
        ),
    ]