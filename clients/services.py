import csv
import os
from clients.models import Client


class ClientService:

    def __init__(self, tablename):
        self.tablename = str(tablename)

    def create_client(self, client):
        with open(self.tablename, mode='a') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=Client.schema())
            writer.writerow(client.to_dict())

    def list_client(self):
        with open(self.tablename, mode='r') as csv_file:
            reader = csv.DictReader(csv_file, fieldnames=Client.schema())
            return list(reader)

    def _savefile(self, clients):
        tmp_table_data = "{}.tmp".format(self.tablename)
        with open(tmp_table_data, mode='w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=Client.schema())
            writer.writerows(clients)
            os.remove(self.tablename)
            os.rename(tmp_table_data, self.tablename)

    def update_client(self, update_client):
        clients = self.list_client()
        update_clients = []
        for client in clients:
            if client["uid"] == update_client.uid:
                update_clients.append(update_client.to_dict())
            else:
                update_clients.append(client)
        self._savefile(update_clients)

    def delete_client(self, deleted_client):
        clients=self.list_client()
        new_clients = []
        for client in clients:
            if client["uid"] == deleted_client:
                pass
            else:
                new_clients.append(client)
        self._savefile(new_clients)
        
