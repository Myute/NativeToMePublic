# Generated by Django 3.0.4 on 2020-05-05 20:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tribes', '0002_auto_20200505_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joinrequest',
            name='requestingUser',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='joinrequest',
            name='tribeIDToJoin',
        ),
        migrations.AddField(
            model_name='joinrequest',
            name='tribeIDToJoin',
            field=models.ManyToManyField(to='tribes.Tribe'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='postID',
            field=models.IntegerField(default=78, primary_key=True, serialize=False),
        ),
    ]
