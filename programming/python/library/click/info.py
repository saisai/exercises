import sys
import click


@click.command()
@click.option('--shout/--no-shout', default=False)
def info(shout):
    rv = sys.platform
    if shout:
        rv = rv.upper() + '!!!!!1'
    click.echo(rv)

if __name__ == '__main__':
    info()

