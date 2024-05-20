from datetime import datetime
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from cloudinary.models import CloudinaryField
import random


class Category(models.Model):
    """ A model to represent a category of products"""
    name = models.CharField(
        max_length=255,
        unique=True,
        null=True,
        blank=True,
        verbose_name='Category Name'
    )
    friendly_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    
    class Meta:
        # Set the verbose name and verbose name plural
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        # Return the name of the category
        return self.name

    def get_friendly_name(self):
        # Return the friendly name of the category
        return self.friendly_name
    

class Tag(models.Model):
    """ A model to represent a tag for a product"""
    name = models.CharField(
        max_length=255,
        unique=True,
        null=True,
        blank=True,
        verbose_name='Tag Name'
    )
    friendly_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    
    class Meta:
        # Set the verbose name and verbose name plural
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['name']

    def __str__(self):
        # Return the name of the tag
        return self.name

    
    def get_friendly_name(self):
        # Return the friendly name of the tag
        return self.friendly_name
    

class Product(models.Model):

    class PlayTime(models.IntegerChoices):
        """ A model to represent the play time of a product"""
        MINI = 15, 'Mini'
        SHORT = 30, 'Short'
        MEDIUM = 60, 'Medium'
        LONG = 120, 'Long'
        EPIC = 240, 'Epic'
        LEGENDARY = 480, 'Legendary'

    class Difficulty(models.IntegerChoices):
        """ A model to represent the difficulty of a product"""
        EASY = 1, 'Easy'
        MEDIUM = 2, 'Medium'
        HARD = 3, 'Hard'
        EXPERT = 4, 'Expert'
        MASTER = 5, 'Master'

    """ A model to represent a product"""
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    tags = models.ManyToManyField(
        'Tag',
        blank=True,
        verbose_name='Tags',
        related_name='products',
        help_text= 'Hold "Crtl" while clicking select multiple tags'
    )
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=True,
        verbose_name='Product Name'
    )
    sku = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        unique=True,
        verbose_name='SKU',
        help_text='Stock Keeping Unit, generated automatically'
    )
    year = models.IntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.now().year)
        ],
        null=True,
        blank=True,
        verbose_name='Year Released',
        help_text='Year the product was released, e.g. 2024'
    )
    description = models.TextField(
        max_length=2048,
        null=False,
        blank=False,
        verbose_name='Description'
    )
    min_players = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10),
        ],
        null=True,
        blank=True,
        verbose_name='Minimum Players'
    )
    max_players = models.IntegerField(
        validators=[
            MinValueValidator(2),
            MaxValueValidator(24),
        ],
        null=True,
        blank=True,
        verbose_name='Maximum Players'
    )
    min_age = models.IntegerField(
        validators=[
            MinValueValidator(2),
            MaxValueValidator(99),
        ],
        null=True,
        blank=True,
        verbose_name='Minimum Age'
    )
    play_time = models.IntegerField(
        choices=PlayTime.choices,
        null=True,
        blank=True,
        verbose_name='Play Time',
        default=PlayTime.SHORT,
    )
    publisher = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Publisher'
    )
    has_dimensions = models.BooleanField(
        default=False,
        verbose_name='Has Dimensions'
    )
    has_amount = models.BooleanField(
        default=False,
        verbose_name='Has Amount'
    )
    height = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Height',
        help_text='Height in mm'
    )
    amount = models.IntegerField(
        validators=[
            MinValueValidator(2),
            MaxValueValidator(100),
        ],
        null=True,
        blank=True,
        verbose_name='Amount',
        help_text='For number of pcs in a set'
    )
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Rating'
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
        verbose_name='Price'
    )
    difficulty = models.IntegerField(
        choices=Difficulty.choices,
        null=True,
        blank=True,
        verbose_name='Difficulty',
        default=Difficulty.MEDIUM
    )
    is_featured = models.BooleanField(
        default=False,
        verbose_name='Is Featured',
        help_text='This will add styling to highlight the product on the page'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Is Active'
    )

    class Meta:
        # Set the verbose name and verbose name plural
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']

    def __str__(self):
        # Return the name of the product
        return self.name
    
    def generate_sku(self):
        # Generate a SKU for the product
        self.sku = f'{self.name[:3].upper()}-{random.randint(1000, 9999)}'

    def save(self, *args, **kwargs):
        # If the SKU is not set, generate one
        if not self.sku:
            self.generate_sku()
        # Call the save method of the parent class
        super().save(*args, **kwargs)

    def get_rating(self):
        # Return the rating of the product
        return self.rating
    
    def get_price(self):
        # Return the price of the product
        return self.price
    
    def get_all_images(self):
        # Return all images of the product
        images = ProductImage.objects.filter(product=self)
        if images:
            return images
        return False
    
    def get_main_image(self):
        # The get_main_image method returns the main image of the product.
        images = ProductImage.objects.filter(product=self)
        if images:
            for image in images:
                if image.is_default:
                    return image
                else:
                    default_image = images[0]
                    return default_image
        return False
    

class ProductImage(models.Model):
    """ A model to represent an image of a product"""
    product = models.ForeignKey(
        'Product',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='images'
    )
    image = CloudinaryField(
        'product_images',
        folder='dungeon_dwellers_products',
        null=True,
        blank=True,
        eager=[
            {'width': '50', 'height': '50', 'crop':'crop'}
        ],
        transformation={
            'width': '500', 'height': '500', 'crop':'fill' 
        }
    )
    is_default = models.BooleanField(
        verbose_name='Is Default',
        default=False,
    )

    class Meta:
        # Set the verbose name and verbose name plural
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'
        ordering = ['product']

    def __str__(self):
        # Return the name of the product
        return self.product.name
    
    def get_image(self):
        # Return the image of the product
        return self.image

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return False
