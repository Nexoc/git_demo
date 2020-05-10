import random as r

n = r.randint(1, 100)
user_num = 0
cnt = 0
name = input('Geben Sie Ihren Namen ein ')

while True:
    try:
        user_num = int(input('Ich habe ein Zahl von 1 bis 100 gemacht, rate mal: '))
        cnt += 1
        if user_num == n:
            print(f'Ja!!! Sie haben die Zahl in {cnt} Versuchen erraten! Vielen Dank für das Spiel, '+name)
            if input('Möchten Sie noch ein mal spielen? j|n ') == 'j':
                n = r.randint(1, 100)
                cnt = 0

            else:
                break
        elif user_num > n:
                print('Meine Nummer ist weniger')
        else:
                print('Meiner Nummer ist großer')
    except ValueError:
        print('Muss ein Zahl sein')


print(f'Danke.Auf wieder sehen')
