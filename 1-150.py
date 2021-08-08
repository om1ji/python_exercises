from types import resolve_bases


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

def twenty_nine(list1: set, list2: set): print(list1.difference(list2))

# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])

def thirty(base, height): print(0.5*base*height)

def thirty_one(a: int, b: int):
    from math import gcd
    print(gcd(a,b))

def thirty_two(a: int, b:int):
    from math import gcd
    print(abs(a,b)//gcd(a,b))

def thirty_three(a: int, b: int, c:int):
    if len(set([a,b,c]))>3: print('0')
    else: print(a+b+c)
