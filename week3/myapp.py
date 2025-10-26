from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, world'

@app.route('/example')
def example():
    return render_template('example.html')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'quan_ly_de_an'

mysql = MySQL(app)

@app.route('/input', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form) 
        details = request.form
        MADA = details['MADA']
        STT = details['STT']
        TEN_CONG_VIEC = details['TEN_CONG_VIEC']
        cur = mysql.connection.cursor()
        cur.execute("""INSERT INTO congviec(MADA, STT, TEN_CONG_VIEC) VALUES (%s, %s, %s)""", (MADA, STT, TEN_CONG_VIEC))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')

@app.route('/congviec')
def congviec():
    cur = mysql.connection.cursor()
    #cur.execute("SELECT * FROM congviec")
    cur.execute("SELECT MADA, STT, TEN_CONG_VIEC FROM congviec")
    congviec = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    cur.close()
    return render_template('congviec.html', congviec=congviec, columns=columns)
        
