import click

@click.command()
@click.option('--pos', nargs=2, type=float)
def findme(pos):
    a, b = pos
    click.echo(f"{a} / {b}")


if __name__ == '__main__':
    findme()

