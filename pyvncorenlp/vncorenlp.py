import json, requests

class VNCoreNLP:
    def __init__(self, server_url):
        if server_url[-1] == '/':
            server_url = server_url[:-1]
        self.server_url = server_url

    def analyze(self, text):
        assert isinstance(text, str)
        try:
            requests.get(self.server_url)
        except requests.exceptions.ConnnectionError:
            raise Exception('Check your server url')
        
        r = requests.get(self.server_url, params={ 'input': text })
        output = r.text
        try:
            output = json.loads(r.text)
            print(output)
        except:
            pass
        return output