# Generated by Django 4.1.3 on 2022-11-22 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EntregaA', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='nosotros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('informacion', models.CharField(max_length=100)),
                ('fecha', models.IntegerField()),
            ],
        ),
    ]