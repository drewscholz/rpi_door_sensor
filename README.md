# rpi_magnet_contact

This setup will communicate the door state to another server via API post.


$20 door sensor
----------------
* raspberry pi zero with headers
* 8GB micro SD card
* magnetic contact sensor


Set cron job
---------------
*  edit the file /etc/rsyslog.conf and uncomment this line `# cron.*                          /var/log/cron.log` (enables cron logging)
*  open crontab `sudo crontab -e`
*  add `SHELL=/bin/bash`, `PYTHONPATH=/usr/bin/python3`
*  set job `@reboot /home/pi/rpi_magnet_contact/magnet_contact.py 2>&1`
*  ensure python script has `#!/usr/bin/python3` at top of file
*  restart pi `sudo reboot`


If pip3 is not working:
---------------
* `sudo apt update`
