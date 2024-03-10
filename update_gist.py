import requests
import json

gist_id = 'gist_id'
filename = 'filename.py'
new_code = 'your updated code here'

url = f'https://api.github.com/gists/{gist_id}'
payload = {
    'files': {
        filename: {
            'content': new_code
        }
    }
}
headers = {'Authorization': 'Bearer YOUR_ACCESS_TOKEN'}

response = requests.patch(url, headers=headers, data=json.dumps(payload))
