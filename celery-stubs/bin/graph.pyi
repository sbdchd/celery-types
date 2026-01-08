import click
from celery.bin.base import CeleryCommand

graph: click.Group
bootsteps: CeleryCommand
workers: CeleryCommand
