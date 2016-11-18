import click
import report


@click.command()
@click.argument('tar', type=click.Path(exists=True, dir_okay=False))
@click.argument('keypath')
def getkey(tar, keypath):
    val = report.getkey(tar, keypath)
    click.echo(val)


if __name__ == "__main__":
    getkey()
