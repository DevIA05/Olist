from django.db import models

class ZipCode(models.Model):
    zip_code_prefix = models.CharField(db_column='zip_code_prefix', primary_key=True, max_length=50)

class State(models.Model):
    state_code = models.CharField(db_column='state_code', max_length=5, primary_key=True)

class City(models.Model):
    city_id = models.AutoField(primary_key=True, db_column='city_id')
    city_name = models.CharField(db_column='city_name', max_length=50)
    state_code = models.ForeignKey(State, on_delete=models.DO_NOTHING, db_column='state_code', related_name='city_state_code')

class CityZipCode(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    city_id = models.ForeignKey(City, on_delete=models.DO_NOTHING, db_column='city_id', related_name='city_zip_code_city')
    zip_code_prefix = models.ForeignKey(ZipCode, on_delete=models.DO_NOTHING, db_column='zip_code_prefix', related_name='city_zip_code_zip_code_prefix')
    
    class Meta:
        unique_together = ('city_id', 'zip_code_prefix')

class Geolocation(models.Model):
    geolocation_id = models.AutoField(primary_key=True, db_column='geolocation_id')
    geolocation_lng = models.CharField(db_column='geolocation_lng', max_length=50)
    geolocation_lat = models.CharField(db_column='geolocation_lat', max_length=50)
    city_id = models.ForeignKey(City, on_delete=models.DO_NOTHING, db_column='city_id', related_name='geolocation_city')


class CustomerUnique(models.Model):
    customer_unique_id = models.CharField(db_column='customer_unique_id', primary_key=True, max_length=50)
    zip_code_prefix = models.ForeignKey(ZipCode, on_delete=models.DO_NOTHING, db_column='zip_code_prefix', related_name='zip_code')

class CustomerIds(models.Model):
    customer_id = models.CharField(db_column='customer', max_length=50, primary_key=True)
    customer_unique = models.ForeignKey(CustomerUnique, on_delete=models.DO_NOTHING, db_column='customer_unique', related_name='customer_unique')

class Order(models.Model):
    order_id = models.CharField(max_length=50, primary_key=True, db_column='order_id')
    order_status = models.CharField(db_column='order_status', max_length=50)
    order_approved_at = models.DateTimeField(db_column='order_approved_at')
    order_purchase_timestamp = models.DateTimeField(db_column='order_purchase_timestamp')
    order_delivered_carrier_date = models.DateTimeField(db_column='order_delivered_carrier_date')
    order_delivered_customer_date = models.DateTimeField(db_column='order_delivered_customer_date')
    order_estimated_delivery_date = models.DateTimeField(db_column='order_estimated_delivery_date')
    customer_id = models.ForeignKey(CustomerIds, on_delete=models.CASCADE, db_column='customer_id', related_name='customer')

class OrderPayment(models.Model):
    payment_id = models.AutoField(primary_key=True, db_column='payment_id')
    payment_sequential = models.IntegerField(db_column='payment_sequential')
    payment_installments = models.IntegerField(db_column='payment_installments')
    payment_value = models.FloatField(db_column='payment_value')
    payment_type = models.CharField(db_column='payment_type', max_length=50)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, db_column='order_id', related_name='payment_order')

class OrderReview(models.Model):
    review_id = models.CharField(max_length=50, primary_key=True, db_column='review_id')
    review_comment_title = models.CharField(max_length=50, db_column='review_comment_title')
    review_score = models.IntegerField(db_column='review_score')
    review_comment_message = models.TextField(db_column='review_comment_message')
    review_creation_date = models.DateTimeField(db_column='review_creation_date')
    review_answer_timestamp = models.DateTimeField(db_column='review_answer_timestamp')
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, db_column='order_id', related_name='review_order')

class ProductCategoryNameTranslation(models.Model):
    product_category_name = models.CharField(max_length=50, primary_key=True, db_column='product_category_name')
    product_category_name_english = models.CharField(max_length=50, db_column='product_category_name_english', unique=True)

class Product(models.Model):
    product_id = models.CharField(max_length=50, primary_key=True, db_column='product_id')
    product_name_lenght = models.IntegerField(db_column='product_name_lenght')
    product_description_lenght = models.IntegerField(db_column='product_description_lenght')
    product_photos_qty = models.IntegerField(db_column='product_photos_qty')
    product_weight_g = models.IntegerField(db_column='product_weight_g')
    product_height_cm = models.IntegerField(db_column='product_height_cm')
    product_length_cm = models.IntegerField(db_column='product_length_cm')
    product_width_cm = models.IntegerField(db_column='product_width_cm')
    product_category_name_translation = models.ForeignKey(ProductCategoryNameTranslation, on_delete=models.DO_NOTHING, db_column='product_category_name_translation', related_name='product_category_name_translation')

class Seller(models.Model):
    seller_id = models.CharField(max_length=50, primary_key=True, db_column='seller_id')
    zip_code_prefix = models.ForeignKey(ZipCode, on_delete=models.DO_NOTHING, db_column='zip_code_prefix', related_name='seller_zip_code')


class OrderItems(models.Model):
    order_item_id = models.AutoField(primary_key=True, db_column='order_item_id')
    shipping_limit_date = models.DateTimeField(db_column='shipping_limit_date')
    price = models.FloatField(db_column='price')
    freight_value = models.FloatField(db_column='freight_value')
    order_id = models.ForeignKey(Order, on_delete=models.DO_NOTHING, db_column='order_id', related_name='order_item_order')
    product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING, db_column='product_id', related_name='order_item_product')
    seller_id = models.ForeignKey(Seller, on_delete=models.DO_NOTHING, db_column='seller_id', related_name='order_item_seller')

