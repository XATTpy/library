# Generated by Django 2.2.3 on 2019-07-19 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_remove_user_books'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='reader',
        ),
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to='client.User'),
        ),
    ]
