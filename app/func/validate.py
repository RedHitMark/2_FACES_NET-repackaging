import requests
import os


def submit_to_virustotal():
    url = 'https://www.virustotal.com/api/v3/files'
    headers = {'x-apikey': os.getenv("VIRUS_TOTAL_API")}
    files = {'file': open(os.getcwd() + "/../../upload_dir/test.apk", 'rb')}

    r = requests.post(url=url, headers=headers, files=files)
    print(r.json())


def get_virustotal_report(file_id):
    url = 'https://www.virustotal.com/api/v3/analyses/' + file_id
    headers = {'x-apikey': os.getenv("VIRUS_TOTAL_API")}
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
