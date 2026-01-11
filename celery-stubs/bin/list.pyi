import click
from celery.bin.base import CeleryCommand

list_: click.Group
bindings: CeleryCommand
