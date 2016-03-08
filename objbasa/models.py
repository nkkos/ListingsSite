from django.db import models
from django.utils import timezone

class Listing(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=300)
    address = models.TextField()
    show_address = models.BooleanField()
    price = models.IntegerField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    INDOOR = 'IND'
    OUTDOOR = 'OUTD'
    SPACE_TYPE_CHOICES = (
    (INDOOR, 'Indoor'),
    (OUTDOOR, 'Outdoor'),
    )
    space_type = models.CharField(max_length=7, choices=SPACE_TYPE_CHOICES, default=INDOOR)

    DRAFT = 'DF'
    APPR = 'AP'
    BLOCKED = 'BL'
    LISTING_STATUS_CHOICES = (
    (DRAFT, 'Draft'),
    (APPR, 'Approved'),
    (BLOCKED, 'Blocked'),
    )
    listing_status = models.CharField(max_length=8, choices=LISTING_STATUS_CHOICES, default=DRAFT)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
