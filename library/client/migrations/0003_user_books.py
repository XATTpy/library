# Generated by Django 2.2.3 on 2019-07-19 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20190718_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='books',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.Book'),
        ),
    ]
