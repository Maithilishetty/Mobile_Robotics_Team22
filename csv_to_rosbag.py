import csv
import sys
import rospy
import rosbag
import tf
from math import pi
from tf2_msgs.msg import TFMessage
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Path

# MAKE SURE TO RUN THIS COMMAND TO ESTABLISH A BASE FRAME
# rosrun tf static_transform_publisher 0 0 0 0 0 0 1 map my_frame 10

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Please give a csv file path as an argument.")
		exit(1)
		
	
	with open(sys.argv[1], 'r') as file:
		with rosbag.Bag("out.bag", 'w') as bag:
			reader = csv.reader(file)
			next(file) # skip first line (headers)
			## get timestamp offset
			#start_time = int(reader.readline().split(",")[0])
			#curr_time = rospy.Time.now().to_nsec()
			#offset = start_time - curr_time
			#file.seek(0) # reset file pointer
			#next(file) # skip first line again
			
			paths = Path()
			paths.header.frame_id = 'my_frame'
			paths.poses = []
			
			# loop through all data and put them in a bag
			for vals in reader:
				#vals = row.split(",")
				if len(vals) != 8:
					continue
					
				t = rospy.Time(0, int(vals[0]))
					
				# Create the laser message
				msg = PoseStamped()
				msg.header.frame_id = 'my_frame'
				msg.header.stamp = t
				msg.pose.position.x = float(vals[1]) # x
				msg.pose.position.y = float(vals[2]) # y
				msg.pose.position.z = float(vals[3]) # z
				msg.pose.orientation.x = float(vals[4]) # qx
				msg.pose.orientation.y = float(vals[5]) # qy
				msg.pose.orientation.z = float(vals[6]) # qz
				msg.pose.orientation.w = float(vals[7]) # qw
								
				# Write to bag
				bag.write('auv', msg, t)
				paths.poses.append(msg)
				paths.header.stamp = t
				bag.write('path', paths, t)
				
