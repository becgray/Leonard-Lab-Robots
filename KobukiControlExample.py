#!/usr/bin/env python
from __future__ import print_function
import os
import sys
import rospy
import time
from kobuki_msgs.msg import BumperEvent,MotorPower,WheelDropEvent,ButtonEvent
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty
from nav_msgs.msg import Odometry
from threading import Thread

def threadedPublisher():
    print("hello from thread")
    time.sleep(2)

 
class SimpleKobuki:
    def __init__(self):
        #Events
        self.bumper_sub = rospy.Subscriber("mobile_base/events/bumper", BumperEvent, self.bumper_cb)
        self.wheel_drop_sub = rospy.Subscriber("mobile_base/events/wheel_drop", WheelDropEvent, self.wheel_drop_cb)
        self.wheel_drop_sub = rospy.Subscriber("mobile_base/events/button", ButtonEvent, self.button_cb)

        #Commands
        self.power_cmd_pub = rospy.Publisher("mobile_base/commands/motor_power", MotorPower,queue_size=10)
        self.vel_cmd_pub = rospy.Publisher("mobile_base/commands/velocity",Twist,queue_size=10)
        self.vel_cmd = Twist()
        self.odm_reset_pub = rospy.Publisher("mobile_base/commands/reset_odometry",Empty,queue_size=10)
        self.r = rospy.Rate(10);

        #Get Data
        self.odometer_sub = rospy.Subscriber("odom", Odometry, self.Odometry_cb)

        #Threading for continuous input
        thread = Thread(target = self.threadedPublisher)
        thread.daemon = True
        thread.start()

        #Variables
        self.odometry = Odometry
        self.max_x_vel = 1.5
        self.max_ang_vel = 1.5

    #Begin class methods

    def threadedPublisher(self): #Contiually publishes commands to avoid timeout
        while True:      
            self.r.sleep()
            self.vel_cmd_pub.publish(self.vel_cmd)

    def bumper_cb(self, data):
        sys.stdout.flush()
        if data.state == BumperEvent.PRESSED:
            sys.stdout.write("\r\033[K" + "PRESSED")
            self.vel_cmd.linear.x = 0 #Turns x velocity to 0 is bumer pressed
            self.vel_cmd.angular.z = 0 #Turns angular velocity to 0 is bumer pressed
        elif data.state == BumperEvent.RELEASED:
            sys.stdout.write("\r\033[K" + "RELEASED")
        else:
            sys.stdout.write("\r\033[K" + "Bumper Unknown event")

    def wheel_drop_cb(self, data):
        sys.stdout.flush()
        if data.state == WheelDropEvent.DROPPED:
            sys.stdout.write("\r\033[K" + "WHEEL DROPPED")
            self.vel_cmd.linear.x = 0 #Turns x velocity to 0 is bumer pressed
            self.vel_cmd.angular.z = 0 #Turns angular velocity to 0 is bumer pressed
        elif data.state == WheelDropEvent.RAISED:
            sys.stdout.write("\r\033[K" + "WHEEL RAISED")
        else:
            sys.stdout.write("\r\033[K" + "Bumper Wheel Drop event")

    def button_cb(self, data):
        sys.stdout.flush()
        if data.button == ButtonEvent.Button0:
            if data.state == ButtonEvent.RELEASED:
                #print("Button0 Released")
                pass
                #Do stuff on release
            else:
                print("Button0 Pressed")
                pass
                 #Do stuff on press
        if data.button == ButtonEvent.Button1:
            if data.state == ButtonEvent.RELEASED:
                #print("Button1 Released")
                pass
                #Do stuff on release
            else:
                print("Button1 Pressed")
                pass
                 #Do stuff on press
        if data.button == ButtonEvent.Button2:
            if data.state == ButtonEvent.RELEASED:
                #print("Button2 Released")
                pass
                #Do stuff on release
            else:
                print("Button2 Pressed")
                pass
                 #Do stuff on press
   
    def waitConnection(self):
        while self.power_cmd_pub.get_num_connections() < 1 and rospy.is_shutdown() == 0:
            print("Waiting...")
            time.sleep(1)
        print("Connected")

    def setLinearVel(self, vel): #m/s
        print("test func")
        self.vel_cmd.linear.x = vel
        self.vel_cmd_pub.publish(self.vel_cmd)

    def setAngularVel(self, vel): #rad/sec
        self.vel_cmd.angular.z = vel
        self.vel_cmd_pub.publish(self.vel_cmd)

    def turnOn(self):
        self.power_cmd_pub.publish(MotorPower(MotorPower.ON))
        
    def turnOff(self):
        self.power_cmd_pub.publish(MotorPower(MotorPower.OFF))

    def resetOdometry(self):
        self.odm_reset_pub.publish(Empty())

    def controlLed(self, ID, color):
        print('Not implemented yet')
        
    def Odometry_cb(self,data):
        self.odometry = data
        print(self.odometry.pose.pose)
        pass

def main(args):
    rospy.init_node("SimpleKobuki_View", anonymous=True) 
    kobuki = SimpleKobuki() #create Kobuki instance
    kobuki.waitConnection() #Wait for connection to be established


    
    try:  #Execute code is node is running
        if not rospy.is_shutdown():
            #-----------------------Main code begins here---------------------
            #kobuki.turnOn()
            kobuki.setLinearVel(0.5)
            rospy.sleep(3)
            kobuki.resetOdometry()            
            #kobuki.turnOff()


            #------------------------Main code ends here----------------------
    except KeyboardInterrupt:
        print("\r\033[K"+"Shutting down")
 
if __name__ == '__main__':
    os.system("clear")
    main(sys.argv)
