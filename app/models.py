from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, index=True)
    secure_password = db.Column(db.String(255), nullable=False)
    pitches = db.relationship('Pitch', backref='user', lazy='dynamic')
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitches = db.relationship('Pitch', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')

    @classmethod
    def get_comments(cls, pitch_id):
        comments = Comment.query.filter_by(pitch_id=pitch_id).all()

        return comments

    def save_u(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

        @property
        def set_password(self):
            raise AttributeError('You cannot read the password attribute')

        @set_password.setter
        def password(self, password):
            self.secure_password = generate_password_hash(password)

        def verify_password(self, password):
            return check_password_hash(self.secure_password, password)


def __repr__(self):
    return f'User {self.username}'


class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    post = db.Column(db.Text())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category = db.Column(db.String(255), index=True)
    comment = db.relationship('Comment', backref='pitch', lazy='dynamic')

    def save_p(self):
        db.session.add(self)
        db.session.commit()


@classmethod
def get_upvotes(cls, id):
    upvote = Upvote.query.filter_by(pitch_id=id).all()
    return upvote


@classmethod
def get_downvotes(cls,id):
        downvote = Downvote.query.filter_by(pitch_id=id).all()
        return downvote


def __repr__(self):
    return f'Pitch {self.post}'


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

    def save_p(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'comment:{self.comment}'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
