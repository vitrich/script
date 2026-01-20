from random import randint, shuffle


f = open("tasks.tex", "w")
f.write("")
f = open("tasks.tex", "a")
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
    "Ильиной Софии Антоновны",
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

names = vitrich4
print("Hi")
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

    for i in range(n):  # 1
        a = randint(2, 10)
        b = randint(3, 11)
        c = a * b
        d = 0
        s = (
            "\\item Найди число, если его $\\frac{1}{"
            + str(b)
            + "}$  часть равна "
            + str(c)
            + ". Нарисуй схему.  \\\\ \\nopagebreak \\begin{tikzpicture}\n \\draw[step="
            + st
            + ",gray,very thin] (0,0) grid "
            + rect
            + ";\n % Обводка внешнего контура  \\draw[black, thick] (0,0) rectangle "
            + rect
            + ";\n \\end{tikzpicture}"
        )
        ans = "\\item " + str(c * b)
        ar = [a, b, c, d, s, ans]
        e1.append(ar)

    for i in range(n):
        a = randint(2, 15)
        b = randint(3, 14)
        d = a * b
        c = 0
        s = (
            "\\item Найди $\\frac{1}{"
            + str(a)
            + "}$ часть от "
            + str(d)
            + ". Нарисуй схему. \\\\ \\nopagebreak \\begin{tikzpicture}\n \\draw[step="
            + st
            + ",gray,very thin] (0,0) grid "
            + rect
            + ";\n % Обводка внешнего контура  \\draw[black, thick] (0,0) rectangle "
            + rect
            + ";\n \\end{tikzpicture}"
        )
        ans = "\\item " + str(b)
        ar = [a, b, c, d, s, ans]
        e1.append(ar)

    for i in range(n):
        a = randint(2, 10)
        b = a + randint(3, 12)
        c = a * b
        d = randint(4, 20)
        s = (
            "\\item Найди число, если его $\\frac{"
            + str(a)
            + "}{"
            + str(b)
            + "}$  часть равна "
            + str(c)
            + ". Нарисуй схему.  \\\\ \\nopagebreak \\begin{tikzpicture}\n \\draw[step="
            + st
            + ",gray,very thin] (0,0) grid "
            + rect
            + ";\n % Обводка внешнего контура  \\draw[black, thick] (0,0) rectangle "
            + rect
            + ";\n \\end{tikzpicture}"
        )
        ans = "\\item " + str(c * b // a)
        ar = [a, b, c, d, s, ans]
        e1.append(ar)
    for i in range(n):
        a = randint(3, 13)
        b = a + randint(5, 10)
        d = a * b
        c = 0
        s = (
            "\\item Найди $\\frac{"
            + str(a)
            + "}{"
            + str(b)
            + "}$ часть от "
            + str(d)
            + ".  Нарисуй схему. \\\\ \\nopagebreak \\begin{tikzpicture}\n \\draw[step="
            + st
            + ",gray,very thin] (0,0) grid "
            + rect
            + ";\n % Обводка внешнего контура  \\draw[black, thick] (0,0) rectangle "
            + rect
            + ";\n \\end{tikzpicture}"
        )
        ans = "\\item " + str(d * a // b)
        ar = [a, b, c, d, s, ans]
        e1.append(ar)

    for i in range(n):
        a = randint(2, 20)
        b = randint(3, 22)
        c = a * b * 100
        d = randint(2, 20)
        s = (
            "\\item Найди число, если его  "
            + str(a)
            + " \\%  равны "
            + str(c)
            + ". Нарисуй схему.  \\\\ \\nopagebreak \\begin{tikzpicture}\n \\draw[step="
            + st
            + ",gray,very thin] (0,0) grid "
            + rect
            + ";\n % Обводка внешнего контура  \\draw[black, thick] (0,0) rectangle "
            + rect
            + ";\n \\end{tikzpicture}"
        )
        ans = "\\item " + str(c * 100 // a)
        ar = [a, b, c, d, s, ans]
        e1.append(ar)
    for i in range(n):
        a = randint(3, 12)
        b = randint(4, 23)
        d = a * b * 100
        c = 0
        s = (
            "\\item Найди "
            + str(a)
            + " \\%  от "
            + str(d)
            + ".  Нарисуй схему. \\\\ \\nopagebreak \\begin{tikzpicture}\n \\draw[step="
            + st
            + ",gray,very thin] (0,0) grid "
            + rect
            + ";\n % Обводка внешнего контура  \\draw[black, thick] (0,0) rectangle "
            + rect
            + ";\n \\end{tikzpicture}"
        )
        ans = "\\item " + str(d * a // 100)
        ar = [a, b, c, d, s, ans]
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
f.close()
f = open("answ.tex", "w")
f.write(fAnsw)
f.close()
