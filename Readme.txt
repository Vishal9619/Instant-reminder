Instant Reminder - An application through which we can send reminders via text message directly on mobile after every 60 minutes.

REQUIREMENTS
============
 Python - 3.6.5
 Flask - 1.0.2
 APScheduler==3.5.1
 twilio==6.14.7

PRE-REQUISTES TO BE KNOWN
=========================
1- Since the app has been designed using twilio api, so the mobile number you wish to receive messages must be verified here- https://www.twilio.com/console/phone-numbers/verified

2- If you enter a mobile number which isn't verified on twilio, then you wont be receiving messages. After every 60 minute, the number of times message sending failed is shown on terminal.

3- The app has been designed for a single person.(It can be designed for many people using database)

4- The app will not send message between 9:00 PM to 9:00 AM as twilio doesn't allow messaging between this time in India.(This can be handled by asking user on front end about the time during which he sleeps or by various other techniques)

5- The screenshots of the app have been included in Screenshots folder.

INSTRUCTIONS TO RUN THE APP
===========================
1- First we need to start the virtual environment for Flask by using command- "source venv/bin/activate".
2- Next, we need to run our app using command- "python3 app.py"
3- Some dependencies will be asked to install, which have been imported in python app, so they can be installed using pip3 commands.
4- After the app successfully runs, then it will be started on local host.
5- Open your browser and enter url- "http://0.0.0.0:8000/"
6- The app is started!
7- Enter your twilio verified mobile number and text message to start receiving reminders every 1 hour.


The application is deployed on heroku here: https://instant-reminder.herokuapp.com
Currently its failing to execute properly on heroku, as wheneven we select Yes on next page and submit, it shows error. This can be handled by removing /home from page link, and the app will start running properly.