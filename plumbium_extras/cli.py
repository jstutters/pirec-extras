from __future__ import print_function
import sys
import click
from . import archive, report
from .exceptions import ReportNotFound, FileNotFound


@click.group()
@click.argument('tar', type=click.Path(exists=True, dir_okay=False))
@click.pass_context
def cli(ctx, tar):
    ctx.obj = {}
    ctx.obj['tar'] = tar


@cli.command()
@click.argument('keypath')
@click.pass_context
def getkey(ctx, keypath):
    """Read a key from report.json with an archived analysis."""
    try:
        val = report.getkey(ctx.obj['tar'], keypath)
    except ReportNotFound as e:
        print('Error:', e, file=sys.stderr)
        sys.exit(1)
    except KeyError as e:
        print('Error: Key not found in report', file=sys.stderr)
        sys.exit(1)
    else:
        click.echo(val)


@cli.command()
@click.pass_context
def extrep(ctx):
    """Extract report.json from an archived analysis."""
    try:
        f = report.extract_report(ctx.obj['tar'])
    except ReportNotFound as e:
        print('Error:', e, file=sys.stderr)
        sys.exit(1)
    else:
        for l in f:
            l = l.replace('\\n', '\n')
            print(l, end='')


@cli.command()
@click.argument('filename')
@click.pass_context
def extfile(ctx, filename):
    """Extract a file from an archived analysis."""
    try:
        archive.extract_file(ctx.obj['tar'], filename, filename)
    except FileNotFound as e:
        print('Error:', e, file=sys.stderr)
        sys.exit(1)
