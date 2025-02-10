import click
import subprocess
import search
@click.group()
def CLI():
    pass

@CLI.command()
@click.argument('name')
def init(name):
    '''Creating a vagrant machine from vagrant cloud'''
    subprocess.run(f'vagrant init {name}', shell=True)

@CLI.command()
@click.argument('name')
def up(name):
    '''Running the vagrant machine'''
    if search.search(name) == True:
        subprocess.run(f'vagrant up {name}', shell=True)
    else:
        click.echo('There is no machine named: {name}!')

@CLI.command()
@click.argument('name')
def halt(name):
    '''Stopping the vagrant machine'''
    if search.search(name) == True:
        subprocess.run(f'vagrant halt {name}', shell=True)
    else:
        click.echo(f'There is no machine named: {name}!')

@CLI.command()
@click.argument('name')
def suspend(name):
    '''Suspending the vagrant machine'''
    if search.search(name) == True:
        subprocess.run(f'vagrant suspend {name}', shell=True)
    else:
        click.echo('There is no machine named: {name}!')

@CLI.command()
@click.argument('name')
def resume(name):
    '''Resuming the vagrant machine'''
    if search.search(name) == True:
        subprocess.run(f'vagrant halt {name}', shell=True)
    else:
        click.echo('There is no machine named: {name}!')

if __name__ == '__main__':
    CLI()
