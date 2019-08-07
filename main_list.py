import os, sys
clients = ["Pablo","Ricardo"]

def create_client(client_name):
    global clients
    if client_name not in clients:
        clients.append(client_name)
    else:
        return False    
    return clients


def update_client(client_name,client_new_name):
    global clients
    if client_name in clients:
        index = clients.index(client_name)
        clients[index]=client_new_name
    else:
        return False    
    return clients


def delete_client(client_name):
    global clients
    if client_name in clients:
        clients.remove(client_name)
    else:
        return False    
    return clients    


def _print_clients():
    global clients
    print(clients)


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
        print("eso esto eso es to eso es todo amigos") 
    elif type == "UA":
        print("type new client to update") 
    else:
        print("opcion invalida") 


def _get_client():
    nclient = input()
    return nclient.lower().capitalize()

if __name__ == '__main__':
    command=""
    while (command != "E"):
        os.system('clear') 
        _print_welcome()
        command = input()
        command = command.upper()
        _print(command)
        if command == 'C':
            if not create_client(_get_client()):
                print ("ya existe")
            else:
                 print(clients)       
        elif command == 'D':
            if not delete_client(_get_client()):
                print ("no existe nombre")
            else:
                 print(clients)  
        elif command == 'L':
            _print_clients()
        elif command == 'E':
            sys.exit()    
        elif command == 'U':
            nclient = _get_client()
            _print(command+"A")
            uclient = _get_client()
            if not update_client(nclient,uclient):
                print ("no existe nombre")
            else:
                 print(clients)   
        print ("press enter to continue")    
        input()        