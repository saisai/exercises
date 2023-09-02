import click

@click.command()
@click.option('--item', type=(str, int))
def putitem(item):
    name, id = item
    click.echo(f"name={name} id={id}")

if __name__ == '__main__':
    putitem()

