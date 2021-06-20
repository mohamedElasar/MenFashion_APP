# Generated by Django 3.2.4 on 2021-06-19 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Adv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('image_url', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=400)),
                ('image_url', models.ImageField(null=True, upload_to='')),
                ('description', models.TextField(max_length=400)),
                ('categories', models.ManyToManyField(to='ShopsApp.Category')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='shop_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShopItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('price', models.FloatField(blank=True, null=True)),
                ('description', models.TextField(max_length=255)),
                ('image_url', models.ImageField(upload_to='')),
                ('category_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ShopsApp.category')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='ShopsApp.shop')),
            ],
        ),
        migrations.CreateModel(
            name='FavItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shops', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_fav', to='ShopsApp.shop')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]