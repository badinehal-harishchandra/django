# Generated by Django 4.0.2 on 2022-03-02 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videorequest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='videotitle',
            field=models.CharField(max_length=30),
        ),
    ]