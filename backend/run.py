import click
from flask.cli import with_appcontext
from application import create_app, db
from application.models import User, Gender

app = create_app()

@app.cli.command('init-db')
# @with_appcontext
def init_db_command():
    db.create_all()
    click.echo('Initialized database')

@app.cli.command('create-user')
@click.argument('email') 
@click.argument('password') 
def create_user(email, password):
    u = User(
        first_name='Byte',
        last_name='Hacks',
        # dob=datetime.now(),
        gender=Gender.MALE,
        location='ma',
        email=email
    )
    u.set_password(password)
    db.session.add(u)
    db.session.commit()
    click.echo(f'Added {email} to the database')


    

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Gender': Gender}

if __name__ == "__main__":
    app.run(debug=True)