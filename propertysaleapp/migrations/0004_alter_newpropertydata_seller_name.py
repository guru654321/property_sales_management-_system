# Generated by Django 4.2.7 on 2024-01-19 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propertysaleapp', '0003_newstatusdata_delete_addstatusdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpropertydata',
            name='seller_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
