from django.urls import reverse  
from vcf_handler.models import Vcf
from vcf_handler.serializers import VcfSerializer
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import force_authenticate
from django.contrib.auth.models import User
from django.shortcuts import resolve_url
import json
from rest_framework.test import APITestCase,APIRequestFactory
from rest_framework.test import force_authenticate

class GetAllMethodsVcfTest(APITestCase):

  # Set up new test records
    def setUp(self):
        self.rs123 = Vcf.objects.create(
            CHROM='chr1', POS=1000, ALT='A', REF='G', ID_seq='rs123')
        self.rs1233 = Vcf.objects.create(
            CHROM='chr1', POS=1000, ALT='A', REF='G', ID_seq='rs123')
        self.rs123_update = Vcf.objects.create(
            CHROM='chr1', POS=1001, ALT='A', REF='G', ID_seq='rs123')

     # get API response for specific record(s)
    def test_get_vcfs(self):
        client = APIClient()
        response = client.get(
            reverse('vcf-detail', kwargs={'id_seq': self.rs123.ID_seq}))
        # get data from db
        vcfs = Vcf.objects.filter(ID_seq='rs123')
        serializer = VcfSerializer(vcfs, many=True)
        self.assertEqual(response.data, serializer.data)
    
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    ## return 404 not found for 
    def test_no_get_vcfs(self):
        client = APIClient()
        response = client.get(
            reverse('vcf-detail', kwargs={'id_seq': "rs3241"}))
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # Return 403 no authentcation 
    def test_should_not_create_vcf_with_no_auth(self):
        
        sample_vcf = {"CHROM": "chr1", "POS": 1000, "ALT": "A", "REF": "G", "ID": "rs123"}
        response = self.client.post(reverse('vcfs'), sample_vcf)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # Post method for successfully create record
    def test_should_create_vcf(self):

        user = User.objects.create_user('username', 'Pas$w0rd')
        self.client.force_authenticate(user)
        response = self.client.get('/api-auth/login/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        sample_vcf = {"CHROM": "chr1", "POS": 1000, "ALT": "A", "REF": "G", "ID": "rs123"}
        response = self.client.post(reverse('vcfs'), sample_vcf)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Return 400 for post with validation errors
    def test_should_not_create_vcf_validation_errors(self):

        user = User.objects.create_user('username', 'Pas$w0rd')
        self.client.force_authenticate(user)
        response = self.client.get('/api-auth/login/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        sample_vcf = {"CHROM": "chr1", "POS": 1000, "ALT": "A", "REF": "G", "ID": "r123"}
        response = self.client.post(reverse('vcfs'), sample_vcf)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Put method for successfully put record
    def test_valid_put_vcf(self):
        user = User.objects.create_user('username', 'Pas$w0rd')
        self.client.force_authenticate(user)
        response = self.client.get('/api-auth/login/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.put(
            reverse('vcf-detail', kwargs={'id_seq': self.rs123.ID_seq}),
            data={"CHROM": "chr1", "POS": 1001, "ALT": "A", "REF": "G","ID": "rs123"}
        )
     
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Return 404 not found for invalid id 
    def test_invalid_put_vcf(self):
        user = User.objects.create_user('username', 'Pas$w0rd')
        self.client.force_authenticate(user)
        response = self.client.get('/api-auth/login/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.put(
            reverse('vcf-detail', kwargs={'id_seq': 'rs243'}),
            data={"CHROM": "chr1", "POS": 1001, "ALT": "A", "REF": "G","ID": "rs123"}
        )
     
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # Delete method for successfully delete record
    def test_valid_delete_vcf(self):
        user = User.objects.create_user('username', 'Pas$w0rd')
        self.client.force_authenticate(user)
        response = self.client.get('/api-auth/login/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.delete(
            reverse('vcf-detail', kwargs={'id_seq': self.rs123.ID_seq}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

     # Return 404 not found for invalid id 
    def test_invalid_delete_vcf(self):
        user = User.objects.create_user('username', 'Pas$w0rd')
        self.client.force_authenticate(user)
        response = self.client.get('/api-auth/login/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.delete(
            reverse('vcf-detail',kwargs={'id_seq': "rs3241"}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)




