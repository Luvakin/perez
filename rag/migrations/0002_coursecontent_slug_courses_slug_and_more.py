# Generated by Django 5.2.3 on 2025-07-02 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rag', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursecontent',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AddField(
            model_name='courses',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AlterField(
            model_name='coursecontent',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
