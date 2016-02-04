import os


ssh_files = ['/etc/hosts','~/.ssh/config','/etc/ssh/ssh_config','~/.ssh/authorized_keys','~/.ssh/known_hosts','/etc/ssh/ssh_known_hosts']
for each_file in ssh_files:
  file_content = read(each_file,"r")
  print file_content.readlines()
