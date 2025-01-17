# Generated by Django 4.2.5 on 2023-09-20 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('price', models.IntegerField()),
                ('discounted_price', models.IntegerField()),
                ('imgae', models.ImageField(upload_to='media')),
                ('description', models.TextField()),
                ('specification', models.TextField()),
                ('slug', models.TextField()),
                ('stock', models.CharField(choices=[('In Stock', 'In Stock'), ('Out of Stock', 'Out of Stock')], max_length=100)),
                ('labels', models.CharField(choices=[('default', 'default'), ('hot', 'hot'), ('new', 'new'), ('sale', 'sale')], max_length=100)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
    ]
