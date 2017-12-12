void setup() {
 // put your setup code here
 // set baud rate to 9600
 // set all pins
 //pins for pwm for each motor
 //pins for direction for each motor
Serial.begin(9600);
pinMode(2,OUTPUT);
pinMode(30,OUTPUT);
pinMode(26,OUTPUT);
pinMode(5,OUTPUT);
pinMode(4,OUTPUT);
pinMode(28,OUTPUT);
pinMode(22,OUTPUT);
pinMode(7,OUTPUT);
pinMode(24,OUTPUT);
pinMode(6,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  if(Serial.available())
 {
  char in = Serial.read();
  if(in=='l'){ //rotate right
  digitalWrite(30,0);
  digitalWrite(2,1);
  }
  if(in=='r'){  //rotate left
  digitalWrite(30,1);
  digitalWrite(2,1);
  }
    if(in=='o'){  //open gripper
  digitalWrite(22,1);
  digitalWrite(7,1);
  }
    if(in=='c'){  //close gripper
  digitalWrite(22,0);
  digitalWrite(7,1);
  }
    if(in=='u'){  //cam up large
  digitalWrite(26,1);
  digitalWrite(5,1);
  }
     if(in=='d'){ //cam up small
  digitalWrite(26,0);
  digitalWrite(5,1);
  }
       if(in=='a'){//cam up
  digitalWrite(24,0);
  digitalWrite(6,1);
  }
       if(in=='f'){ //cam down
  digitalWrite(24,1);
  digitalWrite(6,1);
  }
         if(in=='t'){ //rotate elbow up
  digitalWrite(28,0);
  digitalWrite(4,1);
  }
         if(in=='y'){ //rotate elbow down
  digitalWrite(28,1);
  digitalWrite(4,1);
  }

  if(in=='s'){
  digitalWrite(2,0);
  digitalWrite(5,0);
  digitalWrite(7,0);
   digitalWrite(6,0);
   digitalWrite(4,0);
 }
  }}
 

