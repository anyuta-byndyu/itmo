# Бындю ИСУ-502689
# вариант 9
import time,sys
BLUE = '\u001b[48;5;17m'
WHITE = '\u001b[48;5;15m'
END = '\u001b[0m'
BEGIN='\x1B[1G'
ERASE='\X1B[2K'
# код для вывода флага
'''
def flag():
    for i in range(6):
        if i in range(2,4): print(f'{BLUE}{" "*(26)}{END}') #для генерации синей горизонтальной полосы
        else: print(f'{WHITE}{" "*(6)}{BLUE}{" "*5}{WHITE}{" "*15}{END}') #все осальные строки
flag()
def loading():
    for i in range(100):
        time.sleep(0.1)
        print(f'[100DLoading...{i+1}%', end='',flush=True)
    print('Done!')

def loading_multi(num):
    bar_width=25
    for k in range(1,num+1):
        for p in range(1,bar_width+1):
            bar="#"*p+"-"*(bar_width-p)
            print(BEGIN + ERASE + "Task " + str(k) + "/" + str(num) +
                  " [" + bar + "] " + str(p * 4) + "%", end='', flush=True)
            time.sleep(0.1)
        print("Done!")
'''
#выводим узор круга разных размеров
'''
def draw_line(offset=0,length=1,color=88):
    line=' '*(length)
    a=f'{" "*offset}\x1b[48;5;{color}m{line}\x1b[0m'
    return a

def cir():
    for height in range(10,2,-2):
        color=45
        for i in range(1,height+1):
            if height//2>=i:
                print(draw_line(height+2-2*i,2*i,color)+draw_line(0,2*i,color))
            else:
                print(draw_line(2*i-height,(height+1-i)*2,color)+draw_line(0,(height+1-i)*2,color))
        print(" ")
        time.sleep(1)
cir()
'''
#функция y=x/2
'''
def draw_dot(offset=0,symbol="/"):
    a=f'{"  "*offset}{symbol}'
    return a
def func():
    symbol="*"
    height=19
    for i in range(height+1):
        print((height-i)/2,draw_dot(height+1-i,symbol))
    print(" "*6+" ".join([str(i) for i in range(height+1)]))
func()
'''
#диаграмма
file = open("17.txt","r")
'''
a=[float(i) for i in file] #генератор списка. считывает все числа и переводит их из str во float
list_negative = len([i for i in a if -10<=i<=-5]) # генератор списка проходит по всем занчениям файла и выбирает те, что удовлетворяют -10<=i<=-5
list_positive=len([i for i in a if 5<=i<=10])
list_all=len([i for i in a if -10<=i<=-5 or 5<=i<=10])# все числа из нужного диапозона
ratio_negative= (list_negative)*10/list_all
ratio_positive= (list_positive)*10/list_all
def diagram():
    color=90
    for i in range(10*2+1): #так как 100% это максимум, чтобы добиться более точной диаграммы будем выводить не целые числа а с шагом 0.5 для этого 10*2
        point_positive =''
        point_negative=''
        line=' '*2
        if (20-i)/2<=ratio_negative: point_negative = f'{" "*8}\x1b[48;5;{color}m{line}\x1b[0m'
        if (20 - i) / 2 <= ratio_positive: point_positive = f'{" "*8}\x1b[48;5;{color}m{line}\x1b[0m' #выводим столбцы соответсвующие количественному соотношению чисел из диапазона 5<=i<=10 к числам из -10<=i<=-5 and 5<=i<=10
        print((20-i)/2,point_positive,point_negative)
    print('числа от'+' '*2+'5<=i<=10'+' '*2+'-10<=i<=-5')
diagram()
'''

#допзадание
'''
def loading():
    print('loading...')
    for i in range(100):
        time.sleep(0.1)
        line=(i+1)
        #print(f'{"["} \x1b[48;5;90m{" "*(i+1)}\x1b[0m {"]"}', end='', flush=True)
        bar="["+f'\x1b[48;5;90m{" "*line}\x1b[0m'+"]"
        sys.stdout.write(u'\u001b[1000D'+bar)
        sys.stdout.flush()
    print(' Done!')

loading()'''
