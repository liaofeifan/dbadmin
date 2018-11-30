from app import create_app, db
from app.models import User

app = create_app()
cli.register(app)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=False)


#http://test.wenrui.work/