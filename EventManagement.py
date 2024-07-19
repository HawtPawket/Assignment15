# Task 2: Event Management System Enhancement

# - Problem Statement: Extend an existing Event class by adding a feature to keep track of the number of participants. 
# Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.

# - Code Example: Basic Event class without participant tracking.


class Event:
    def __init__(self, name, date):
            self.name = name
            self.date = date
            self.guests = 10

    def addGuests(self):
          self.guests += 1

    def guestsCount(self):
          print("The number of current guests is", self.guests)

event = Event("Hazels 6th Birthday party!", "10/23/2024!")
event.guestsCount()
event.addGuests()
event.guestsCount()


# used guests instead of participant to make the code look cleaner. 
