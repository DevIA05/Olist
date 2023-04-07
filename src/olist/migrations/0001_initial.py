# Generated by Django 4.1.7 on 2023-04-07 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.AutoField(db_column='city_id', primary_key=True, serialize=False)),
                ('city_name', models.CharField(db_column='city_name', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerIds',
            fields=[
                ('customer_id', models.CharField(db_column='customer', max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.CharField(db_column='order_id', max_length=50, primary_key=True, serialize=False)),
                ('order_status', models.CharField(db_column='order_status', max_length=50)),
                ('order_approved_at', models.DateTimeField(db_column='order_approved_at')),
                ('order_purchase_timestamp', models.DateTimeField(db_column='order_purchase_timestamp')),
                ('order_delivered_carrier_date', models.DateTimeField(db_column='order_delivered_carrier_date')),
                ('order_delivered_customer_date', models.DateTimeField(db_column='order_delivered_customer_date')),
                ('order_estimated_delivery_date', models.DateTimeField(db_column='order_estimated_delivery_date')),
                ('customer_id', models.ForeignKey(db_column='customer_id', on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='olist.customerids')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategoryNameTranslation',
            fields=[
                ('product_category_name', models.CharField(db_column='product_category_name', max_length=50, primary_key=True, serialize=False)),
                ('product_category_name_english', models.CharField(db_column='product_category_name_english', max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('state_code', models.CharField(db_column='state_code', max_length=5, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ZipCode',
            fields=[
                ('zip_code_prefix', models.CharField(db_column='zip_code_prefix', max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('seller_id', models.CharField(db_column='seller_id', max_length=50, primary_key=True, serialize=False)),
                ('zip_code_prefix', models.ForeignKey(db_column='zip_code_prefix', on_delete=django.db.models.deletion.DO_NOTHING, related_name='seller_zip_code', to='olist.zipcode')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.CharField(db_column='product_id', max_length=50, primary_key=True, serialize=False)),
                ('product_name_lenght', models.IntegerField(db_column='product_name_lenght')),
                ('product_description_lenght', models.IntegerField(db_column='product_description_lenght')),
                ('product_photos_qty', models.IntegerField(db_column='product_photos_qty')),
                ('product_weight_g', models.IntegerField(db_column='product_weight_g')),
                ('product_height_cm', models.IntegerField(db_column='product_height_cm')),
                ('product_length_cm', models.IntegerField(db_column='product_length_cm')),
                ('product_width_cm', models.IntegerField(db_column='product_width_cm')),
                ('product_category_name_translation', models.ForeignKey(db_column='product_category_name_translation', on_delete=django.db.models.deletion.DO_NOTHING, related_name='product_category_name_translation', to='olist.productcategorynametranslation')),
            ],
        ),
        migrations.CreateModel(
            name='OrderReview',
            fields=[
                ('review_id', models.CharField(db_column='review_id', max_length=50, primary_key=True, serialize=False)),
                ('review_comment_title', models.CharField(db_column='review_comment_title', max_length=50)),
                ('review_score', models.IntegerField(db_column='review_score')),
                ('review_comment_message', models.TextField(db_column='review_comment_message')),
                ('review_creation_date', models.DateTimeField(db_column='review_creation_date')),
                ('review_answer_timestamp', models.DateTimeField(db_column='review_answer_timestamp')),
                ('order_id', models.ForeignKey(db_column='order_id', on_delete=django.db.models.deletion.CASCADE, related_name='review_order', to='olist.order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderPayment',
            fields=[
                ('payment_id', models.AutoField(db_column='payment_id', primary_key=True, serialize=False)),
                ('payment_sequential', models.IntegerField(db_column='payment_sequential')),
                ('payment_installments', models.IntegerField(db_column='payment_installments')),
                ('payment_value', models.FloatField(db_column='payment_value')),
                ('payment_type', models.CharField(db_column='payment_type', max_length=50)),
                ('order_id', models.ForeignKey(db_column='order_id', on_delete=django.db.models.deletion.CASCADE, related_name='payment_order', to='olist.order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('order_item_id', models.AutoField(db_column='order_item_id', primary_key=True, serialize=False)),
                ('shipping_limit_date', models.DateTimeField(db_column='shipping_limit_date')),
                ('price', models.FloatField(db_column='price')),
                ('freight_value', models.FloatField(db_column='freight_value')),
                ('order_id', models.ForeignKey(db_column='order_id', on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_item_order', to='olist.order')),
                ('product_id', models.ForeignKey(db_column='product_id', on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_item_product', to='olist.product')),
                ('seller_id', models.ForeignKey(db_column='seller_id', on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_item_seller', to='olist.seller')),
            ],
        ),
        migrations.CreateModel(
            name='Geolocation',
            fields=[
                ('geolocation_id', models.AutoField(db_column='geolocation_id', primary_key=True, serialize=False)),
                ('geolocation_lng', models.CharField(db_column='geolocation_lng', max_length=50)),
                ('geolocation_lat', models.CharField(db_column='geolocation_lat', max_length=50)),
                ('city_id', models.ForeignKey(db_column='city_id', on_delete=django.db.models.deletion.DO_NOTHING, related_name='geolocation_city', to='olist.city')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerUnique',
            fields=[
                ('customer_unique_id', models.CharField(db_column='customer_unique_id', max_length=50, primary_key=True, serialize=False)),
                ('zip_code_prefix', models.ForeignKey(db_column='zip_code_prefix', on_delete=django.db.models.deletion.DO_NOTHING, related_name='zip_code', to='olist.zipcode')),
            ],
        ),
        migrations.AddField(
            model_name='customerids',
            name='customer_unique',
            field=models.ForeignKey(db_column='customer_unique', on_delete=django.db.models.deletion.DO_NOTHING, related_name='customer_unique', to='olist.customerunique'),
        ),
        migrations.AddField(
            model_name='city',
            name='state_code',
            field=models.ForeignKey(db_column='state_code', on_delete=django.db.models.deletion.DO_NOTHING, related_name='city_state_code', to='olist.state'),
        ),
        migrations.CreateModel(
            name='CityZipCode',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('city_id', models.ForeignKey(db_column='city_id', on_delete=django.db.models.deletion.DO_NOTHING, related_name='city_zip_code_city', to='olist.city')),
                ('zip_code_prefix', models.ForeignKey(db_column='zip_code_prefix', on_delete=django.db.models.deletion.DO_NOTHING, related_name='city_zip_code_zip_code_prefix', to='olist.zipcode')),
            ],
            options={
                'unique_together': {('city_id', 'zip_code_prefix')},
            },
        ),
    ]
