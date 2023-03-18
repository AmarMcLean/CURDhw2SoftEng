from flask import Flask, abort,render_template,request,redirect
from models import db,UserModel
 
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
 
@app.before_first_request
def create_table():
    db.create_all()
 
@app.route('/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
 
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        score = request.form['score']
        Users = UserModel(
            first_name=first_name,
            last_name=last_name,
            score=score
        )
        db.session.add(Users)
        db.session.commit()
        return redirect('/')
 
 
@app.route('/')
def RetrieveList():
    Users = UserModel.query.all()
    return render_template('datalist.html',Users = Users)
 
 
@app.route('/<int:id>')
def RetrieveUser(id):
    Users = UserModel.query.filter_by(id=id).first()
    if Users:
        return render_template('data.html', Users = Users)
    return f"Employee with id ={id} Doenst exist"
 
@app.route('/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    Users = UserModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if Users:
            db.session.delete(Users)
            db.session.commit()
            return redirect('/')
        abort(404)
    return render_template('delete.html')
 
app.run(host='localhost', port=5000)