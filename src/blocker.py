from datetime import datetime
import tkinter as tk

end_time = datetime(2022, 6, 1, 0, 0)
sites = ['www.reddit.com', 'reddit.com', 'www.facebook.com', 'facebook.com']
hosts_filepath = 'C:\\Windows\\System32\\Drivers\\etc\\hosts'
redirect = "127.0.0.1"


def block():
    if datetime.now() < end_time:
        print("Block sites!")
        with open(hosts_filepath, 'r+') as hosts:
            hosts_content = hosts.read()
            for site in sites:
                if site not in hosts_content:
                    hosts.write(redirect + " " + site + "\n")
    else:
        print("Unblock sites!")
        with open(hosts_filepath, 'r+') as hosts:
            lines = hosts.readlines()
            # Seek 0 makes the pointer start at the beginning which makes
            # the write line function overwrite the existing content. 
            # This is why there is a little snippet of the old content
            # at the end. 
            hosts.seek(0)
            for line in lines:
                # This line writes lines in the text  
                # file AFTER the default text block if a 
                # blocked website is not found in that line of the 
                # hosts.txt.
                if not any(site in line for site in sites):
                    hosts.write(line)
            # Truncate is used to return the file to its original format
            # if no parameter is given. 
            hosts.truncate()


if __name__ == '__main__':
    block()
