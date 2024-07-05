import click
from app.lib import db

@click.command('init-db')
def init_db_command():
    db.init_db()
    click.echo('Initialized the database.')

@click.command('migrate')
def migrate_command():
    db.migrate()
    click.echo('Migrated the database.')