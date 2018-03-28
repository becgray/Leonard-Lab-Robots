# Leonard-Lab-Robots
Setup info the the Leonard Lab Robots
## Etching the image onto the SD card
1. Download file from: https://downloads.ubiquityrobotics.com/pi.html
1. Etch on SD card, plug into Pi
1. Login password: ubuntu
### First time setup
1. Remove need for password with every use of `sudo`:
```
sudo visudo
ubuntu ALL=(ALL) NOPASSWD:ALL
```
1. From ubiquity robots: `sudo systemctl disable magni-base`
1. update and upgrade “apt-get” (internet connection required)
```
sudo apt-get update
sudo apt-get upgrade
```
### Enabling auto-login
Go to System Tools>Users and Groups and change to not requiring password on login.
Then in terminal:
```
sudo nano etc/lightdm/lightdm.conf.d/12-autologin.conf

[Seat:*]
autologin-user=ubuntu
autologin-user-timeout=0
```

### Getting ROS and Kobukis ready
This section is from http://wiki.ros.org/kobuki/Tutorials/Installation
**Install Kobuki**
To install Kobuki packages:
```
sudo apt-get install ros-kinetic-kobuki ros-kinetic-kobuki-core
```
**Dialout Group**
If not already in the dialout group:
```
sudo usermod -a -G dialout $USER
```
and then log out, log back in again.

**Set Udev Rule**
```
rosrun kobuki_ftdi create_udev_rules
```

### Launch files
Copy the kobuki_labcontrol (from USB) folder to /catkin_ws/src, then
```
cd ~catkin_ws
catkin_make
```
Make sure the name for each is correct.



### Autostart
Copy the autostart folder to /home/ubuntu and update "start_roslaunch" to include the correct IP.
```chmod``` each file. 
Set up a new cron job via:
```
crontab -e
```

Then at the bottom:
```
@reboot bash /home/ubuntu/autostart/autostart_screens.sh
```

Cross your fingers and reboot!

### Sidenotes: If Firefox crashes all the time
This solution is from https://ubuntuforums.org/showthread.php?t=2382079
**Install Firefox ESR**
```
sudo add-apt-repository ppa:mozillateam/ppa
sudo apt-get update
sudo apt-get install firefox-esr
```
You may also want to uninstall the built-in problematic Firefox
```
sudo apt-get remove firefox
```


