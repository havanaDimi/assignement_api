from rest_framework import serializers
from vcf_handler.models import Vcf, SEQ_CHOICES

# Define serializer for the vcf model
class VcfSerializer(serializers.ModelSerializer):
    ID = serializers.RegexField(regex=r'^rs[1-9]\d*$', source='ID_seq') # add validation rule to the ID field
  
    class Meta:
        model = Vcf
        fields = ['CHROM', 'POS', 'ALT', 'REF', 'ID']
        depth = 1
