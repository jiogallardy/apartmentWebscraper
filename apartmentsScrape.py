from abc import ABC, abstractmethod
import PushNotifier
class ApartmentBaseScraper(ABC): 
    def __init__(self, property: str, location: str, push_notifier: PushNotifier): 
        self.property = property
        self.location = location
        self.push_notifier = push_notifier

    @abstractmethod
    def find_two_bedrooms(self): 
        pass
    @abstractmethod
    def find_arrays(self): 
        pass