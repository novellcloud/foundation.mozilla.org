# Generated by Django 2.2.17 on 2021-02-10 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buyersguide', '0008_auto_20210126_1943'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buyersguideproductcategory',
            old_name='name_pt',
            new_name='name_pt_BR',
        ),
    ]