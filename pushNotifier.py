import requests
import certifi
import schedule
import time
from functools import partial

class PushNotifier: 
    def __init__(self, api_token: str, user_key: str): 
        self.api_token = api_token
        self.user_key = user_key

    def send_single_notification(self, message: str):    
        """
        Send a single notification to a user.

        :param user_key: The user's key
        :type user_key: str
        :param message: The message to send
        :type message: str
        :return: The response from the API call
        """        
        url = 'https://api.pushover.net/1/messages.json'
        payload = {
            'token': self.api_token,
            'user': self.user_key,
            'message': str(message)
        }
            
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(url, data=payload, headers=headers, verify=certifi.where())

        return response.json()

    def send_to_subscribers(self, subscribers, message: str): 
        """
        Send a notification to all subscribers.

        :param subscribers: A list of subscribers
        :type subscribers: list
        :param message: The message to send
        :type message: str
        """        
        for subscriber in subscribers:
            self.send_single_notification(subscriber.user_key, message)


    def send_message_at_interval(self, interval: int, message: str):
        """
        Set up a scheduled job to send messages at specified intervals.

        :param interval: Interval in hours
        :param message: Message to send
        """
        schedule.every(interval).hours.do(partial(self.send_single_notification, message))
    
    def run(self):
        # This method starts the scheduler to run indefinitely
        while True:
            schedule.run_pending()
            time.sleep(10)
