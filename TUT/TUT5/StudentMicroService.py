from flask import *
import sqlite3 as sqlite
app = Flask(__name__)
@app.route('/student-application')
def startstudentapplication():
	return render_template('student-application.html')
@app.route('/insert_stu',  methods = ['POST', 'GET'])
def insert_stu():
	message=" hello"
	if request.method == 'POST':
		try:
			id=request.form['id']
			company=request.form['company']
			con=sqlite.connect(r"C:\\Users\\Hp\\Desktop\\TPO\\StudentDb.db")
			cur=con.cursor()
			cur.execute("INSERT into student(id,company) values(?,?)",(id,company))
			con.commit()
			message="Successfully applied to the company"
		except Exception as e:
			con.rollback()
			message="Cannot apply for the company"			
		finally:
			con.close()
			return render_template('result-student-application.html',message=message)
	return "DONE"

#APPlication Status
@app.route('/student-application-status')
def start_stu_appl_status():
	return render_template('student-application-status.html')

@app.route('/application_status', methods=['POST','GET'])
def application_status():
	message="hello"
	if request.method=='POST':
		try:
			id=request.form['id']
			con=sqlite.connect(r"C:\\Users\\Hp\\Desktop\\TPO\\StudentDb.db")
			cur=con.cursor()
			cur.execute("SELECT status from student where id=?",(id,))
			for i in cur:
				message=i
			con.commit()
		except Exception as e:
			message="Error occured"
			con.rollback()
		finally:
			con.close()
			return render_template('result-student-application-status.html',message=message)
if __name__ == '__main__':
	app.run(debug = True)
