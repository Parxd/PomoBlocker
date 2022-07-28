def block(sites):
    hosts = 'C:\\Windows\\System32\\Drivers\\etc\\hosts'
    with open(hosts, 'r+') as hosts:
        hosts_content = hosts.read()
        for site in sites:
            if site not in hosts_content:
                hosts.write("0.0.0.0 " + site + "\n")


def unblock(sites):
    hosts = 'C:\\Windows\\System32\\Drivers\\etc\\hosts'
    with open(hosts, 'r+') as hosts:
        lines = hosts.readlines()
        # Seek 0 makes the pointer start at the beginning which allows overwriting the existing content.
        hosts.seek(0)
        for line in lines:
            if not any(site in line for site in sites):
                hosts.write(line)
        hosts.truncate()

