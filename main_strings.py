import os
clients = 'Pablo,Ricardo,'

def create_client(client_name):
    global clients
    if client_name not in clients:
        clients += _add_comma(client_name.capitalize())
    else:
        return False    
    return clients


def update_client(client_name,client_new_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name.capitalize()+',', client_new_name.capitalize()+',')
    else:
        return False    
    return clients


def delete_client(client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name.capitalize()+',', '')
    else:
        return False    
    return clients    

def _print_clients():
    global clients
    print(clients)


def _add_comma(str):
    str += ","
    return str


def _print_welcome():
    print("WELCOME PAPS")
    print('*'*50)
    print("[C]reate client")
    print("[L]ist clients")
    print("[D]elete client") 
    print("[U]pdate client") 
    print("[E]nd") 


def _print(type):
    if type == "C":
        print("type client to add") 
    elif type == "D":
        print("type client to delete") 
    elif type == "L":
        print("list of clients")    
    elif type == "U":
        print("type client to update") 
    elif type == "E":
        print("eso esto eso es to esoestodo amigos") 
    elif type == "UA":
        print("type new client to update") 
    else:
        print("opcion invalida") 


if __name__ == '__main__':
    command=""
    while (command != "E"):
        os.system('clear') 
        _print_welcome()
        command = input()
        command = command.upper()
        _print(command)
        if command == 'C':
            nclient = input()
            if not create_client(nclient):
                print ("ya existe")
            else:
                 print(clients)       
        elif command == 'D':
            nclient = input()
            if not delete_client(nclient):
                print ("no existe nombre")
            else:
                 print(clients)  
        elif command == 'L':
            _print_clients()
        elif command == 'E':
            pass    
        elif command == 'U':
            nclient = input()
            _print(command+"A")
            uclient = input()
            if not update_client(nclient,uclient):
                print ("no existe nombre")
            else:
                 print(clients)   
        print ("press enter to continue")    
        input()        