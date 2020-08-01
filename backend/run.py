from application import create_app, db
from application.models import User, Gender

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Gender': Gender}

if __name__ == "__main__":
    app.run(debug=True)