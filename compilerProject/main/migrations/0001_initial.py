# Generated by Django 2.2.8 on 2022-05-05 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgrammingTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('input_description', models.TextField()),
                ('output_description', models.TextField()),
                ('input_example', models.TextField()),
                ('output_example', models.TextField()),
                ('time_limit', models.IntegerField()),
                ('memory_limit', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_public', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('language', models.IntegerField(choices=[('python', 'Python'), ('java', 'Java'), ('c', 'C'), ('c++', 'C++'), ('javascript', 'JavaScript')], default=0)),
                ('difficulty', models.IntegerField(choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')], default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Programming Task',
                'verbose_name_plural': 'Programming Tasks',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ProgrammingTaskSolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.IntegerField(choices=[('python', 'Python'), ('java', 'Java'), ('c', 'C'), ('c++', 'C++'), ('javascript', 'JavaScript')], default=0)),
                ('code', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_public', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ProgrammingTask')),
            ],
            options={
                'verbose_name': 'Programming Task Solution',
                'verbose_name_plural': 'Programming Task Solutions',
                'ordering': ['-created_at'],
            },
        ),
    ]