from src.core.event import Event

test = Event()

for x in range(1,9):
    test.add_event(f'14-2-202{x} 12:23', 'Valentine', 'dd')
