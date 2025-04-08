def day_of_week(day):
    match day:
        case 1:
            return 'Monday'
        case 2:
            return 'Tuesday'
        case 3:
            return 'Wednesday'
        case 4:
            return 'Thirsday'
        case 5:
            return 'Friday'
        case 6:
            return 'Saturday'
        case 7:
            return 'Sunday'
        case _:
            return 'There is only 7 days in week'
        
def is_weekend(day):
    match day:
        case 'Monday' | 'Tuesday' | 'Wednesday' | 'Thirsday' | 'Friday':
            return False
        case 'Saturday' | 'Sunday':
            return False
        case _:
            return 'Unknown day'
        

        
while True:
    try:
        user_input = int(input('Enter number of week day: '))
        print(day_of_week(user_input))
        break
    except ValueError:
        print("Invalid input! Please enter a number.")