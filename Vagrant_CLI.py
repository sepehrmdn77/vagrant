import click
import subprocess
import search
@click.group()
def CLI():
    pass

@CLI.command()
@click.argument('name')
def init(name):
    '''Enter a name for creating a vagrant machine from vagrant cloud'''
    subprocess.run(f'vagrant init {name}', shell=True)

@CLI.command()
@click.argument('name')
def up(name):
    '''Enter the name for running the vagrant machine'''
    if search.search(name) == True:
        subprocess.run(f'vagrant up {name}', shell=True)
    else:
        click.echo('There is no machine named: {name}!')

@CLI.command()
@click.argument('name')
def halt(name):
    '''Enter the name for stopping the vagrant machine'''
    if search.search(name) == True:
        subprocess.run(f'vagrant halt {name}', shell=True)
    else:
        click.echo(f'There is no machine named: {name}!')

@CLI.command()
@click.argument('name')
def suspend(name):
    '''Enter the name for suspending the vagrant machine'''
    if search.search(name) == True:
        subprocess.run(f'vagrant suspend {name}', shell=True)
    else:
        click.echo('There is no machine named: {name}!')

@CLI.command()
@click.argument('name')
def resume(name):
    '''Enter the name for resuming the vagrant machine'''
    if search.search(name) == True:
        subprocess.run(f'vagrant halt {name}', shell=True)
    else:
        click.echo('There is no machine named: {name}!')
@CLI.command()
def list():
    '''Listing all machines'''
    click.echo(search.check())
@CLI.command()
def status():
    '''Status of all machines'''
    subprocess.run(f'vagrant status', shell=True)

if __name__ == '__main__':
    CLI()