# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
from flask import *
import MySQLdb
import MySQLdb.cursors
import warnings
warnings.filterwarnings("ignore")
from config import *

app = Flask(__name__)
app.config.from_object(__name__)

def connectdb():
	db = MySQLdb.connect(host=HOST, user=USER, passwd=PASSWORD, db=DATABASE, port=PORT, charset=CHARSET, cursorclass = MySQLdb.cursors.DictCursor)
	db.autocommit(True)
	cursor = db.cursor()
	return (db,cursor)

# 关闭数据库
def closedb(db,cursor):
	db.close()
	cursor.close()

@app.route('/')
def index():
	(db,cursor) = connectdb()
	cursor.execute("select * from movie limit 100")
	movies = cursor.fetchall()
	closedb(db,cursor)
	return render_template('index.html', movies=movies)

if __name__ == '__main__':
	app.run(debug=True)