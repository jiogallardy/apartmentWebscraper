from abc import ABC
from abc import abstractmethod

class baseSubscriber(ABC): 
    def __init__(self): 
        pass
    @abstractmethod
    def subscribe(self): 
        pass
    @abstractmethod
    def unsubscribe(self): 
        pass
    @abstractmethod
    def listSubscriptions(self): 
        pass
    
class PaidSubscriber(baseSubscriber): 
    def __init__(): 
        pass

class UnpaidSubscriber(baseSubscriber): 
    def __init__(): 
        super.__base__
        pass

class PushOverSubscriber(UnpaidSubscriber): 
    def __init__(self, user_key: str): 
        self.user_key = user_key




