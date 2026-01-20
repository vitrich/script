import os
from random import randint, shuffle

# Папка, где лежит этот скрипт
base_dir = os.path.dirname(os.path.abspath(__file__))
tasks_path = os.path.join(base_dir, "tasks.tex")
answ_path = os.path.join(base_dir, "answ.tex")

n = 1
fAnsw = ""
title = "Дроби"
st = "0.7cm "
rect = "(18,6)"

vitrich5 = [
    "Рыльской Эвилины Ильгамовны",
    "Абелюк Марии",
    "Гондарева Ильи",
    "Аношина Матвея Антоновича",
    "Егоровой Мирославы Даниловны",
    "Карнауха Тимофея Павловича",
    "Костенко Каролины Романовны",
    "Минца Марка Евгеньевича",
    "Полякова Никиты",
    "Саргсян Эмилии Арамовны",
    "Строкатовой Киры Павловны",
    "Тавриной Марии Ивановны",
]

vitrich4 = [
    "Каниной Агнии",
    "Спицына Марка",
    "Александровой Ксении Андреевны",
    "Баумгертнер Елизаветы Владиславовны",
    "Гайдадиной Анны Алексеевны",
    "Гринчук Арины",
    "Ермолаевой Софии",
    "Икаева Руслана Алановича",
    "Кострицкой Есении Ивановны",
    "Купцова Даниила Андреевича",
    "Лукашовой Мирославы Евгеньевны",
    "Мухаметшиной Алисы Рифатовны",
    "Нижегородова Даниила Кирилловича",
    "Поландова Максима Ивановича",
    "Поповой Ульяны Дмитриевны",
    "Тильдикова Ярослава Александровича",
    "Топчиева Аарона Рустамовича",
]

names = vitrich5

with open(tasks_path, "w", encoding="utf-8") as f:
    for j in names:
        begin = (
            "\\subsection*{Вариант "
            + str(names.index(j) + 1)
            + " для  "
            + j
            + ". "
            + title
            + " \\\\ \\today   \\currenttime} \n  \\begin{enumerate}\n"
        )

        s = ""
        e1 = []
        tasksL = []

        # 1) Найди число по 1/b части
        for i in range(n):
            a = randint(2, 10)
            b = randint(3, 11)
            c = a * b
            d = 0
            s1 = (
                "\\item Найди число, если его $\\frac{1}{"
                + str(b)
                + "}$  часть равна "
                + str(c)
                + ". Нарисуй схему.  \\\\ \\nopagebreak \\begin{tikzpicture}\n"
                " \\draw[step="
                + st
                + ",gray,very thin] (0,0) grid "
                + rect
                + ";\n % Обводка внешнего контура  \\draw[black, thick] (0,0) rectangle "
                + rect
                + ";\n \\end{tikzpicture}\n"
            )
            ans = "\\item " + str(c * b) + "\n"
            ar = [a, b, c, d, s1, ans]
            e1.append(ar)

        # 2) Найди 1/a часть от числа
        for i in range(n):
            a = randint(2, 15)
            b = randint(3, 14)
            d = a * b
            c = 0
            s1 = (
                "\\item Найди $\\frac{1}{"
                + str(a)
                + "}$ часть от "
                + str(d)
                + ". Нарисуй схему. \\\\ \\nopagebreak \\begin{tikzpicture}\n"
                " \\draw[step="
                + st
                + ",gray,very thin] (0,0) grid "
                + rect
                + ";\n % Обводка внешнего контура  \\draw[black, thick] (0,0) rectangle "
                + rect
                + ";\n \\end{tikzpicture}\n"
            )
            ans = "\\item " + str(b) + "\n"
            ar = [a, b, c, d, s1, ans]
            e1.append(ar)

        # 3) Найди число по a/b части
        for i in range(n):
            a = randint(2, 10)
            b = a + randint(3, 12)
            c = a * b
            d = randint(4, 20)
            s1 = (
                "\\item Найди число, если его $\\frac{"
                + str(a)
                + "}{"
                + str(b)
                + "}$  часть равна "
                + str(c)
                + ". Нарисуй схему.  \\\\ \\nopagebreak \\begin{tikzpicture}\n"
                " \\draw[step="
                + st
                + ",gray,very thin] (0,0) grid "
                + rect
                + ";\n % Обводка внешнего контура  \\draw[black, thick] (0,0) rectangle "
                + rect
                + ";\n \\end{tikzpicture}\n"
            )
            ans = "\\item " + str(c * b // a) + "\n"
            ar = [a, b, c, d, s1, ans]
            e1.append(ar)

        # 4) Найди a/b часть от числа
        for i in range(n):
            a = randint(3, 13)
            b = a + randint(5, 10)
            d = a * b
            c = 0
            s1 = (
                "\\item Найди $\\frac{"
                + str(a)
                + "}{"
                + str(b)
                + "}$ часть от "
                + str(d)
                + ".  Нарисуй схему. \\\\ \\nopagebreak \\begin{tikzpicture}\n"
                " \\draw[step="
                + st
                + ",gray,very thin] (0,0) grid "
                + rect
                + ";\n % Обводка внешнего контура  \\draw[black, thick] (0,0) rectangle "
                + rect
                + ";\n \\end{tikzpicture}\n"
            )
            ans = "\\item " + str(d * a // b) + "\n"
            ar = [a, b, c, d, s1, ans]
            e1.append(ar)

        # 5) Найди число по проценту
        for i in range(n):
            a = randint(2, 20)
            b = randint(3, 22)
            c = a * b * 100
            d = randint(2, 20)
            s1 = (
                "\\item Найди число, если его  "
                + str(a)
                + " \\%  равны "
                + str(c)
                + ". Нарисуй схему.  \\\\ \\nopagebreak \\begin{tikzpicture}\n"
                " \\draw[step="
                + st
                + ",gray,very thin] (0,0) grid "
                + rect
                + ";\n % Обводка внешнего контура  \\draw[black, thick] (0,0) rectangle "
                + rect
                + ";\n \\end{tikzpicture}\n"
            )
            ans = "\\item " + str(c * 100 // a) + "\n"
            ar = [a, b, c, d, s1, ans]
            e1.append(ar)

        # 6) Найди a% от числа
        for i in range(n):
            a = randint(3, 12)
            b = randint(4, 23)
            d = a * b * 100
            c = 0
            s1 = (
                "\\item Найди "
                + str(a)
                + " \\%  от "
                + str(d)
                + ".  Нарисуй схему. \\\\ \\nopagebreak \\begin{tikzpicture}\n"
                " \\draw[step="
                + st
                + ",gray,very thin] (0,0) grid "
                + rect
                + ";\n % Обводка внешнего контура  \\draw[black, thick] (0,0) rectangle "
                + rect
                + ";\n \\end{tikzpicture}\n"
            )
            ans = "\\item " + str(d * a // 100) + "\n"
            ar = [a, b, c, d, s1, ans]
            e1.append(ar)

        end = "\\end{enumerate}  \n\\newpage\n"
        answ = (
            "\\subsection*{Ответы. В "
            + str(names.index(j) + 1)
            + ".  \\\\ \\today   \\\\ \\currenttime}   \n\\begin{enumerate}\n"
        )

        # shuffle(e1)

        s = ""
        for i in e1:
            s += i[4]
            answ += i[5]

        answ += "\\end{enumerate}  \n"

        f.write(begin + s + end)
        fAnsw += answ

with open(answ_path, "w", encoding="utf-8") as f:
    f.write(fAnsw)
