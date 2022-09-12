from django.shortcuts import render

# Create your views here.
from vcf_handler.models import Vcf
from vcf_handler.serializers import VcfSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
from rest_framework import permissions
from rest_framework import generics
from django.http import HttpResponseRedirect
import os
from pathlib import Path

# function to handle any vcf file
def parse_vcf(fname, info_cols=None, nrows=None):
    """Parse a VCF file. The INFO column is parsed to a dictionary.

    """
    header = "CHROM POS ID REF ALT QUAL FILTER INFO FORMAT GT".split()
    vcf = pd.read_csv(
        fname, delimiter='\t', comment='#', names=header, nrows=nrows)

    return vcf

# view to read file from the folder inside application named files files
def read_file(request):
    Vcf.objects.all().delete()
    
    
    paths = list(Path(os.path.join(os.path.dirname(__file__)), 'files').glob('**/*.gz'))
    if len(paths) != 0:
        for p in paths:
            
            vcf = parse_vcf(p)
           
            df_records = vcf.to_dict('records')

            model_instances = [Vcf(

                CHROM=record["CHROM"],
                POS=record['POS'],
                ID_seq = record['ID'],
                ALT = record['ALT'],
                REF = record['REF'],
                ) for record in df_records]
            Vcf.objects.bulk_create(model_instances)

    return HttpResponseRedirect('/vcfs/')
  
class VcfList(APIView):
    """
    List all vcf records, and add new records from the file to the database.
    """

    # add authentication permission for defined methods
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # GET method to list all records from the vcf model in the database
    def get(self, request, format=None):
        vcfs = Vcf.objects.all()
        # define serializer to serializer all records
        serializer = VcfSerializer(vcfs, many=True) 
        #return data
        return Response(serializer.data)

    # POST method to create new object in the database model 
    def post(self, request, format=None):
    	# define serializer and get the validation rules
        serializer = VcfSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from vcf_handler.permissions import IsOwnerOrReadOnly
class VcfDetail(APIView):
    """
    Retrieve, update or delete a vcf instance, based on authorization priviledges.
    """
    # add authentication permission for defined methods
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]

    # function to filter from the database for the requested ID. Return row(s) from the VCF that match the id
    def get_object(self, id_seq):
        vcf = Vcf.objects.filter(ID_seq=id_seq)
        if vcf.exists():
        	return vcf
        else:
            raise Http404

    # GET method to return row(s) from the VCF that match the id and return as response the data
    def get(self, request, id_seq, format=None):
        vcf = self.get_object(id_seq)
        serializer = VcfSerializer(vcf, many=True)
        return Response(serializer.data)

    # PUT method to return row(s) from the VCF that match the id, update the specific row(s) and return as response the updated data
    def put(self, request, id_seq, format=None):
        vcf = self.get_object(id_seq)
        for instance in vcf:
        	serializer = VcfSerializer(instance, data=request.data)
        	if serializer.is_valid():
        		serializer.save()
        		return Response(serializer.data)
        	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE method to return row(s) from the VCF that match the id, delete the specific row(s) and return as response no content
    def delete(self, request, id_seq, format=None):
        vcf = self.get_object(id_seq)
        vcf.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
