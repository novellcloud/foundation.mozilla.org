# Generated by Django 2.2.17 on 2020-12-10 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyersguide', '0006_buyersguideproductcategory_og_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyersguideproductcategory',
            name='name_de',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='buyersguideproductcategory',
            name='name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='buyersguideproductcategory',
            name='name_es',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='buyersguideproductcategory',
            name='name_fr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='buyersguideproductcategory',
            name='name_fy_NL',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='buyersguideproductcategory',
            name='name_nl',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='buyersguideproductcategory',
            name='name_pl',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='buyersguideproductcategory',
            name='name_pt',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='productprivacypolicylink',
            name='label_de',
            field=models.CharField(help_text='Label for this link on the product page', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='productprivacypolicylink',
            name='label_en',
            field=models.CharField(help_text='Label for this link on the product page', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='productprivacypolicylink',
            name='label_es',
            field=models.CharField(help_text='Label for this link on the product page', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='productprivacypolicylink',
            name='label_fr',
            field=models.CharField(help_text='Label for this link on the product page', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='productprivacypolicylink',
            name='label_fy_NL',
            field=models.CharField(help_text='Label for this link on the product page', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='productprivacypolicylink',
            name='label_nl',
            field=models.CharField(help_text='Label for this link on the product page', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='productprivacypolicylink',
            name='label_pl',
            field=models.CharField(help_text='Label for this link on the product page', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='productprivacypolicylink',
            name='label_pt',
            field=models.CharField(help_text='Label for this link on the product page', max_length=500, null=True),
        ),
    ]