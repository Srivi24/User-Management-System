from flask import Flask, render_template, url_for, request, redirect, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
#Database linking connection
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="" # Enter your MySQL workbench user password
app.config["MYSQL_DB"]="crud"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(app)


#Loading Home Page
@app.route("/")
@app.route('/home')
def home():
    count = []
    con=mysql.connection.cursor()
    sql="SELECT ID, NAME, AGE, CITY FROM users"
    con.execute(sql)
    res=con.fetchall()
    l = len(res)
    for k in range(1,l+1):
        count.append(k)
    return render_template("home.html",datas=res, count=count)

#Add Users
@app.route('/add', methods = ['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        city = request.form['city']
        if int(age) > 12:
            con = mysql.connection.cursor()
            sql = "INSERT INTO users (NAME, AGE, CITY) VALUES (%s, %s, %s)"
            con.execute(sql, [name, age, city])
            mysql.connection.commit()
            con.close()
            flash('User Details Added')
            return redirect(url_for("home"))
        else:
            flash("Age must be greater than 12")
            return redirect(url_for("edit"))
    return render_template('addUser.html')

#Edit User
@app.route("/edit/<string:id>",methods=['GET','POST'])
def edit(id):
    con=mysql.connection.cursor()
    if request.method=='POST':
        name=request.form['name']
        city=request.form['city']
        age=request.form['age']
        sql="update users set NAME=%s,CITY=%s,AGE=%s where ID=%s"
        con.execute(sql,[name,city,age,id])
        mysql.connection.commit()
        con.close()
        flash('User Detail Updated')
        return redirect(url_for("home"))
        
    sql="select * from users where ID=%s"
    con.execute(sql,[id])
    res=con.fetchone()
    return render_template("edit.html",datas=res)

#Delete User
@app.route("/delete/<string:id>",methods=['GET','POST'])
def delete(id):
    con=mysql.connection.cursor()
    sql="delete from users where ID=%s"
    con.execute(sql,[id])
    mysql.connection.commit()
    con.close()
    flash('User Details Deleted')
    return redirect(url_for("home"))


if (__name__ == '__main__'):
    app.secret_key = "abc123"
    app.run(debug=True)

