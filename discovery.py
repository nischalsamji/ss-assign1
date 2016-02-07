import os
#I really don wanna code today but just keeping my streak intact :/

ssh_files = ['/etc/hosts','~/.ssh/config','/etc/ssh/ssh_config','~/.ssh/authorized_keys','~/.ssh/known_hosts','/etc/ssh/ssh_known_hosts']
for each_file in ssh_files:
    try:
        file_content = open(each_file,"r")
        filecontent = file_content.readlines()
        for each_line in filecontent:
            if each_line.starts_with("#"):
                continue
            else:
                print each_line
    except IOError:
        print each_file + " This file not found"
