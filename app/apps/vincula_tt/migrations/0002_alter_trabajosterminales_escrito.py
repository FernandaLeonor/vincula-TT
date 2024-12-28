# Generated by Django 5.1.4 on 2024-12-24 01:53

import apps.vincula_tt.validation
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vincula_tt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajosterminales',
            name='escrito',
            field=models.FileField(upload_to='archivos/', validators=[apps.vincula_tt.validation.validate_file_size]),
        ),
    ]