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
1. From ubiquity robots: `sudo systemctl disable magnibase`
1. On wifi: 
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
Copy the kobuki_labcontrol folder to /catkin_ws/src, then
```
ch ~catkin_ws
catkin_make
```
Make sure the name for each is correct.

### Autostart
Copy the autostart folder to /home/ubuntu and ```chmod``` each file. Set up a new cron job via
```
crontab -e
```

Then at the bottom:
```
@reboot bash /home/ubuntu/autostart/autostart_screens.sh
```

Cross your fingers and reboot!
