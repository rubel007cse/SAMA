# Generated by Django 2.0.1 on 2018-11-27 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainx', '0003_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
