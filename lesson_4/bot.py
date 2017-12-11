from flask import Flask, flash, redirect, render_template, \
    request, url_for, session
import requests
import json
import apiai
import uuid


app = Flask(__name__)
app.secret_key = 'secret'

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/apiai")
def apiai_route():
    ai = apiai.ApiAI("more secret")
    request = ai.text_request()
    request.lang = 'es'  # optional, default value equal 'en'
    request.session_id = "12"
    request.query = "Hello"
    response = request.getresponse()

    print (response.read())
    return "True"

@app.route('/message', methods=['POST'])
def message():
    data = json.loads(request.data)
    message_id = data['data']['id']
    session_id = data['data']['personEmail'] + data['data']['roomId']
    room_id = data['data']['roomId']

    if data['data']['personEmail'] == 'mybot@sparkbot.io':
        return "true"

    if session_id not in session:
        session[session_id] = uuid.uuid1()
    
    headers = {'Authorization': 'Bearer evenMoreSecret'}

    data = requests.get('https://api.ciscospark.com/v1/messages/'+str(message_id), headers=headers)
    data = json.loads(data.text)
    text = data['text']


    ai = apiai.ApiAI("more secret")
    r = ai.text_request()
    r.lang = 'es'  # optional, default value equal 'en'
    r.session_id = 'asd'
    r.query = text
    response = r.getresponse()
    response = response.read()
    print(response)
    response = json.loads(response)

    if response['result']['actionIncomplete'] is False:
        if 'sw' in response['result']['parameters']:
            swtich = response['result']['parameters']['sw']
            port = response['result']['parameters']['port']

            
            swtich = swtich.replace("OSCI ", "")
            port = port.replace("OSCI ", "")

            print("sw", swtich)
            print("port", port)
            import paramiko

            ssh = paramiko.SSHClient()
            ssh.load_system_host_keys()
            ssh.set_missing_host_key_policy(paramiko.WarningPolicy())
            ssh.connect(swtich.strip(), port=22, username= "user", password= "even more secret", look_for_keys=False, allow_agent=False)
            stdin, stdout, stderr = ssh.exec_command("show interfaces " + port )
            stdout = stdout.readlines()
            txt_response = '\n'.join(stdout)
            print("stf", stdout)
            ssh.close()
        else:
            txt_response = response['result']['fulfillment']['speech']
    else:
        txt_response = response['result']['fulfillment']['speech']


    payload = {'roomId': room_id, 'text': txt_response}
    data = requests.post('https://api.ciscospark.com/v1/messages', headers=headers, data=payload)
    data = json.loads(data.text)
    print(data)

    return "true"