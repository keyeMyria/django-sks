# Generated by Django 2.0.5 on 2018-05-23 03:48

from decimal import Decimal
import django.contrib.postgres.fields.hstore
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seo_title', models.CharField(blank=True, max_length=70, null=True, validators=[django.core.validators.MaxLengthValidator(70)])),
                ('seo_description', models.CharField(blank=True, max_length=300, null=True, validators=[django.core.validators.MaxLengthValidator(300)])),
                ('name', models.CharField(max_length=256)),
                ('handle', models.SlugField(max_length=256)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'permissions': (('view_category', 'Can view categories'), ('edit_category', 'Can edit categories')),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seo_title', models.CharField(blank=True, max_length=70, null=True, validators=[django.core.validators.MaxLengthValidator(70)])),
                ('seo_description', models.CharField(blank=True, max_length=300, null=True, validators=[django.core.validators.MaxLengthValidator(300)])),
                ('body_html', models.TextField(blank=True, verbose_name='description')),
                ('handle', models.CharField(max_length=256, verbose_name='handle')),
                ('published_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('published_scope', models.CharField(choices=[('pos', 'Online shop')], default='pos', max_length=30, verbose_name='visability')),
                ('attributes', django.contrib.postgres.fields.hstore.HStoreField(blank=True, default={})),
            ],
            options={
                'permissions': (('view_product', 'Can view products'), ('edit_product', 'Can edit products')),
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('handle', models.SlugField(max_length=256)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'permissions': (('view_product_type', 'Can view product_types'), ('edit_product_type', 'Can edit product_types')),
            },
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attributes', django.contrib.postgres.fields.hstore.HStoreField(blank=True, default={})),
                ('inventory_management', models.CharField(blank=True, default='blank', max_length=32)),
                ('inventory_policy', models.CharField(blank=True, default='deny', max_length=32)),
                ('quantity', models.IntegerField(default=Decimal('1'), validators=[django.core.validators.MinValueValidator(0)])),
                ('quantity_allocated', models.IntegerField(default=Decimal('0'), validators=[django.core.validators.MinValueValidator(0)])),
                ('option1', models.CharField(blank=True, default='', max_length=256)),
                ('option2', models.CharField(blank=True, default='', max_length=256)),
                ('option3', models.CharField(blank=True, default='', max_length=256)),
                ('position', models.IntegerField(default=1, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sku', models.CharField(blank=True, default='', max_length=256)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='product.Product')),
            ],
            options={
                'ordering': ('position',),
            },
        ),
    ]
