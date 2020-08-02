import click
from flask.cli import FlaskGroup
from application import create_app, db
from application.models import User, Gender


cli = FlaskGroup(create_app=create_app)


@cli.command('create_db')
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
    click.echo('Initialized database')


@cli.command('create_user')
@click.argument('email') 
@click.argument('password') 
def create_user(email, password):
    u = User(
        first_name='Byte',
        last_name='Hacks',
        # dob=datetime.now(),
        gender=Gender.MALE,
        location='ma',
        email=email,
        jobs=[],
    )
    u.set_password(password)
    db.session.add(u)
    db.session.commit()
    click.echo(f'Added {email} to the database')


if __name__ == "__main__":
    cli()