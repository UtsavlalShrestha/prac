# Generated by Django 5.1.2 on 2024-11-10 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_notecategory_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notecategory',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
