from django.db import models

# Create your models here.

class Ipoinfo(models.Model):
    STATUS = (
        ('Ongoing', 'Ongoing'),
        ('Coming', 'Coming'),
        ('New Listed', 'New Listed'),
    )
    #id = models.PositiveBigIntegerField(primary_key=True)
    company = models.CharField(max_length=50)
    price_band = models.CharField(max_length=100)
    open = models.DateField()
    close = models.DateField()
    issue_size = models.IntegerField()
    issue_type = models.CharField(max_length=50, null=True)
    listing_date = models.DateField()
    #status = models.IntegerField()
    status = models.CharField(max_length=50, choices=STATUS, default='Ongoing')
    ipo_price = models.CharField(max_length=100)
    listing_price = models.CharField(max_length=100)
    listing_gain = models.CharField(max_length=100)
    cmp = models.CharField(max_length=100)
    current_return = models.CharField(max_length=100)
    rhp = models.CharField(max_length=100)
    drhp = models.CharField(max_length=100)
    action = models.BinaryField()
    #delete
    def __str__(self):
        return self.company
