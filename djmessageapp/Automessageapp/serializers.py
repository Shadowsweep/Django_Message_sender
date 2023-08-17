from rest_framework import serializers 
from Automessageapp.models import Customers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields =  ('id','policyno','customername','lastdate','hourtime','mintime','contactno')
