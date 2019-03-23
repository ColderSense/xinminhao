# -*- coding: utf-8 -*-
#！/usr/bin/python

from flask import Flask, render_template, Response, jsonify, request
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
# start flask app
app = Flask(__name__)


@app.route('/')
def index():
	"""Video streaming home page."""
	return render_template('index.html')
@app.route('/feedback')
def feedback():
	"""Video streaming home page."""
	return render_template('feedback.html')
	
@app.route('/send_email', methods=['POST'])
def send_email():
	sender = 'leecqchn@163.com'
	receiver = 'lee_cq@qq.com'
	data = request.get_json()
	name =data['name']
	email =data['email']
	message = data['message']
	print(name, email, message)
	
	send_msg = 'The person ' + name + ' has send some message to you,' + 'the email is: ' + email + ', the feedback message is: ' + message
	msg=MIMEText(send_msg,'plain','utf-8')
	msg['From']=formataddr([name,sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
	msg['To']=formataddr(["lichaoqun",receiver])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
	msg['Subject']="xinminhao_feedback" #邮件的主题，也可以说是标题
		
	smtp = smtplib.SMTP() 
	smtp.connect('smtp.163.com',25) 
	smtp.login('leecqchn@163.com', 'lcq19930819') 
	smtp.sendmail(sender, receiver, msg.as_string()) 
	smtp.quit()
	print(jsonify({"msg": "success"}))
	return "success"


if __name__ == "__main__":
	# open and run simulink model threading
	'''
	t= threading.Thread(target=run_simulink)
	t.setDaemon(True)
	t.start()
	'''	
	# open url
	#webbrowser.open("https://127.0.0.1:5000")
	# open web service
	app.run()
