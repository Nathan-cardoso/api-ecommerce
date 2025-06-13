from django.db import models

class Promotion(models.Model):
    description = models.CharField(
        max_length=255
    )

    discount = models.FloatField()


class Collection(models.Model):

    title = models.CharField(
        max_length=255
    )

    featured_product = models.ForeignKey(
        'Product',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
    )


class Product(models.Model):
    
    title = models.CharField(
        max_length=255
    ),

    descrpition = models.TextField(),

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    ),

    inventory = models.IntegerField(),

    last_updated = models.DateTimeField(
        auto_now=True
    )

    collection = models.ForeignKey(
        Collection,
        on_delete=models.PROTECT
    )

    promotions = models.ManyToManyField(
        Promotion
    )    



class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = (
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold')
    )

    first_name = models.CharField(
        max_length=255
    )

    last_name = models.CharField(
        max_length=255
    )

    email = models.EmailField(
        unique=True
    )

    phone = models.CharField(
        max_length=20
    )

    birth_date = models.DateTimeField(
        null=True
    )

    membership = models.CharField(
        max_length=1,
        choices=MEMBERSHIP_CHOICES,
        default=MEMBERSHIP_BRONZE
    )



class Address(models.Model):

    street = models.CharField(
        max_length=255
    )

    city = models.CharField(
        max_length=100
    )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
    )


class Order(models.Model):

    PAYMENT_STATUS_PEDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'

    PAYMENT_STATUS_CHOICES = (
        (PAYMENT_STATUS_PEDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    )

    placed_at = models.DateTimeField(
        auto_now_add=True,
    )

    payment_status = models.CharField(
        max_length=1,
        choices=PAYMENT_STATUS_CHOICES,
        default=PAYMENT_STATUS_PEDING
    )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        null=True
    )


class OrderItem(models.Model):

    quantity = models.PositiveSmallIntegerField()

    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        null=True
    )

    Product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT
    )

    unit_price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )


class Cart(models.Model):

    created_at = models.DateTimeField(
        auto_now_add=True
    )



class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE
    )

    Product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE
    )

    quantity = models.PositiveSmallIntegerField()

