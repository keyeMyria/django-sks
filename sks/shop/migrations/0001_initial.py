# Generated by Django 2.0.5 on 2018-05-23 03:48

from django.conf import settings
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0003_set_site_domain_and_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seo_title', models.CharField(blank=True, max_length=70, null=True, validators=[django.core.validators.MaxLengthValidator(70)])),
                ('seo_description', models.CharField(blank=True, max_length=300, null=True, validators=[django.core.validators.MaxLengthValidator(300)])),
                ('name', models.CharField(db_index=True, max_length=256, verbose_name='name')),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='settings', to='sites.Site')),
            ],
            options={
                'permissions': (('edit_shop', 'Can edit staff'), ('view_shop', 'Can view staff')),
            },
        ),
        migrations.CreateModel(
            name='ShopStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(null=True, verbose_name='created at')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_owner', models.BooleanField(default=False)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop_staff', to='shop.Shop')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop_staff', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('edit_staff', 'Can edit staff'), ('view_staff', 'Can view staff')),
            },
        ),
        migrations.AddField(
            model_name='shop',
            name='staff',
            field=models.ManyToManyField(through='shop.ShopStaff', to=settings.AUTH_USER_MODEL),
        ),
    ]
