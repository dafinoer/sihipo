# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-09-30 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sihipo_root', '0010_auto_20180908_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantoptdetail',
            name='kode',
            field=models.CharField(choices=[(None, 'N/A'), ('PH', 'Keasaman'), ('EC', 'Konduktifitas'), ('HT', 'Kelembapan'), ('TW', 'Suhu Air'), ('TA', 'Suhu Udara'), ('LW', 'Level Air'), ('BL', 'Level Baterai'), ('PA', 'Usia Tanam')], max_length=3, verbose_name='Kode'),
        ),
        migrations.AlterField(
            model_name='plantsensordetail',
            name='kode',
            field=models.CharField(choices=[(None, 'N/A'), ('PH', 'Keasaman'), ('EC', 'Konduktifitas'), ('HT', 'Kelembapan'), ('TW', 'Suhu Air'), ('TA', 'Suhu Udara'), ('LW', 'Level Air'), ('BL', 'Level Baterai'), ('PA', 'Usia Tanam')], max_length=3, verbose_name='Kode'),
        ),
        migrations.AlterField(
            model_name='plantsensorlogdetail',
            name='kode',
            field=models.CharField(choices=[(None, 'N/A'), ('PH', 'Keasaman'), ('EC', 'Konduktifitas'), ('HT', 'Kelembapan'), ('TW', 'Suhu Air'), ('TA', 'Suhu Udara'), ('LW', 'Level Air'), ('BL', 'Level Baterai'), ('PA', 'Usia Tanam')], max_length=3, verbose_name='Kode'),
        ),
    ]