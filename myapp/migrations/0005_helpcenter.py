# Generated by Django 3.2.3 on 2021-05-16 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myapp', '0004_delete_helpcenter'),
    ]

    operations = [
        migrations.CreateModel(
            name='HelpCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('query', models.CharField(choices=[('Regarding Tips and Suggestions', 'Regarding Tips and Suggestions'), ('Regarding Transaction Alerts', 'Regarding Transaction Alerts'), ('Regarding Profile Updation', 'Regarding Profile Updation'), ('Other than above', 'Other than above')], max_length=100)),
                ('problem', models.TextField()),
            ],
        ),
    ]
