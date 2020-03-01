# Generated by Django 3.0.3 on 2020-02-27 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fcuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='사용자명')),
                ('password', models.CharField(max_length=64, verbose_name='비밀번호')),
                ('registerd_dttm', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
            ],
            options={
                'db_table': 'fastcampus_fcuser',
            },
        ),
    ]