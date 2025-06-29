import json
import os
from datetime import datetime

DATA_FILE = 'events.json'

class EventManager:
    def __init__(self):
        self.events = []
        self.load_events()

    def load_events(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as file:
                self.events = json.load(file)
        else:
            self.events = []

    def save_events(self):
        with open(DATA_FILE, 'w') as file:
            json.dump(self.events, file, indent=4)

    def get_all_events(self):
        return sorted(self.events, key=lambda x: x['start_time'])

    def create_event(self, data):
        new_id = max([event['id'] for event in self.events], default=0) + 1
        event = {
            'id': new_id,
            'title': data['title'],
            'description': data['description'],
            'start_time': data['start_time'],
            'end_time': data['end_time']
        }
        self.events.append(event)
        self.save_events()
        return event

    def update_event(self, event_id, data):
        for event in self.events:
            if event['id'] == event_id:
                event.update(data)
                self.save_events()
                return event
        return {'error': 'Event not found'}

    def delete_event(self, event_id):
        self.events = [event for event in self.events if event['id'] != event_id]
        self.save_events()
        return {'message': 'Event deleted successfully'}