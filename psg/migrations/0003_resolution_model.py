# Generated by Django 4.2.4 on 2023-09-07 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('psg', '0002_rename_window_model_main_page_window_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resolution_model',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s', serialize=False, to='cms.cmsplugin')),
                ('title', models.CharField(max_length=9999)),
                ('description', models.CharField(max_length=9999)),
                ('resolution', models.FileField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
