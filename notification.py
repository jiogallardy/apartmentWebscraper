import requests
import certifi


class notitic
def send_pushover_notification(user_key, api_token, message):
    url = 'https://api.pushover.net/1/messages.json'
    payload = {
        'token': api_token,
        'user': user_key,
        'message': message
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    
    # Sending the POST request with SSL certificate verification enabled
    response = requests.post(url, data=payload, headers=headers, verify=certifi.where())
    
    return response.json()  # Return the JSON response from Pushover

# Example usage
api_token = 'a6v5rk5g8j3hi9x84axhkupojc5msf'  # Your API Token
user_key = 'ujw4rnukf4xtr8bq81gapwc13brdqd'  # Your User Key
message = 'Damn daniel is so sexy !'

response = send_pushover_notification(user_key, api_token, message)
print(response)
