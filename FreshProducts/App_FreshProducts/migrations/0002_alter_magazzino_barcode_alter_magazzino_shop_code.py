# Generated by Django 4.0.2 on 2022-05-02 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_FreshProducts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magazzino',
            name='Barcode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_FreshProducts.prodotto'),
        ),
        migrations.AlterField(
            model_name='magazzino',
            name='Shop_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_FreshProducts.punto_vendita'),
        ),
    ]
