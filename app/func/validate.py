import requests
import os


def submit_to_virustotal():
    url = 'https://www.virustotal.com/api/v3/files'
    headers = {'x-apikey': '5d79ad0a589d1cc65d0223f92f2bfad6142811b60e8c3b90eb5e598aecdc291f'}
    files = {'file': open(os.getcwd() + "/../../upload_dir/8.-quadro-normativo.pdf", 'rb')}

    r = requests.post(url=url, headers=headers, files=files)
    print(r.json())


def get_virustotal_report(file_id):
    url = 'https://www.virustotal.com/api/v3/analyses/' + file_id
    headers = {'x-apikey': '5d79ad0a589d1cc65d0223f92f2bfad6142811b60e8c3b90eb5e598aecdc291f'}
    r1 = requests.get(url=url, headers=headers)
    response = r1.json()
    print(response)
    analysisTimestamp = response['data']['attributes']['date']
    analysisResult = response['data']['attributes']['result']
    analysisStats = response['data']['attributes']['stats']
    # TODO parse virus total response


if __name__ == '__main__':
    # submit_to_virustotal()
    get_virustotal_report('YWFjNzgzZTdmOWEzM2I0NTcwZDJkNWNhYmQxYmU1NDE6MTYxMzY0ODA3MQ==')
