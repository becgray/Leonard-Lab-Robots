# !/bin/bash
LOG_FILE=/home/user/autostart/logs/log_autostart_screens.txt

echo "" >> ${LOG_FILE}
echo "" >> ${LOG_FILE}
echo "" >> ${LOG_FILE}
echo "" >> ${LOG_FILE}
echo "#############################################" >> ${LOG_FILE}
echo "Running autostart_screens.sh" >> ${LOG_FILE}
echo $(date) >> ${LOG_FILE}
echo "#############################################" >> ${LOG_FILE}
echo "" >> ${LOG_FILE}
echo "Logs:" >> ${LOG_FILE}

set -e
set -v

{

screen -d -m bash /home/user/autostart/start_roslaunch.sh

} &>> ${LOG_FILE}