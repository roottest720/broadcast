import requests

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot_token = '6673598316:AAEGW38a7chRpOmlFmYGPpK4I6TVbOUDMf0'
chat_id = '5113588348'  # Replace with the chat ID of the user or group you want to send the message to

# Replace 'Your message here' with the actual message you want to send
# message_text = 'Hello from python'

# # Telegram Bot API endpoint for sending messages
api_url = f'https://api.telegram.org/bot{bot_token}/sendChatAction'

# # Parameters for the API request


# Make the API request
# response = requests.get(api_url, params=params)

# Print the response from the Telegram API
response1 = requests.get(f'https://bots.darksyker.fun/kiara_bot/broadcast/all_users.php')
# print(response1.json()["response_code
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
