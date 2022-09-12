from django.db import models
from django.core.validators import RegexValidator

# List of sequences choices
SEQ_CHOICES =  (
    ("A", "A"),
    ('G', "G"),
    ('C', "C"),
    ('T', "T"),
    ('.', "."),
)

# Define validator for  CHROM field to accept specific patterns of inputs
ChromValidator = RegexValidator(regex=r'^chr(?:[1-9]|1[0-9]|2[0-2]|[XYM])$', message='Invalid CHROM. The proper syntax is prefixed with chr and followed by numbers 1 to 22 or letters X,Y,M.')

# Define Vcf model class with the interested fields
class Vcf(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    CHROM = models.CharField(max_length=100, blank=True,validators=[ChromValidator]) # add chrom validation rule
    POS = models.IntegerField(blank=True, null=True)
    ID_seq = models.CharField(max_length=100,  verbose_name=u"ID", blank=True) # change display name
    ALT = models.CharField(choices=SEQ_CHOICES, blank=True,  max_length=100) # add sequences choices list
    REF = models.CharField(choices=SEQ_CHOICES, blank=True,  max_length=100) # add sequences choices list
   
    # save method
    def save(self, *args, **kwargs):
	    
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['created']
    