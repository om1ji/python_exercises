def one():
    text = 'Twinkle, twinkle, little star, \n\tHow I wonder what you are!\n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are'

    output = """

    Twinkle, twinkle, little star,
        How I wonder what you are! 
            Up above the world so high,   		
            Like a diamond in the sky. 
    Twinkle, twinkle, little star, 
        How I wonder what you are
        
        """

    print(text)

def two():
    import sys
    print(sys.version)

def three():
    import datetime
    print('Current date and time:\n' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%Ss'))

def four():
    from math import pi
    r = float(input('r: '))
    print('Area: ' + str((pi * r**2)))

def five():
    first = input('First: ')
    second = input('Second: ')
    print(second, first, sep=' ')

def six():
    data = input('Values: ').split(', ')

    print(data, tuple(data))

def seven():
    print(input('Filename: ').split('.')[1])

def eight():
    color_list = ["Red","Green","White" ,"Black"]
    print(color_list[0], color_list[-1])

def nine():
    exam_date = (11, 12, 2014)
    output = ''
    for i in exam_date:
        output += str(i) + '/'
    print('The examination will start from: ' + output)

def ten():
    n = str(input('N: '))
    print(int(n) + int(n+n) + int(n+n+n))

def eleven():
    print(abs.__doc__)

def twelve():
    import calendar
    m, y = int(input('Month: ')), int(input('Year: '))
    print(calendar.month(y, m))

def thirteen():
    pass

def fourteen():
    from datetime import date
    date1 = date(int(input('Year: ')), int(input('Month: ')), int(input('Day: ')))
    date2 = date(int(input('Year: ')), int(input('Month: ')), int(input('Day: ')))
    print((date2-date1).days + 'days')

def fifteen():
    # 4/3 πr³
    from math import pi
    print(4/3*pi*int(input('Radius: '))**3)

def sixteen():
    a = int(input('Number: '))
    if a > 17: print(a*2)
    else: print(17-a)

def seventeen():
    a = int(input('Number: '))
    print(100 <= a <= 1000 or 100 <= a <= 2000)

def eighteen(a, b, c):
    if a == b == c: print(3*a)
    else: print(a+b+c)

def nineteen(string):
    if string.startswith('ls'): print(string)
    else: print('ls'+string)

def twenty(string, n): 
    if n > 0: print(string*n)

def twenty_one():
    a = int(input('Accept from the user: '))
    if a % 2 == 0: print('Even')
    else: print('Odd')

def twenty_two():
    bruh = input('List: ').split(', ')
    counter = 0
    for item in bruh: 
        if item == '4': counter += 1
    print(counter)

def twenty_three(string, n):
    if len(string) < 2: print(string*n)
    else: print(string[:2]*n)

def twenty_four(letter: str):
    vowels = ['a', 'o', 'u', 'e', 'i']
    if letter.lower() in vowels: print('Vowel')
    else: print('Not Vowel')

def twenty_five(value, values):
    if value in values: print('Bruh')
    else: print('Not Bruh :((')

def twenty_six(values: list): 
    for i in values: print('bruh '*i)

def twenty_seven(list: list):
    bruh = ''
    for i in list:
        bruh += str(i)
    print(bruh)

def twenty_eight(numbers: list):
    for i in numbers:
        if i == 237: 
            break
        elif i % 2 == 0: print(i)

def twenty_nine(list1: set, list2: set): 
    print(list1.difference(list2))

def thirty(base, height): 
    print(0.5*base*height)

def thirty_one(a: int, b: int):
    from math import gcd
    print(gcd(a,b))

def thirty_two(a: int, b:int):
    from math import gcd
    print(abs(a,b)//gcd(a,b))

def thirty_three(a: int, b: int, c: int):
    if len(set([a,b,c]))>3: print('0')
    else: print(a+b+c)

def thirty_four(a: int, b:int):
    if 15 <= (a + b) <= 20: print(20)
    else: print(a + b)

def thirty_five(a: int, b: int):
    if a == b or a + b == 5 or b - a == 5: print(1)

def thirty_six(a: int, b: int) -> int:
    if isinstance(a, int) and isinstance(b, int): print(a+b)

def thirty_seven(name, age, address): 
    print(name, age, address, sep='\n')

def thirty_eight(x: int, y: int) -> int: 
    print((x+y)**2)

def thirty_nine(amt, int, years):
    r = amt*((1+(0.01*int)) ** years)
    print(round(r, 2))

def fourty(x1, y1, x2, y2): 
    print(x2-x1, y2-y1, sep=' ')

def fourty_one(path):
    from os.path import exists
    print(exists(path))

def fourty_two():
    import platform
    print(platform.architecture()[0])

def fourty_three():
    import os, platform
    print(os.name, platform.system(), platform.release(), sep='\n')

def fourty_four():
    import site
    print(site.getsitepackages())

def fourty_five(cmd):
    import os
    os.system(cmd)

def fourty_six():
    from os.path import realpath
    print(realpath(__file__))

def fourty_seven():
    import multiprocessing as m
    print(m.cpu_count())

def fourty_eight(string, *args):
    if 'float' in args: print(float(string))
    elif 'integer' in args: print(int(string))

def fourty_nine():
    from os import listdir
    print(listdir())

def fifty():
    pass

def fifty_one(func: str):
    import cProfile
    cProfile.run(f'{func}')

def fifty_two():
    import sys

    def eprint(*args, **kwargs):
        print(*args, file=sys.stderr, **kwargs)

    eprint("abc", "efg", "xyz", sep="--")

def fifty_three(var_name):
    from os import getenv
    print(getenv(var_name).split(';'))

def fifty_four():
    from getpass import getuser
    print(getuser())

def fifty_five():
    import socket # Не сам
    print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] 
    if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), 
    s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])

def fifty_six():
    import fcntl, termios, struct # Не сам
    th, tw = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))

    print('Number of columns and Rows: ', tw, th, sep=' ')

def fifty_seven():
    from time import time
    time1 = time()
    bruh = 2**2**2**2**2
    time2 = time()
    print(bruh, time2-time1)

def fifty_eight(n):
    bruh = 0
    for i in range(n):
        bruh += i
    print(bruh)

def fifty_nine(foot, inches):
    print(foot*30.48 + inches*2.54)

def sixty(katet1, katet2):
    from math import sqrt
    hypotenuse = sqrt(katet1**2 + katet2**2)
    print(round(hypotenuse, 2))

def sixty_one(feet):
    print(feet*12)
    print(feet/3)
    print(feet/5280)

def sixty_two():
    pass

def sixty_three(path):
    from os.path import abspath
    print(abspath(path)) 

def sixty_four():
    pass

def sixty_five(seconds: int):
    days = seconds // (24*3600)
    hours = (seconds // 3600) % 24
    minutes = (seconds // 60) % 60
    seconds = seconds % 60
    print(days, hours, minutes, seconds, sep=' ')

def sixty_six(kg, m: float):
    print(round(kg/m**2, 1))

