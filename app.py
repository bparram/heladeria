from flask import Flask, render_template
import os
from database.db import db,init_db
from dotenv import load_dotenv
from models import copa_db, ingredientes_db,malteada_db,producto_db
from controllers.controlador_menu import traer_menu
from controllers.controller_malteada import controller_malteada
from controllers.controller_copa import controller_copa
from controllers.Contoller_ingredientes import controller_ingredientes


load_dotenv()
app = Flask(__name__, template_folder="views")

app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
init_db(app)

app.register_blueprint(traer_menu)
app.register_blueprint(controller_malteada)
app.register_blueprint(controller_copa)
app.register_blueprint(controller_ingredientes)



@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)    
