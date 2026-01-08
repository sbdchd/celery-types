import click
from celery.bin.base import CeleryCommand

upgrade: click.Group
settings: CeleryCommand
