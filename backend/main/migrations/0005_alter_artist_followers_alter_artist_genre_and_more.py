# Generated by Django 4.2.7 on 2025-04-29 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_admin_options_alter_artist_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='followers',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='genre',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='concertowner',
            name='adress',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='concertowner',
            name='capacity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
