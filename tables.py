from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, password, name, email) -> None:
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


class TradeLog(db.Model):
    __tablename__ = 'trocas'

    id = db.Column(db.Integer, primary_key=True)
    troca = db.Column(db.Text)  # registro da troca
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    trade_owner = db.relationship('User', foreign_keys=user_id)

    def __init__(self, troca, user_id) -> None:
        self.troca = troca
        self.user_id = user_id

    def __repr__(self):
        return '<Troca %r>' % self.id
