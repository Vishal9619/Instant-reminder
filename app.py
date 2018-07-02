from flask import Flask, request, render_template, redirect, url_for
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, date
import time
from twilio.rest import Client

app = Flask(__name__)
mobile = ""
note = "Reminder for you"
tot_fail = 0
schedular = BackgroundScheduler()
def StartSMS():
		global mobile,note,tot_fail
		current = int(datetime.now().strftime("%H"))
		if(current >= 21 and current <= 9):
			return

		mobile = mobile
		account_sid = "AC1dbcae0e435ef98c73e01cb49e0a5e35"
		auth_token = "4c195142b9173861838bbd2abb98fae3"

		client = Client(account_sid,auth_token)

		message = client.messages.create(
			to = mobile,
			from_ = "+13862109616",
			body = "Hello World!"
			)
		time.sleep(10)
		sms_status=message.sid
		message = client.messages(sms_status).fetch()
		sms_status = message.status
		fail = 0
		while(not(sms_status == 'delivered' or sms_status == 'received')) and (fail<5):
			message = client.messages.create(
				to = mobile,
				from_ = "+13862109616",
				body = note
				)
			fail+=1
			sms_status=message.sid
			time.sleep(10)
			message = client.messages(sms_status).fetch()
			sms_status = message.status
		tot_fail += fail
		print("Message failed for ",tot_fail," times")

@app.route("/", methods = ['POST','GET'])
def index():
	if request.method == "POST":
		global mobile,note
		mobile = request.form['mobile']
		note = request.form['note']
		global schedular
		schedular.add_job(StartSMS,'interval',minutes=1,id=mobile)
		schedular.start()
		return render_template('congo.html', mobile=mobile)
	else:
		return render_template('index.html')

@app.route('/home', methods = ['POST','GET'])
def reminder():
	if request.method == "POST":
		sms_val = request.form['optradio']
		if(sms_val=='1'):
			global schedular, mobile
			schedular.remove_job(mobile);
			mobile=""
			note=""
			schedular.shutdown()
			schedular=BackgroundScheduler()
			return render_template('index.html')
		else:
			return render_template('congo.html')

if __name__ == "__main__":
	app.debug=True
	app.run(host="0.0.0.0",port=8000)