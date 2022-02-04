#!/usr/bin/env python
import rospy
from std_msgs.msg import String
sum1=0


def callback(data):
    global sum1
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    message=data.data 
    #number=rospy.sub(u"([^\u0030-\u0039])","",message)
    number=filter(str.isdigit, message)
    num=int(number)
    sum1=sum1+num
    
    print (sum1)

    
    
def velocity():

    rospy.init_node('velocity', anonymous=True) #

    rospy.Subscriber("Divide", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    velocity()