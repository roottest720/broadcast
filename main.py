from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Define a simple route for handling GET requests
def hello():
    return 'Hello, World!'
@app.route('/broadcast', methods=['GET'])
def get_data():
    bot_token = '6673598316:AAEGW38a7chRpOmlFmYGPpK4I6TVbOUDMf0'
    chat_id = '5113588348'
    api_url = f'https://api.telegram.org/bot{bot_token}/sendChatAction'
    response1 = requests.get(f'https://bots.darksyker.fun/kiara_bot/broadcast/all_users.php')
    if response1.json()["response_code"] == 200:
        all_users = response1.json()["all_users"]
        alive_users = 0
        dead_users = 0
        i = 0
        api_url1 = f'https://api.telegram.org/bot{bot_token}/sendMessage'
        params = {'chat_id': chat_id, 'text': f"Broadcast started from py"}
        response = requests.get(api_url1, params=params)
        for user in all_users:
            params = {'chat_id': user, 'action': "typing"}
            response = requests.get(api_url, params=params)
            if response.json()["ok"] == True:
                alive_users += 1
            else:
                dead_users += 1
            i+=1
            if i % 100 == 0:
                api_url1 = f'https://api.telegram.org/bot{bot_token}/sendMessage'
                params = {'chat_id': chat_id, 'text': f"Alive users: {alive_users}\nDead users: {dead_users}\nTotal users checked: {i}"}
                response = requests.get(api_url1, params=params)
    api_url1 = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    params = {'chat_id': chat_id, 'text': f"Broadcast done!\nAlive users: {alive_users}\nDead users: {dead_users}\nTotal users checked: {i}"}
    response = requests.get(api_url1, params=params)
    return jsonify(data)

if __name__ == '__main__':
    app.run()
