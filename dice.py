from random import randint
from colorama import init, Fore
from colorama import Back
from colorama import Style

init(autoreset=True)

def dice():
    random_num = randint(1, 6)
    num = randint(1,6)

    print(Fore.YELLOW + 'Чтобы закончить нажмите Ctrl + C')
    input('Чтобы кинуть кубик, нажмите ENTER')
    
    if num > random_num:
        print()
        print(Fore.MAGENTA + 'У компьютера выпало: ' , str(random_num), Fore.MAGENTA + ',а у вас: ', str(num))
        print(Fore.GREEN + 'Поздравляю, вы выграли!')
        print()
    elif num == random_num:
        print()
        print(Fore.MAGENTA + 'У компьютера и у вас выпало: ' , str(num))
        print(Fore.WHITE + 'Похоже это ничья!')
        print()
    else:
        print()
        print(Fore.MAGENTA + 'У компьютера выпало: ' , str(random_num) , Fore.MAGENTA + ' ,а у вас: ' , str(num))
        print(Fore.RED + 'Похоже, вы проиграли!')
        print()

while True:
    dice()
