"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template
from models import db, connect_db, Cupcake
from forms import CupcakeForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcake_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)

@app.route('/')
def index_page():
    form= CupcakeForm()
    return render_template('index.html', form=form)

@app.route('/api/cupcakes')
def list_cupcakes():
    """get all cupcakes"""
    all_cups = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=all_cups)

@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    """get a single cupcake"""
    cupcake =Cupcake.query.get_or_404(id)
    return jsonify(cupcake= cupcake.serialize())


@app.route('/api/cupcakes', methods=['POST'])
def add_cupcake():
    """adds a new cupcake"""
    new_cupcake = Cupcake(flavor=request.json['flavor'],size=request.json['size'],
                          rating=request.json['rating'],image=request.json['image'])
    db.session.add(new_cupcake)
    db.session.commit()
    json = jsonify(cupcake=new_cupcake.serialize())
    return(json, 201)

@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def update_cupcake(id):
    """updates a cupcake"""
    cupcake =Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get('flavor',cupcake.flavor)
    cupcake.size = request.json.get('size',cupcake.size)
    cupcake.rating = request.json.get('rating',cupcake.rating)
    cupcake.image = request.json.get('image',cupcake.image)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcake(id):
    """deletes a cupcake"""
    cupcake =Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="Deleted")




