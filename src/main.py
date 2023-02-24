from core.calendar import Calendar

def main():
    calendar = Calendar()

    while True:
        print('1. Create new event')
        print('2. View events')
        print('3. Remove event')
        print('4. Show daily events')
        print('0. Exit')

        choice = input('Enter your choice: ')
        if choice == '0':
            break
        elif choice == '1':
            datetime_str = input('Enter the date and time of the event (DD-MM-YYYY HH:MM): ')
            event_name = input('Enter the name of the event: ')
            description_choice = input('Do you want to set a description for this event? (y/n): ')
            if description_choice.lower() == 'y':
                event_description = input('Enter the description for the event: ')
            else:
                event_description = None
            calendar.create_event(datetime_str, event_name, event_description)
        elif choice == '2':
            calendar.view_events()
        elif choice == '3':
            calendar.remove_event()
        elif choice == '5':
            calendar.show_daily_events()
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()