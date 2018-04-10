from flask import *
import sqlite3 as sqlite
app = Flask(__name__)
@app.route('/')
def starthome():
	return render_template('home.html')

@app.route('/student')
def startstudent():
	return render_template('student.html')
@app.route('/company')
def startcompany():
	return render_template('company.html')
@app.route('/tpo')
def starttpo():
	return render_template('tpo.html')
#APPLY for companies
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

#TPO Microservices
#invite company

@app.route('/invite-company')
def startinvitecompany():
	return render_template('invite-company.html')
@app.route('/insert_company',methods=['POST','GET'])
def insert_company():
	message="hello"
	if request.method=='POST':
		try:
			companyname=request.form['company']
			con=sqlite.connect(r"C:\\Users\\Hp\\Desktop\\TPO\\CompanyDb.db")
			cur=con.cursor()
			cur.execute("INSERT into company(name,preferred_branch) values(?,?)",(companyname,'IT'))
			con.commit()
			message="Invitaion sent"
		except Exception as e:
			con.rollback()
			message="Couldn't invite the company...try again later"
		finally:
			con.close()
			return render_template('result-invite-company.html',message=message)

#schedule company
@app.route('/schedule-company')
def startschedulecompany():
	return render_template('schedule-company.html')
@app.route('/schedule',methods=['POST','GET'])
def schedule():
	message="hello"
	if request.method=='POST':
		try:
			companyname=request.form['company']
			con=sqlite.connect(r"C:\\Users\\Hp\\Desktop\\TPO\\CompanyDb.db")
			cur=con.cursor()
			cur.execute("UPDATE company SET Date=? where name=?",("Schduled",companyname))
			con.commit()
			message="Company is Schduled"
		except Exception as e:
			con.rollback()
			message="Couldn't schedule the company...try again later"
		finally:
			con.close()
			return render_template('result-schedule-company.html',message=message)

#Company Microservices
#request to tpo
@app.route('/send-req-to-tpo')
def startreqtotpo():
	return render_template('req_to_tpo.html')

@app.route('/request_tpo',methods=['POST','GET'])
def insert_request():
	message="hello"
	if request.method=='POST':
		try:
			companyname=request.form['company']
			branch=request.form['branch']
			salary=request.form['salary']
			con=sqlite.connect(r"C:\\Users\\Hp\\Desktop\\TPO\\CompanyDb.db")
			cur=con.cursor()
			cur.execute("INSERT into company(name,preferred_branch,salary) values(?,?,?)",(companyname,branch,salary))
			con.commit()
			message="Company sent request to TPO"
		except Exception as e:
			con.rollback()
			message="Couldn't request to TPO...try again later"
		finally:
			con.close()
			return render_template('result-request-to-tpo.html',message=message)
@app.route('/send-shortlist')
def startsendshortlist():
	return render_template('send-shortlist.html')
@app.route('/shortlist',methods=['POST','GET'])
def shortlist():
	message="hello"
	if request.method=='POST':
		try:
			companyname=request.form['company']
			id=request.form['id']
			con=sqlite.connect(r"C:\\Users\\Hp\\Desktop\\TPO\\StudentDb.db")
			cur=con.cursor()
			cur.execute("UPDATE student set status=? where id=? AND company=?",("Selected",id,companyname))
			con.commit()
			message="Company sent request to TPO"
		except Exception as e:
			con.rollback()
			message="Couldn't request to TPO...try again later"
		finally:
			con.close()
			return render_template('result-send-shortlist.html',message=message)
if __name__ == '__main__':
	app.run(debug = True)
