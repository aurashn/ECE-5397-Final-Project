from flask import Flask
from flask import render_template, request 
from flask_cors import CORS, cross_origin
import time

#create a flask app for hosting web controller
app = Flask(__name__)
#CORS(app,resources={r"/": {"origins": "http://10.0.0.10:8081"}})

#create a serial link to the arduino for sending commands 
import serial

#serial link on ACM0 at 9600 baud rate
ser = serial.Serial('/dev/ttyACM0', 9600)


a=1
@app.route("/")
#@cross_origin(origin='http://10.0.0.10:8081',headers=['Content- Type','Authorization'])
def index():
    return render_template('robot.html')

#rotate robot left
@app.route('/left')
def left_side():
    data1="LEFT"
    ser.write('l')
    return 'true'

#rotate robot right
@app.route('/right')
def right_side():
   data1="RIGHT"
   ser.write('r')
   return 'true'

#close robot gripper
@app.route('/close')
def close_side():
   data1="close"
   ser.write('c')
   return 'true'

#rotate gripper upwards
@app.route('/cup')
def cup_side():
   data1="close"
   ser.write('f')
   return 'true'

#rotate gripper downwards
@app.route('/cd')
def cd_side():
   data1="close"
   ser.write('a')
   return 'true'

#open robot gripper
@app.route('/open')
def open_side():
   data1="open"
   ser.write('o')
   return 'true'

#rotate robot elbow up
@app.route('/up')
def up_side():
   data1="FORWARD"
   ser.write('u')
   return 'true'

#rotate robot elbow down
@app.route('/down')
def down_side():
   data1="BACK"
   ser.write('d')
   return 'true'

#stop all movement
@app.route('/stop')
def stop():
   data1="STOP"
   ser.write('s')
   return  'true'




if __name__ == "__main__":
 print "Connect on the (local-ip):5010"
 app.run(host='0.0.0.0',port=5010)
