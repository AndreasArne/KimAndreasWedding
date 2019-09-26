from app import create_app, db
from app.models import Guest, Party
# from app.config import DevConfig

# app = create_app(DevConfig)
app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Party': Party, 'Guest': Guest}