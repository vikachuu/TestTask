from flask import Flask

app = Flask(__name__)

app.config['POSTGRES_USER'] = 'postgres'
app.config['POSTGRES_PASSWORD'] = 'vikachu'
app.config['POSTGRES_DB'] = 'database'

# 'postgres://postgres:vikachu@localhost/database'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://' + app.config['POSTGRES_USER'] + ':' + \
                                                        app.config['POSTGRES_PASSWORD'] + '@localhost/' + \
                                                        app.config['POSTGRES_DB']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
