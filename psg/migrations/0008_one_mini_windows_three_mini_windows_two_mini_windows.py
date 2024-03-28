# Generated by Django 4.2.4 on 2024-02-21 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('psg', '0007_iframe'),
    ]

    operations = [
        migrations.CreateModel(
            name='One_mini_windows',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s', serialize=False, to='cms.cmsplugin')),
                ('firstText', models.CharField(max_length=300)),
                ('firstImage', models.ImageField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Three_mini_windows',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s', serialize=False, to='cms.cmsplugin')),
                ('firstText', models.CharField(max_length=300)),
                ('firstImage', models.ImageField(upload_to='')),
                ('secondText', models.CharField(max_length=300)),
                ('secondImage', models.ImageField(upload_to='')),
                ('thirdText', models.CharField(max_length=300)),
                ('thirdImage', models.ImageField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Two_mini_windows',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s', serialize=False, to='cms.cmsplugin')),
                ('firstText', models.CharField(max_length=300)),
                ('firstImage', models.ImageField(upload_to='')),
                ('secondText', models.CharField(max_length=300)),
                ('secondImage', models.ImageField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]