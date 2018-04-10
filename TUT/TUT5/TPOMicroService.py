from flask import *
import sqlite3 as sqlite
app = Flask(__name__)


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

if __name__ == '__main__':
	app.run(debug = True)
