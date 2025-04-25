from flask import Flask
from models import db, User, Aetherios
from os import path
from routes import init_routes
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aetherios.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize the extension with the app
    db.init_app(app)
    
    # Register all routes
    init_routes(app)

    CORS(app, resources={r"/*": {"origins": "http://localhost:9000"}})

    
    # Create database if it doesn't exist
    if not path.exists('database.db'):
        with app.app_context():
            db.create_all()
    
    return app

def populate_db():
    with app.app_context():
        # Check if the database is empty
        if Aetherios.query.count() == 0:
            # Populate the database with initial data
            stmt = Aetherios.__table__.insert().values([
                {'id': 1, 'name': 'Pyrotalon', 'element1': 'Fire', 'species': 'Bird'},
                {'id': 2, 'name': 'Aquadroid', 'element1': 'Water', 'species': 'Golem'},
                {'id': 3, 'name': 'Terrawyrm', 'element1': 'Earth', 'species': 'Drake'},
                {'id': 4, 'name': 'Voltwarg', 'element1': 'Thunder', 'species': 'Wolf'},
                {'id': 5, 'name': 'Venomrenard', 'element1': 'Poison', 'species': 'Fox'},
                {'id': 6, 'name': 'Raysprite', 'element1': 'Aura', 'species': 'Fairy'},
                {'id': 7, 'name': 'Scorchscale', 'element1': 'Fire', 'species': 'Drake'},
                {'id': 8, 'name': 'Cyrokin', 'element1': 'Water', 'species': 'Wolf'},
                {'id': 9, 'name': 'Geomech', 'element1': 'Earth', 'species': 'Golem'},
                {'id': 10, 'name': 'Staticcrest', 'element1': 'Thunder', 'species': 'Bird'}
            ])
            db.session.execute(stmt)
            db.session.commit()
            print("Database populated with initial data.")
        else:
            print("Database already populated. No action taken.")


if __name__ == '__main__':
    app = create_app()
    populate_db()
    # Run the app
    #app.run(debug=True)
    app.run(port = 8080, debug=True)
