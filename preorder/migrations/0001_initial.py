# Generated by Django 3.2.12 on 2022-06-14 07:20

import django.contrib.postgres.indexes
from django.db import migrations, models
import django.db.models.deletion
import saleor.core.utils.json_serializer


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0117_auto_20220613_0240'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private_metadata', models.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('metadata', models.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('requested_shipment_date', models.DateField()),
                ('order', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pre_order', to='order.order')),
            ],
            options={
                'ordering': ('requested_shipment_date',),
                'abstract': False,
            },
        ),
        migrations.AddIndex(
            model_name='preorder',
            index=django.contrib.postgres.indexes.GinIndex(fields=['private_metadata'], name='preorder_p_meta_idx'),
        ),
        migrations.AddIndex(
            model_name='preorder',
            index=django.contrib.postgres.indexes.GinIndex(fields=['metadata'], name='preorder_meta_idx'),
        ),
    ]
