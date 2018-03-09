# !/bin/bash
LOG_FILE=/home/user/autostart/logs/log_start_roslaunch.txt
echo "" >> ${LOG_FILE}
echo "" >> ${LOG_FILE}
echo "" >> ${LOG_FILE}
echo "" >> ${LOG_FILE}
echo "#############################################" >> ${LOG_FILE}
echo "Running start_roslaunch.sh" >> ${LOG_FILE}
echo $(date) >> ${LOG_FILE}
echo "#############################################" >> ${LOG_FILE}
echo "" >> ${LOG_FILE}
echo "Logs:" >> ${LOG_FILE}

set -e

{
source /opt/ros/kinetic/setup.bash
source /home/ubuntu/catkin_ws/devel/setup.bash

export ROS_MASTER_URI=http://192.168.121.102:11311
export ROS_HOSTNAME=<Pi's IP>
export ROS_IP=<Pi's IP>

sleep 8

} &>> ${LOG_FILE}

set -v

{

roslaunch my_pkg my_launch.launch

} &>> ${LOG_FILE}