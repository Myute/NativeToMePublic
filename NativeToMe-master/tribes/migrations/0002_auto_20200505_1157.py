# Generated by Django 3.0.4 on 2020-05-05 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tribes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='postID',
            field=models.IntegerField(default=953, primary_key=True, serialize=False),
        ),
    ]
