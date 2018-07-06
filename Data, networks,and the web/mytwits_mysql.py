from flask import Flask, request
from flask import render_template
from flask import redirect, url_for
from flask import session, flash, abort
from vs_url_for import vs_url_for
from forms import addTwitForm, editTwitForm, loginForm, registerForm
from flask_login import LoginManager, login_required
from flask_login import current_user, login_user, logout_user
## import the sqlalchemy database and the users & twits db classes
from models import db, Users, Twits
## import the passwordhelper class to do password hashing / checking
from passwordhelper import PasswordHelper
from flask_restful import Resource, Api
from flask_restful import fields, marshal_with, abort
from flask_restful import reqparse

login_manager = LoginManager()

app = Flask(__name__)
# configure the sqlalchenmy database URI that is used for the connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://mytwits_user:mytwits_password@localhost/mytwits'
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# initialise the sqlalchemy database connection
db.init_app(app)
# initialise flask-login
login_manager.init_app(app)
api = Api(app)  # initialise our api on the app

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# instantiate a password helper object
ph = PasswordHelper()

# ----resource fields to filter the output for flask-restful
resource_fields = {
    'twit_id': fields.Integer,
    'twit': fields.String,
    'user_id': fields.Integer,
    'created_at': fields.DateTime(dt_format='rfc822')
}

# ----parse and verify the api inputs
parser = reqparse.RequestParser()
parser.add_argument('twit', type=str, help='the text of the twit; must be a string')
parser.add_argument('twit_id', type=int, help='the id of the twit; must be an integer')
parser.add_argument('user_id', type=int, help='the id of the user; must be an integer')


# ----instantiating the resource; the main part of the flask-restful api
class TwitsApi(Resource):  # creating our api resource class
    @marshal_with(resource_fields)
    # to get twits using curl: curl -i localhost:8000/api
    def get(self):
        twits = Twits.query.order_by(Twits.created_at.desc()).all()
        return twits

    @marshal_with(resource_fields)
    # curl -d "twit='YOUR_MESSAGE_HERE'&user_id=YOUR_USER_ID&submit=SUBMIT" localhost:8000/api
    def post(self):
        args = parser.parse_args()
        twit = Twits(twit=args['twit'], user_id=args['user_id'])
        db.session.add(twit)
        db.session.commit()
        return twit, 201


class TwitsIdApi(Resource):
    @marshal_with(resource_fields)
    # to get a specific twit using curl: curl -i localhost:8000/api/TWIT_ID_HERE
    def get(self, twit_id):
        twit = Twits.query.filter_by(twit_id=twit_id).first()
        if not twit:
            abort(404, message="Twit {} doesn't exist".format(twit_id))
        return twit

    @marshal_with(resource_fields)
    # To edit a twit: curl -d "twit=YOUR_MESSAGE_HERE" localhost:8000/api/TWIT_ID_HERE -X PUT -v
    def put(self, twit_id):
        args = parser.parse_args()
        twit = Twits.query.filter_by(twit_id=twit_id).first()
        twit.twit = args['twit']
        db.session.add(twit)
        db.session.commit()
        return twit, 201

    @marshal_with(resource_fields)
    # to delete a twit: curl localhost:8000/api/TWID_ID_HERE -X DELETE -v
    def delete(self, twit_id):
        twit = Twits.query.filter_by(twit_id=twit_id).first()
        if not twit:
            abort(404, message="Twit {} doesn't exist".format(twit_id))
        db.session.delete(twit)
        db.session.commit()
        return {}, 204


# ----assigning a route for the api
api.add_resource(TwitsApi, '/api')
api.add_resource(TwitsIdApi, '/api/<int:twit_id>')


# ---- the callback function for flask-login
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


@app.route('/')
def index():
    twits = Twits.query.order_by(Twits.created_at.desc()).all()
    return render_template("mytwits_mysql.html", twits=twits)


@app.route('/<username>')
def timeline(username):
    twits = Users.query.filter_by(username=username).first().twits
    return render_template('timeline.html', twits=twits, username=username)


@app.route('/add_twit', methods=['GET', 'POST'])
@login_required
def add_twit():
    form = addTwitForm()
    if form.validate_on_submit():
        twit = form.twit.data
        user_id = current_user.user_id
        new_twit = Twits(twit=twit, user_id=user_id)
        # we need to add the object to the flask-sqlalchemy session
        # and then commit our changes for it to be inserted in to the database
        db.session.add(new_twit)
        db.session.commit()
        return redirect(vs_url_for('index'))
    return render_template('add_twit_mysql.html', form=form)


@app.route('/edit_twit', methods=['GET', 'POST'])
@login_required
def edit_twit():
    user_id = current_user.user_id
    form = editTwitForm()
    if request.args.get('id'):
        twit_id = request.args.get('id')
        # we use the Twits class and the query attribute provided by flask-sqlalchemy
        twit = Twits.query.filter_by(twit_id=twit_id).first()
        # the query object is over all records
        # to get the specific twit we use the first() methods
        # having obtained the twits object we can access the text as
        # the attribute twit.twit
        form.twit.data = twit.twit
        form.twit_id.data = twit_id
        return render_template('edit_twit_mysql.html', form=form)
    if form.validate_on_submit():
        # get the twit_id back from the form
        twit_id = form.twit_id.data
        # load that twit
        twit = Twits.query.filter_by(twit_id=twit_id).first()
        # change the twit text to the text submitted in the form
        twit.twit = form.twit.data
        # commit the change
        db.session.commit()
        return redirect(vs_url_for('index'))
    return render_template('edit_twit_mysql.html', form=form)


@app.route('/delete_twit', methods=['GET', 'POST'])
@login_required
def delete_twit():
    if request.args.get('id'):
        twit_id = request.args.get('id')
        twit_for_deletion = Twits.query.filter_by(twit_id=twit_id).first()
        db.session.delete(twit_for_deletion)
        db.session.commit()
    return redirect(vs_url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:  # if user is already logged in
        return redirect(vs_url_for('index'))  # do not display login form, send to index instead
    form = loginForm()
    if form.validate_on_submit():
        # get the user object via sqlalchemy
        password = form.password.data
        user = Users.query.filter_by(username=form.username.data).first()
        # use the password helper to validate the password
        if ph.validate_password(password, user.salt, user.hashed):
            login_user(user)
            flash('login successful!')
            return redirect(vs_url_for('index'))
        else:
            flash('Invalid username or password. Please try again')
            return redirect(vs_url_for('login'))
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    logout_user()
    flash('You are now logged out')
    return redirect(vs_url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:  # if user is already logged in
        return redirect(vs_url_for('index'))  # do not display registration form, send to index instead
    form = registerForm()  # instantiate registerForm class
    if form.validate_on_submit():  # check if the form validates
        user = Users(username=form.username.data)
        user.get_salt()
        user.get_hash(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful. Please log in.')
        return redirect(vs_url_for('login'))  # redirect to the login page
    return render_template('register.html', form=form)  # display register form


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)
