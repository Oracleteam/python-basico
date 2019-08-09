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
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']))


@clients.command()
@click.option('-n', '--client_uid', type=str, prompt=True, help='The client id')
@click.pass_context
def update(ctx, client_uid):
    """Update a client"""
    for i in enumerate(Client.schema()):
        message = "do you want change {i[1]}?"
        ans = input(message.format(i=i))
        if ans.upper() == "Y":
            msg="type {i[1]}:"
            ans = input(msg.format(i=i))
            
        else:
            pass


@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    """delete a client"""
    pass


all = clients
