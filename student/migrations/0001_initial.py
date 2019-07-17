# Generated by Django 2.2.3 on 2019-07-16 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacher', '0017_auto_20190716_0325'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.IntegerField()),
                ('class_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.ClassRegistration')),
            ],
        ),
    ]