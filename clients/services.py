import csv
from clients.models import Client


class ClientService:

    def __init__(self, tablename):
        self.tablename = str(tablename)

    def create_client(self,client):
        with open(self.tablename, mode='a') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=Client.schema())
            writer.writerow(client.to_dict())


    def list_client(self):
        with open(self.tablename, mode='r') as csv_file:
            reader = csv.DictReader(csv_file, fieldnames=Client.schema())
            return list(reader)
    
    def get_client(self,client_uid):
        with open(self.tablename, mode='r') as csv_file:
            reader = csv.DictReader(csv_file, fieldnames=Client.schema())
            for idx, client in enumerate(reader):
                print(idx)
              
    def update_client(self,client):            
        with open(self.tablename, mode='a') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=Client.schema())
            writer.writerow(client.to_dict())
         
    def delete_client():
        
                
