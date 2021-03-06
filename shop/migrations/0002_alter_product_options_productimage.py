# Generated by Django 4.0.1 on 2022-01-29 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created']},
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='products/%Y/%m/%d/None')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
    ]
