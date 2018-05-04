#if defined(ARDUINO) && ARDUINO >= 100
#include "Arduino.h"
#else
#include <WProgram.h>
#endif
#include <Servo.h>
#include <ros.h>
#include <std_msgs/UInt16.h>
ros::NodeHandle nh;
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;

void servo_cb1( const std_msgs::UInt16& cmd_msg){
servo1.write(cmd_msg.data); //set 1servo angle, should be from 0-180
digitalWrite(13, HIGH-digitalRead(13)); //toggle led
}

void servo_cb2( const std_msgs::UInt16& cmd_msg){
servo2.write(cmd_msg.data); //set servo angle, should be from 0-180
digitalWrite(13, HIGH-digitalRead(13)); //toggle led
}

void servo_cb3( const std_msgs::UInt16& cmd_msg){
servo3.write(cmd_msg.data); //set servo angle, should be from 0-180
digitalWrite(13, HIGH-digitalRead(13)); //toggle led
}

void servo_cb4( const std_msgs::UInt16& cmd_msg){
servo4.write(cmd_msg.data); //set servo angle, should be from 0-180
digitalWrite(13, HIGH-digitalRead(13)); //toggle led
}

ros::Subscriber<std_msgs::UInt16> sub1("servo1", servo_cb1);
ros::Subscriber<std_msgs::UInt16> sub2("servo2", servo_cb2);
ros::Subscriber<std_msgs::UInt16> sub3("servo3", servo_cb3);
ros::Subscriber<std_msgs::UInt16> sub4("servo4", servo_cb4);

void setup(){
pinMode(13, OUTPUT);
nh.initNode();
nh.subscribe(sub1);
nh.subscribe(sub2);
nh.subscribe(sub3);
nh.subscribe(sub4); 
servo1.attach(11); //attach it to pin 5 (end)
servo2.attach(10); //attach it to pin 6
servo3.attach(9); //attach it to pin 10
servo4.attach(6); //attach it to pin 11 (base)
}
void loop(){
nh.spinOnce();
delay(1);
}

