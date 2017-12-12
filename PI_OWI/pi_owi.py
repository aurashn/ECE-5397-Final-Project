from flask import Flask
from flask import render_template, request 
from flask_cors import CORS, cross_origin
import time

app = Flask(__name__)
#CORS(app,resources={r"/": {"origins": "http://10.0.0.10:8081"}})
import serial
ser = serial.Serial('/dev/ttyACM0', 9600)


a=1
@app.route("/")
#@cross_origin(origin='http://10.0.0.10:8081',headers=['Content- Type','Authorization'])
def index():
    return render_template('robot.html')

@app.route('/left_side')
def left_side():
    data1="LEFT"
    ser.write('l')
    return 'true'

@app.route('/right_side')
def right_side():
   data1="RIGHT"
   ser.write('r')
   return 'true'

@app.route('/close_side')
def close_side():
   data1="close"
   ser.write('c')
   return 'true'

@app.route('/cup_side')
def cup_side():
   data1="close"
   ser.write('f')
   return 'true'

@app.route('/cd_side')
def cd_side():
   data1="close"
   ser.write('a')
   return 'true'

@app.route('/open_side')
def open_side():
   data1="open"
   ser.write('o')
   return 'true'

@app.route('/up_side')
def up_side():
   data1="FORWARD"
   ser.write('u')
   return 'true'

@app.route('/down_side')
def down_side():
   data1="BACK"
   ser.write('d')
   return 'true'

@app.route('/stop')
def stop():
   data1="STOP"
   ser.write('s')
   return  'true'




if __name__ == "__main__":
 print "Start"
 app.run(host='0.0.0.0',port=5010)
