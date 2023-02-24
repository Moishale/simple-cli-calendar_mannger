import sqlite3


class Event:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            with sqlite3.connect('data/calendar.db') as conn:
                c = conn.cursor()
                c.execute('CREATE TABLE IF NOT EXISTS EVENTS(event TEXT NOT NULL, description TEXT, date TEXT NOT NULL)')
        return cls.__instance

    def add_event(self, datetime, event, description):
        with sqlite3.connect('data/calendar.db') as conn:
            c = conn.cursor()
            c.execute('INSERT INTO events (event, description, date) VALUES (?, ?, ?)', (event, description, datetime))

    def view_events(self):
        with sqlite3.connect('data/calendar.db') as conn:
            c = conn.cursor()
            events = c.execute(f'SELECT * FROM events').fetchall()
        return events

    def delete_event(self, datetime):
        with sqlite3.connect('data/calendar.db') as conn:
            c = conn.cursor()
            c.execute(f'DELETE FROM events WHERE date = "{datetime}";')

    def extract_datetimes(self):
        with sqlite3.connect('data/calendar.db') as conn:
            c = conn.cursor()
            datetimes = c.execute('SELECT date from users').fetchall()
            return datetimes
