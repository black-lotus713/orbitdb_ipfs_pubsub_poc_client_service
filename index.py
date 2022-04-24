import requests
import json
import time
import os

path = os.getcwd()
logfile = path + os.path.sep + 'pinlog.txt'

def main():
    pinlog = []
    newlog = []

    #persistent means of avoiding duplicate pinning
    with open(logfile, 'r') as l:
        print('file opened')
        for line in l.readlines():
            pinlog.append(line)
    print(pinlog)

    #point to orbitdb instance
    r = requests.get('http://localhost:8080/list')

    response = json.loads(r.content)

    hash_list = response['Hash List']

    for hash in hash_list:
        match = False
        for pin in pinlog:
            if hash["content"] in pin:
                match = True

        if match == False:
            print(f"Calling IPFS API to pin: {hash['title']}")

            #point to ipfs node
            p = requests.post(f'http://localhost:5001/api/v0/pin/add?arg={hash["content"]}')

            print(p.content)
            newlog.append(f"{hash['title']} - {hash['content']}\n")

    with open(logfile, 'a') as a:
        for item in newlog:
            a.write(item)


open(logfile, 'a').close()

while True:
    main()
    #this was built with a content creator in mind that
    #only posts once a week so checking more than once
    #a day is aggressive but wasn't sure how it would
    #work or not work with such a long sleep interval
    time.sleep(43200)
