from vcf_handler.models import Vcf
from vcf_handler.serializers import VcfSerializer
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

class GetAllVcfTest(APITestCase):

    # GET list of all vcf records in the database
    def test_get_all_vcfs(self):
        # get API response
        client = APIClient()
        response = client.get('/vcfs/')
        # get data from db
        vcfs = Vcf.objects.all()
        serializer = VcfSerializer(vcfs, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # GET list of all vcf records in the database and accept an ACCEPT HTTP header json
    def test_get_all_vcfs_json(self):
        # get API response
        client = APIClient()
        response = client.get('/vcfs/', HTTP_ACCEPT='application/json') 
        # get data from db
        vcfs = Vcf.objects.all()
        serializer = VcfSerializer(vcfs, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # GET list of all vcf records in the database and accept an ACCEPT HTTP header xml
    def test_get_all_vcfs_xml(self):
        # get API response
        client = APIClient()
        response = client.get('/vcfs/', HTTP_ACCEPT='application/xml') 
        # get data from db
        vcfs = Vcf.objects.all()
        serializer = VcfSerializer(vcfs, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Return 406 not accepted an ACCEPT HTTP header xml
    def test_get_all_vcfs_not_accepted_header(self):
        # get API response
        client = APIClient()
        response = client.get('/vcfs/', HTTP_ACCEPT='application/xdml')         
        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)