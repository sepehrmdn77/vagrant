import click
import subprocess

@click.command()
@click.option('--up', '-u', help='Enter your Vagrant machine name to start.')
@click.option('--down', '-d', help='Enter your Vagrant machine name to halt.')
def CLI(up, down):
    """A simple CLI tool to manage Vagrant machines.
    '-u or --up + <machinename> for starting your machine and -d or --down + <machinename> for stopping your machine.'
    """
    if up and down:
        click.echo("Please enter one of commands not both at the same time!")
    elif up:
        # vagrant up
        is_here = (subprocess.check_output("vagrant status", shell=True, text=True)).split()
        if up in is_here:
            subprocess.run(f'vagrant up {up}', shell=True)
            click.echo(f'machine {up} is going up...')
        else:
            click.echo(f'{up} is not defined!')
    elif down:
        # vagrant halt
        is_here = (subprocess.check_output("vagrant status", shell=True, text=True)).split()
        if down in is_here:
            subprocess.run(f'vagrant halt {down}', shell=True)
            click.echo(f'machine {down} is going down...')
        else:
            click.echo(f'{down} is not defined!')
    else:
        click.echo("Please enter one options -u or -d + <machinename>.")

if __name__ == '__main__':
    CLI()