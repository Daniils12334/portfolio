import random

def spin_row():
    symbols = ['🐇','🐁','🐹','🐒','🐷']
    # result = []
    # for symbol in range(3):
        # result.append(random.choice(symbols))
    # return result

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print('**************') 
    print(' | '.join(row))
    print('**************')

def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🐇':
            return bet * 3
        elif row[0] == '🐁':
            return bet * 4
        elif row[0] == '🐹':
            return bet * 5
        elif row[0] == '🐒':
            return bet * 0.5
        else:
            return bet * 7
    return 0
    

def main():
    balance = 100

    print('***********************')
    print('Welcome to Cacawa slots')
    print('***********************')

    while balance > 0:
        print(f'Current balance: {balance}$')

        bet = input('Place your bet amount: ')

        if not bet.isdigit():
            print('Please enter a valid number: ')
            continue

        bet = int(bet)

        if bet > balance:
            print('Insufficent funds! ')
            continue
        if bet <= 0:
            print('Bet must be greater then 0: ')
            continue

        balance -= bet

        row = spin_row()
        print('spinning...\n')
        print_row(row)

        payout = get_payout(row,bet)

        if payout > 0:
            print(f"You won {payout}$")
        else:
            print("Sorry, you lost")
        balance += payout

        play_again = input('Do you want to spin again? (Y/N): ').upper
        if play_again != 'Y':
            break
    print('*******************************************')
    print("Game over! Your final balance is {balance}$")
    print('*******************************************')

if __name__ == '__main__':
    main()
