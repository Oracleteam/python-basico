import click
from clients.models import Client
from clients.services import ClientService


@click.group()
def clients():
    """Manages the clients lifecycle"""
    pass


@clients.command()
@click.option('-n', '--name', type=str, prompt=True, help='The client name')
@click.option('-n', '--company', type=str, prompt=True, help='The client company')
@click.option('-n', '--email', type=str, prompt=True, help='The client email')
@click.option('-n', '--position', type=str, prompt=True, help='The client position')
@click.pass_context
def create(ctx, name, company, email, position):
    """Create new client"""
    client = Client(name, company, email, position)
    client_service = ClientService(ctx.obj["clients_table"])
    client_service.create_client(client)


@clients.command()
@click.pass_context
def list(ctx):
    """List all clients"""
    client_service = ClientService(ctx.obj["clients_table"])
    click.echo('uid |  name  | company  | email  | position ')
    click.echo('*' * 50)
    for idx, client in enumerate(client_service.list_client()):
        click.echo('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=client["uid"],
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']))


@clients.command()
@click.option('-n', '--client_uid', type=str, prompt=True, help='The client id')
@click.pass_context
def update(ctx, client_uid):
    """Update a client"""
    client_service = ClientService(ctx.obj["clients_table"])
    client_list = client_service.list_client()
    client = [client for client in client_list if client["uid"] == client_uid]
    if client:
        clientss = _update_client_flow(Client(**client[0]))
        client_service.update_client(clientss)
        click.echo("Client updated")
    else:
        click.echo("Client not found")


def _update_client_flow(client):
    """ flow to update client """
    click.echo("Leave enmpty if you dont want modify the value")
    client.name = click.prompt("New Client", type=str, default=client.name)
    client.company = click.prompt(
        "New Company", type=str, default=client.company)
    client.email = click.prompt("New Email", type=str, default=client.email)
    client.position = click.prompt(
        "New Position", type=str, default=client.position)
    return client


@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    """delete a client"""
    pass


all = clients
