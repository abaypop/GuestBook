# Generated by Django 4.2.11 on 2024-03-07 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guest_book', '0002_bukutamu_tgl_akhir_bukutamu_tgl_awal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bukutamu',
            name='tgl_akhir',
        ),
        migrations.RemoveField(
            model_name='bukutamu',
            name='tgl_awal',
        ),
    ]
