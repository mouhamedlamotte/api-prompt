from .database_commands import init_db_command, migrate_command

def register_commands(app):
    app.cli.add_command(init_db_command)
    app.cli.add_command(migrate_command)