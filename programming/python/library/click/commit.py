import click

@click.command()
@click.option('--message', '-m', multiple=True)
def commit(message):
    click.echo('\n'.join(message))
    print('message ', message)

if __name__ == '__main__':
    commit()


