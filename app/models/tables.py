from app import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Interge, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    name = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, id, username, email, name, password):
        self.id = id
        self.username = username
        self.email = email
        self.name = name
        self.password = password

    def __repr__(self):
        return "<User %r>" % self.username

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Interge, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.String, db.ForeingnKey('users.id'))
    user = db.relationship('User', foreingn_key=user_id)

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return "<Post {}>".format(self.id)

class Follow(db.Model):
    __tablename__ = "follow"
    id = db.Column(db.Interge, primary_key=True)
    user_id = db.Column(db.String, db.ForeingnKey('users.id'))
    user_follower = db.Column(db.String, db.ForeingnKey('users.id'))

    user = db.relationship('User', foreingn_key=user_id)
    follower = db.relationship('User', foreingn_key=user_follower)


    def __init__(self, user_id, user_follower):
        self.user_id = user_id
        self.user_follower = user_follower

