import json
import time

import requests
from telegram.client import Telegram, AuthorizationState

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)


tg = Telegram(
    api_id=config['telegram']['api_id'],
    api_hash=config['telegram']['api_hash'],
    phone=config['telegram']['phone'],
    database_encryption_key='123',
    files_directory='tdlib_files/',
    library_path='./tdjson.dll'
)

state = tg.login(blocking=False)
if state == AuthorizationState.WAIT_CODE:
    tg.send_code(input('code: '))
    state = tg.login(blocking=False)
if state == AuthorizationState.WAIT_PASSWORD:
    tg.send_password(input('password: '))
    state = tg.login(blocking=False)
print(state)

result = tg.get_chats()
result.wait()


class Message:
    def __init__(self, chat_id, text):
        self.chat_id = chat_id
        self.text = text


messages: list[Message] = []
other_id = config['telegram']['other']
my_id = config['telegram']['self']


def message_handler(update):
    print(update)

    if (update['message']
            and update['message']['chat_id'] == other_id
            and update['message']['content']
            and not update['message']['is_outgoing']):
        # TODO handle media
        messages.append(Message(update['message']['chat_id'], update['message']['content']['text']['text']))
        tg.send_message(other_id, send_prompt(format_prompt()))


def format_prompt():
    prompt = {
        "model": config['openwebui']['model'],
        "messages": [
            {
                "role": "system",
                "content": config['openwebui']['prompt']
            }
        ]
    }
    for m in messages:
        if m.chat_id == my_id:
            author = 'assistant'
        else:
            author = 'user'

        prompt['messages'].append({
            'role': author,
            'content': m.text
        })
    return json.dumps(prompt)


def send_prompt(prompt):
    resp = requests.post(config["openwebui"]['host'] + '/api/chat/completions',
                         data=prompt,
                         headers={
                             'Authorization': f'Bearer ${config["openwebui"]["token"]}',
                             'Content-Type': 'application/json'
                         })
    print(messages)
    print(resp.json())
    resp_message = resp.json()['choices'][0]['message']['content']
    messages.append(Message(my_id, resp_message))
    time.sleep(3)
    return resp_message


send_prompt(format_prompt())
tg.add_message_handler(message_handler)
tg.idle()
