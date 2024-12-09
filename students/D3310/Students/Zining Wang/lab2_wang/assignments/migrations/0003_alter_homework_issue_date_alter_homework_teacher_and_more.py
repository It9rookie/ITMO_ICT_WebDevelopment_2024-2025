# Generated by Django 5.1.3 on 2024-12-03 23:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0002_remove_homework_penalty_info_remove_subject_teacher_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='issue_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='homework',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignments.teacher'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='grade',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='submitted_at',
            field=models.DateTimeField(),
        ),
    ]
