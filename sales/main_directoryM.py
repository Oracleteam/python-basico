import sys
import os

clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software Engineer',
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data Engineer',
    },
]


def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already in client\'s list')


def list_client():
    global clients

    print('uid |  name  | company  | email  | position ')
    print('*' * 50)

    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']))


def update_client(index):
    global clients

    for idx, client in enumerate(clients[index]):
        message = "do you want change {name}?"
        ans = input(message.format(name=client))
        if ans.upper() == "Y":
            inp = input()
            clients[index][client] = inp
        else:
            pass


def delete_client(index):
    global clients

    clients.pop(index)


def _print_welcome():
    """ welcome message """
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?:')
    print('[C]reate client')
    print('[L]ist clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[E]xit')


def _get_message(command):
    """ message of crud acctions """
    if command == "C":
        print('Add client')
    elif command == "L":
        print('List client')
    elif command == "U":
        print('Update client')
    elif command == "D":
        print('Delete client')
    elif command == "S":
        print('Select client')
    elif command == "E":
        print('good bye')
    else:
        print("?")


def _get_client_field(field_name, message='What is the client {}?'):
    """ return data input """
    field = None

    while not field:
        field = input(message.format(field_name))

    return field


def _get_client():
    """ format client data """
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }

    return client


def _stop():
    """ stop script until press enter """
    print("press enter to continue")
    input()


if __name__ == '__main__':
    command = ''
    while(command != "E"):
        os.system('clear')
        _print_welcome()
        command = input()
        command = command.upper()
        _get_message(command)
        if command == "C":
            client = _get_client()
            create_client(client)
            list_client()
            _stop()
        elif command == "L":
            list_client()
            _stop()
        elif command == "U":
            update_client(int(_get_client_field("id")))
            list_client()
            _stop()
        elif command == "D":
            delete_client(int(_get_client_field("id")))
        elif command == "E":
            sys.exit()
        else:
            print("Incorrect option")
    _stop()
