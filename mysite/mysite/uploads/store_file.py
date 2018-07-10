from azure.storage.blob import BlockBlobService, PublicAccess
import os

def store_file_to_azure(path):
    block_blob_service = BlockBlobService(account_name='talentanalyticsbreca', account_key='uFL0cFPtayFJcSnp3QKsFz6uOSInPXqAx/K/Tsch87Vqfqj4SsPiQAg1iNT1snKTZGRPYtexM4uOI3dxkFqf2A==')
    block_blob_service.create_blob_from_path('talentobreca', path, path)
    os.remove(path)
