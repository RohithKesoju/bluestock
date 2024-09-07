# serializers.py
from rest_framework import serializers
from .models import Ipoinfo

class IPOSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ipoinfo
        fields = ['id', 'company', 'price_band', 'open', 'close',
                  'issue_size', 'issue_type', 'listing_date', 'status',
                  'ipo_price', 'listing_price', 'listing_gain', 'cmp', 'current_return']
