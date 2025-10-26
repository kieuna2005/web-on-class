from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bài tập về nhà tuần 3'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'quan_ly_hang_khong'

mysql = MySQL(app)

@app.route('/input_chuyenbay_23001537', methods=['GET', 'POST'])
def input_chuyenbay():
    if request.method == 'POST':
        print(request.form) 
        details = request.form
        MaCB = details['MaCB']
        GaDi = details['GaDi']
        GaDen = details['GaDen']
        DoDai = details['DoDai']
        GioDi = details['GioDi']
        GioDen = details['GioDen']
        ChiPhi = details['ChiPhi']
        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO CHUYENBAY (MaCB, GaDi, GaDen, DoDai, GioDi, GioDen, ChiPhi)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (MaCB, GaDi, GaDen, DoDai, GioDi, GioDen, ChiPhi))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('input_chuyenbay.html')

@app.route('/view_chuyenbay_23001537')
def chuyenbay():
    cur = mysql.connection.cursor()
    #cur.execute("SELECT * FROM congviec")
    cur.execute("SELECT MaCB, GaDi, GaDen, DoDai, GioDi, GioDen, ChiPhi FROM chuyenbay")
    chuyenbay = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    cur.close()
    return render_template('chuyenbay.html', chuyenbay=chuyenbay, columns=columns)
        
@app.route('/input_maybay_23001537', methods=['GET', 'POST'])
def input_maybay():
    if request.method == 'POST':
        print(request.form) 
        details = request.form
        MaMB = details['MaMB']
        Loai = details['Loai']
        TamBay = details['TamBay']
        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO MAYBAY (MaMB, Loai, TamBay)
            VALUES (%s, %s, %s)
        """, (MaMB, Loai, TamBay))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('input_maybay.html')

@app.route('/view_maybay_23001537')
def maybay():
    cur = mysql.connection.cursor()
    cur.execute("SELECT MaMB, Loai, TamBay from maybay")
    maybay = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    cur.close()
    return render_template('maybay.html', maybay = maybay, columns=columns)

@app.route('/input_nhanvien_23001537', methods=['GET', 'POST'])
def input_nhanvien():
    if request.method == 'POST':
        print(request.form) 
        details = request.form
        MaNV = details['MaNV']
        Ten = details['Ten']
        Luong = details['Luong']
        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO NHANVIEN (MaNV, Ten, Luong)
            VALUES (%s, %s, %s)
        """, (MaNV, Ten, Luong))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('input_nhanvien.html')

@app.route('/view_nhanvien_23001537')
def nhanvien():
    cur = mysql.connection.cursor()
    cur.execute(" SELECT MaNV, Ten, Luong from nhanvien")
    nhanvien = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    cur.close()
    return render_template('nhanvien.html', nhanvien = nhanvien, columns=columns)

@app.route('/input_chungnhan_23001537', methods=['GET', 'POST'])
def input_chungnhan():
    if request.method == 'POST':
        print(request.form) 
        details = request.form
        MaNV = details['MaNV']
        MaMB = details['MaMB']
        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO CHUNGNHAN (MaNV, MaMB)
            VALUES (%s, %s)
        """, (MaNV, MaMB))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('input_chungnhan.html')

@app.route('/view_chungnhan_23001537')
def chungnhan():
    cur = mysql.connection.cursor()
    cur.execute(" SELECT MaNV, MaMB from chungnhan")
    chungnhan = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    cur.close()
    return render_template('chungnhan.html', chungnhan = chungnhan, columns=columns)