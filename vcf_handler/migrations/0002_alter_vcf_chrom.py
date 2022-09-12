# Generated by Django 4.1.1 on 2022-09-11 13:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vcf_handler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vcf',
            name='CHROM',
            field=models.CharField(blank=True, max_length=100, validators=[django.core.validators.RegexValidator('^chr(?:[1-9]|[1][0-9]|[[2][0-2]|[XYM])$', 'Invalid CHROM. The proper syntax is prefixed with chr and followed by numbers 1 to 22 or letters X,Y,M.')]),
        ),
    ]
