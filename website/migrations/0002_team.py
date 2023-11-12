# Generated by Django 4.2.5 on 2023-11-03 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('team_member_count', models.PositiveIntegerField()),
                ('team_member_names', models.JSONField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('project_name', models.CharField(max_length=255)),
                ('project_link', models.URLField()),
            ],
        ),
    ]
