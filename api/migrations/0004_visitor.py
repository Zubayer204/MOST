# Generated by Django 3.2.4 on 2021-07-07 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_delete_visitor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(blank=True, null=True)),
                ('user_agent', models.TextField(blank=True, null=True)),
                ('pages_visited', models.TextField(blank=True, null=True)),
                ('referer', models.URLField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True)),
                ('longitude', models.FloatField(blank=True)),
                ('visiting_time', models.DateTimeField(auto_now_add=True)),
                ('last_visited', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
