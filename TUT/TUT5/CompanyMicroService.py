from flask import *
import sqlite3 as sqlite
app = Flask(__name__)

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
