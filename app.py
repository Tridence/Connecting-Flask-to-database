from flask import Flask, render_template, request

from flask_mysqldb import MySQL

app = Flask(__name__)

app.config ['MYSQL_HOST'] = "localhost"
app.config ['MYSQL_USER'] = "root"
app.config ['MYSQL_PASSWORD'] = ""
app.config ['MYSQL_DB'] = "flask"

mysql = MySQL(app)

@app.route('/',methods=['GET','POST'])
def index():

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']

        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO connect (name,age) VALUES (%s,%s)",(name,age))

        mysql.connection.commit()

        cur.close()

        return "SUCCESS!"

    return render_template('index.html')

    @app.route('/users')
    def user(): 
        cur = mysql.connection.cursor()

        users = cur.execute("SELECT * FROM connect")

        if users > 0:
            userDetails = cur.fetchall()

            return render_template('users.html', userDetails=userDetails)

if __name__ == "main":
    app.run(debug=True)
