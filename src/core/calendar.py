from datetime import datetime

from core.event import Event
from core.date import is_valid_datetime, get_year_from_datetime, is_valid_year, parse_datetime

from prettytable import PrettyTable


class EventsIterator:
    def __init__(self, events):
        self.events = events
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.events):
            raise StopIteration

        event, event_description, date = self.events[self.index]
        self.index += 1
        return event, event_description, date


class Calendar:
    def __init__(self):
        self.event = Event()

    def create_event(self, datetime_str, event_name, event_description=None):
        if not is_valid_datetime(datetime_str):
            print('Invalid datetime format')
            return

        year = get_year_from_datetime(datetime_str)
        if not is_valid_year(year):
            print('Invalid year')
            return

        self.event.add_event(datetime_str, event_name, event_description)
        print('Event created successfully')

    def remove_event(self):
        events = list(self.events_iterator())

        table = PrettyTable(
            field_names=['Event Number', 'Event', 'Description', 'Date'])
        for i, (event, description, date) in enumerate(events):
            table.add_row([i+1, event, description, date])

        print(table)
        choice = int(input('Choose event number:'))

        try:
            event, description, date = events[choice-1]
            self.event.delete_event(date)
            print('Event removed successfully')
        except IndexError:
            print('Invalid choice')

    def show_daily_events(self):
        events = list(self.events_iterator())

        table = PrettyTable(
            field_names=['Event Number', 'Event', 'Description', 'Date'])
        for i, (event, description, date) in enumerate(events):
            past_event_date = parse_datetime(date)
            current_date = parse_datetime(str(datetime.now()))

            if past_event_date == current_date:
                table.add_row([i+1, event, description, date])
        print(table)

    def view_events(self):
        events = self.event.view_events()

        collection = []
        for i, (event, event_description, date) in enumerate(events):
            collection.append([i+1, event, event_description, date])

        table = PrettyTable(
            field_names=['Event Number', 'Event', 'Description', 'Date']
        )
        table.add_rows(collection)

        print(table)

    def events_iterator(self):
        events = self.event.view_events()
        return EventsIterator(events)
