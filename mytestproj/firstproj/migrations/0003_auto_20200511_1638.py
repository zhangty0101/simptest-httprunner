# Generated by Django 3.0.4 on 2020-05-11 16:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('firstproj', '0002_auto_20200511_1629'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ApiInfo',
            new_name='Teststep',
        ),
        migrations.RemoveField(
            model_name='testcase',
            name='api',
        ),
        migrations.AddField(
            model_name='testcase',
            name='teststep',
            field=models.ManyToManyField(blank=True, related_name='step_case', to='firstproj.Teststep', verbose_name='关联步骤'),
        ),
    ]