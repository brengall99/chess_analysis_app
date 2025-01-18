from flask import Flask

def create_app():
    app = Flask(__name__, static_folder='static', static_url_path='/static')
    app.config['SECRET_KEY'] = 'super_secret_key' 

    from .routes import home, analysis, game_lookup, predictions

    app.add_url_rule('/', view_func=home)
    app.add_url_rule('/analysis', view_func=analysis)
    app.add_url_rule('/lookup', view_func=game_lookup, methods=['GET', 'POST'])
    app.add_url_rule('/predictions', view_func=predictions, methods=['GET', 'POST'])

    return app