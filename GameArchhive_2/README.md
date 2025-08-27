Hi Pascal!

## Projekt Ideen und ToDos
- [Projekt-Ideen](./ideas.md)


from flask import Blueprint, render_template

projekt1_bp = Blueprint('projekt1', __name__,
                        template_folder='templates',
                        static_folder='static')

@projekt1_bp.route('/')
def start():
    return render_template('projekt1/start.html')








from flask import Flask
from projekt1.routes import projekt1_bp
from projekt2.routes import projekt2_bp
from projekt3.routes import projekt3_bp

app = Flask(__name__)

# Blueprints registrieren
app.register_blueprint(projekt1_bp, url_prefix='/projekt1')
app.register_blueprint(projekt2_bp, url_prefix='/projekt2')
app.register_blueprint(projekt3_bp, url_prefix='/projekt3')

if __name__ == '__main__':
    app.run(debug=True)
