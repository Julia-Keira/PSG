# Generated by Django 4.2.4 on 2024-02-06 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('psg', '0006_page_header'),
    ]

    operations = [
        migrations.CreateModel(
            name='Iframe',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s', serialize=False, to='cms.cmsplugin')),
                ('src', models.CharField(max_length=9999)),
                ('width', models.CharField(max_length=5)),
                ('height', models.CharField(max_length=5)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]