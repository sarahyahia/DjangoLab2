# Generated by Django 3.1.7 on 2021-03-13 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netflix', '0002_auto_20210313_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='categories',
            field=models.ManyToManyField(to='netflix.Category'),
        ),
    ]
