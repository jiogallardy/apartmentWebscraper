class Subscription:
    """
     Class for subscriptions
    """    

    def __init__(self): 
        self.subscribers = []
  
    def add_subscriber(self, subscriber): 
        """
        add_subscriber _summary_

        :param subscriber: _description_
        :type subscriber: _type_
        """        
        self.subscribers = {}

    def remove_subscriber(self, user_key:str): 
        """
        remove_subscriber removes a subscriber by key 

        :param user_key: _description_
        :type user_key: str
        """        
        if user_key in self.subscribers: 
            del self.subscribers[user_key]
    def get_subscriber(self, user_key): 
        return self.subscribers.get(user_key, None)
    
    def get_active_subscribers(self, )
    

