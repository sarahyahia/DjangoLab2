# Generated by Django 3.1.7 on 2021-03-19 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netflix', '0007_auto_20210313_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='movies/posters'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='movies/videos'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.DateField(blank=True, null=True),
        ),
    ]
