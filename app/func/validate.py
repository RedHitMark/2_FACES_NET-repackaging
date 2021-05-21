import requests
import os


def submit_to_virustotal(sha1_hash):
    url = 'https://www.virustotal.com/api/v3/files'
    headers = {'x-apikey': os.getenv('VIRUS_TOTAL_API')}
    files = {'file': open(os.getcwd() + "/upload_dir/" + sha1_hash + ".apk", 'rb')}

    r = requests.post(url=url, headers=headers, files=files)
    print(r.json())
    return r.json()


def froce_virustotal(sha1_hash):
    url = 'https://www.virustotal.com/api/v3/files/' + sha1_hash + "/analyse"
    headers = {'x-apikey': os.getenv('VIRUS_TOTAL_API')}

    r = requests.get(url=url, headers=headers)
    print(r.json())
    return r.json()


def get_virustotal_report(sha1_hash):
    url = 'https://www.virustotal.com/api/v3/files/' + sha1_hash
    headers = {'x-apikey': os.getenv('VIRUS_TOTAL_API')}
    r1 = requests.get(url=url, headers=headers)
    response = r1.json()
    print(response)
    # analysisTimestamp = response['data']['attributes']['date']
    # analysisResult = response['data']['attributes']['result']
    # analysisStats = response['data']['attributes']['stats']
    return response
    # TODO parse virus total response
