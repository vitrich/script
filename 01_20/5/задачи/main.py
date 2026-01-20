from random import randint, shuffle, sample,choice
from math import *

f = open('tasks.tex', 'w')
f.write('')
f = open('tasks.tex', 'a')
n=2
fAnsw=''
title='Разложение на множители'

frame='(18,4)'    

vitrich5 = [
   "Рыльской Эвилины Ильгамовны",
   "Абелюк Марии",   
   "Гондарева Ильи",
   "Аношина Матвея Антоновича",
   "Егоровой Мирославы Даниловны",
   "Карнауха Тимофея Павловича",
   
   "Костенко Каролины Романовны",
   "Минца Марка Евгеньевича",
   
   "Саргсян Эмилии Арамовны",
   "Строкатовой Киры Павловны",
   "Тавриной Марии Ивановны"    
]
vitrich4 = [

   "Александровой Ксении Андреевны",
   "Баумгертнер Елизаветы Владиславовны",
   "Гайдадиной Анны Алексеевны",
   "Гринчук Арины",
   "Ермолаевой Софии",
   "Икаева Руслана Алановича",
   "Ильиной Софии Антоновны",
   "Кострицкой Есении Ивановны",
   "Купцова Даниила Андреевича",
   "Лукашовой Мирославы Евгеньевны",
   "Мухаметшиной Алисы Рифатовны",
   "Нижегородова Даниила Кирилловича",
   "Поландова Максима Ивановича",
   "Поповой Ульяны Дмитриевны",
   "Тильдикова Ярослава Александровича",
   "Топчиева Аарона Рустамовича"
]

names=vitrich5


def find_common_divisors(a, b):
   # Находим все делители первого числа
   divisors_a = [i for i in range(1, a + 1) if a % i == 0]
   # Находим все делители второго числа
   divisors_b = [i for i in range(1, b + 1) if b % i == 0]
   # Находим пересечение множеств
   common_divisors = list(set(divisors_a) & set(divisors_b))
   return common_divisors
def fac(n):   
   i = 2
   s=set()
   while n > 1:
      while n % i == 0:
         s.add(i)
         n //= i
      i += 1
   return s

def prime_factors(n):
   factors = []
   i = 2
   while i * i <= n:
      while n % i == 0:
         factors.append(i)
         n = n // i
      i += 1
   if n > 1:
      factors.append(n)
   return factors

for j in names:   
   
   begin="\\subsection*{Вариант "+str(names.index(j)+1)+' для  '+j+". "+title+" \\\\ \\today   \\currenttime} \n  \\begin{enumerate}\n"
   s=""
   e1=[]
   tasksL=[]   
         
   for i in range(n):            
      a=[randint(0,4),randint(0,3),randint(0,1),choice([1,7,11,13,17,19,23])]
      b=[randint(0,4),randint(0,3),randint(0,1)]
      c=2**a[0]*3**a[1]*5**a[2]*a[3]
      d=2**b[0]*3**b[1]*5**b[2]   
      
         
             
      s='\\item Делится ли $'+'2\\cdot'*(a[0]+b[0])+'3\\cdot'*(a[1]+b[1])+'5\\cdot'*(a[2]+b[2])+' '+str(a[3])+'$ на $'+'2\\cdot'*(b[0])+'3\\cdot'*(b[1])+'5\\cdot'*(b[2])+' 1$? Если да, запишите разложение на простые множители частного. \\nopagebreak \\\\* \\begin{tikzpicture}\n \\draw[step=0.5cm,gray,very thin] (0,0) grid'+frame+';\n % Обводка внешнего контура  \\draw[black, thick] (0,0) rectangle '+frame+';\n \\end{tikzpicture}'
      ans='\\item $'+a[0]*'2\\cdot'+'3\\cdot'*(a[1])+' 5\\cdot'*(a[2])+' '+str(a[3])+'$\n'
      ar=[a,b,c,d,s,ans]
      e1.append(ar)   
      
   for i in range(n):
      a=[randint(1,2),randint(0,1),randint(0,1),choice([1,7])]
      b=[randint(0,2),randint(1,2),randint(0,1),choice([1,7])]
      c=2**a[0]*3**a[1]*5**a[2]*a[3]
      d=2**b[0]*3**b[1]*5**b[2]*b[3]  
      
      e=gcd(d, c)           
      s='\\item Найди наибольший общий делитель и наименьшее обще кратное чисел  '+str(c)+'  и  '+str(d)+'  \\\\ \\begin{tikzpicture}\n \\draw[step=0.5cm,gray,very thin] (0,0) grid'+frame+';\n % Обводка внешнего контура  \\draw[black, thick] (0,0) rectangle '+frame+';\n \\end{tikzpicture}'
      ans='   \\item НОД $'+str(e)+'$ НОК $'+str(lcm(c,d))+"$\n"
      ar=[a,b,c,d,s,ans]
      e1.append(ar)    
   
        
   
   end="\\end{enumerate}  \n\\newpage\n"
   answ='\\subsection*{Ответы. В '+str(names.index(j)+1)+'.  \\\\ \\today   \\\\ \\currenttime}   \n\\begin{enumerate}\n'
   
   
   #shuffle(e1)
   s=""
   
   for i in e1:
      s+=i[4]
      answ+=i[5]
      
   answ+='\\end{enumerate}\n'
   
   f.write(begin+s+end)
   fAnsw+=answ
f.close()
f = open('answ.tex', 'w')
f.write(fAnsw)
f.close()