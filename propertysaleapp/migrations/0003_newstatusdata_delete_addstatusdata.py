# Generated by Django 4.2.7 on 2024-01-19 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propertysaleapp', '0002_addstatusdata_newpropertytypedata_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewstatusData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=100)),
                ('status_description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='AddStatusData',
        ),
    ]
