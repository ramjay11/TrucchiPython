import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Indovina un numero compreso tra 1 e {x}: '))
        if guess < random_number:
            print('Scusa, indovina di nuovo. Numero troppo basso')
        elif guess > random_number:
            print('Scusa, indovina di nuovo. Numero troppo alto')
    print(f'Sì, hai indovinato il numero {random_number} correttamente!')

# Il computer indovinerà il numero
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low    
        feedback = input(f'È {guess} troppo alto (H), troppo basso (L) o corretto (C)? ').lower()
        if feedback == 'h':
            h = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Sì, il computer ha indovinato il tuo numero, {guess}, correttamente!')            

computer_guess(11)
# guess(11)