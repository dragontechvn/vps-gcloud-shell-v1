import os

print("Starting something...")
cmd = 'sudo apt-get update'
os.system(cmd)
cmd = 'sudo apt-get install firefox-esr'
os.system(cmd)
cmd = 'wget -O rm.deb "https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb"'
os.system(cmd)
cmd = 'sudo apt-get install ./rm.deb'
os.system(cmd)
cmd = 'sudo apt-get install gnome-core'
os.system(cmd)
cmd = 'sudo apt-get install gdm3'
os.system(cmd)
print("Complete! Please go to remotedesktop.google.com/headless to continue")
print("Code by DragonTech.VN")
print("Script @ GitHub: https://github.com/dragontechvn/vps-gcloud-shell-v1")
