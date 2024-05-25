import requests
from bs4 import BeautifulSoup
import re
from pushNotifier import PushNotifier
import time
from datetime import datetime, timedelta

class WebScraper:
    def __init__(self, webSite: str, siteName: str):
        self.siteName = siteName
        self.webSite = webSite
        self.previousCount = None

    def findAvailableTwoBeds(self):
        response = requests.get(self.webSite)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        unit_divs = soup.find_all('div', class_='unit-expanded-card')
        apartments = []

        for unit in unit_divs:
            specs = unit.find('div', class_='specs')
            details = specs.find_all('p')

            if '2 Bed' in details[1].text:
                floor_plan_raw = unit.find('div', class_='floorplan').find('img')['alt']
                floor_plan = re.search(r'(\d Bedrooms\s)([A-Z])', floor_plan_raw)
                floor_plan = floor_plan.group(2) if floor_plan else 'Unknown'
                price = specs.find('span', class_='pricing').text.strip() if specs.find('span', class_='pricing') else 'N/A'
                floor = details[2].text.split('/')[-1].strip()
                floor_number = int(floor.split(' ')[1])
                availability = details[3].text.strip()
                # Assume room number extraction is added here

                apartments.append({
                    'price': price,
                    'floor': floor_number,
                    'available': availability,
                    'floor_plan': floor_plan,
                })

        return apartments

    def findAboveAFloor(self, floor: int) -> list:
        apartments = self.findAvailableTwoBeds()
        aboveFloor = []
        for room in apartments:
            if room['floor'] > floor:
                aboveFloor.append(room)
        return aboveFloor
    
    def monitorChangesOnSetRange(self, floor: int, pushNotifier: PushNotifier):
        # Run for two weeks and then shut off 
        start_time = datetime.now()
        two_weeks = timedelta(weeks=2)


        while datetime.now() - start_time < two_weeks: 
            aboveFloor = self.findAboveAFloor(floor)

            floorAmounts = len(aboveFloor)
            if self.previousCount is not None and floorAmounts != self.previousCount: 
                pushNotifier.send_single_notification(f'Change detected in amount of apartments, apartments list is now {aboveFloor}' )
            self.previousCount = floorAmounts
            time.sleep(300)


    



                


