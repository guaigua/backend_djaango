# From Django
from django.db import models
from django.core.validators import RegexValidator

# Utilities
from utils.models import RestorationsModel


class Client(RestorationsModel):

    first_name = models.CharField('first name', max_length=100) # -- required
    last_name = models.CharField('last name', max_length=100) # -- required

    # # Username Field
    # username = serializers.CharField(
    #     min_length=4, 
    #     max_length=30,
    #     validators=[UniqueValidator(queryset=User.objects.all())]
    # )

    email = models.EmailField(
        'email address',
        max_length=30,
        unique=True,
        error_messages={
            'unique': 'A client with that email already exists.'
        }
    )

    birthday = models.DateTimeField(
        'birthday',
        auto_now_add=False,
        auto_now=False,
        null=True,
        help_text='Day the equipment was purchased.')

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A client with that email already exists.'
        }
    ) # -- required

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    
    company = models.ForeignKey('company.Company', on_delete=models.SET_NULL, null=True, blank=False) # -- required
    # Address Fields
    
    address = models.TextField(max_length=250, null=True, blank=True) 
    city = models.CharField('city', max_length=30, null=True, blank=False) # -- required
    state = models.CharField('state', max_length=30, null=True, blank=False) # -- required
    zip_code = models.CharField('zip', max_length=30, null=True, blank=False) # -- required
    country = models.CharField('country', max_length=30, null=True, blank=False) # -- required

    county = models.CharField('county', max_length=30, null=True, blank=True) 
    route = models.CharField('route', max_length=30, null=True, blank=True) 
    street_number = models.CharField('street number', max_length=30, null=True, blank=True) 
    neighborhood = models.CharField('neighborhood', max_length=30, null=True, blank=True) 
    latitude = models.DecimalField('latitude', max_digits=30, decimal_places=20, null=True, blank=True) 
    longitude = models.DecimalField('longitude', max_digits=30, decimal_places=20, null=True, blank=True) 

    

    def __str__(self):
        """Return username."""
        return self.first_name

    def get_short_name(self):
        """Return username."""
        return self.first_name