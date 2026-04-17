e = [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]

# перестановки при поворотах шестиугольника
turn1 = [[1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 1]]
turn2 = [[1, 2, 3, 4, 5, 6], [3, 4, 5, 6, 1, 2]]
turn3 = [[1, 2, 3, 4, 5, 6], [4, 5, 6, 1, 2, 3]]
turn4 = [[1, 2, 3, 4, 5, 6], [5, 6, 1, 2, 3, 4]]
turn5 = [[1, 2, 3, 4, 5, 6], [6, 1, 2, 3, 4, 5]]

# перестановки симметрии
simm1 = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1]]
simm2 = [[1, 2, 3, 4, 5, 6], [4, 3, 2, 1, 6, 5]]
simm3 = [[1, 2, 3, 4, 5, 6], [5, 4, 3, 2, 1, 6]]
simm4 = [[1, 2, 3, 4, 5, 6], [1, 6, 5, 4, 3, 2]]
simm5 = [[1, 2, 3, 4, 5, 6], [2, 1, 6, 5, 4, 3]]
simm6 = [[1, 2, 3, 4, 5, 6], [3, 2, 1, 6, 5, 4]]

# функция для композиции 2 перестановок
def composition(permutation1, permutation2):
    out = [[1, 2, 3, 4, 5, 6], [0, 0, 0, 0, 0, 0]]
    for i in range(6):
        perm2_el = permutation2[1][i]
        perm1_el = permutation1[1][perm2_el-1]
        out[1][i] = perm1_el

    return getName(out)

# функция для получения имени конкретной перестановки
# возвращает None,если такой перестановки нет в группе
def getName(perm):
    for k, v in named.items():
        if v == perm:
            return k
    return None

# словарь с именами перестановок
named = {
    "e ": e, "t1": turn1, "t2": turn2, "t3": turn3, "t4": turn4, "t5": turn5,
    "s1": simm1, "s2": simm2, "s3": simm3, "s4": simm4, "s5": simm5, "s6": simm6
}

line = [e, turn1, turn2, turn3, turn4, turn5, simm1, simm2, simm3, simm4, simm5, simm6]
collumn = line

print("   | e  t1 t2 t3 t4 t5 s1 s2 s3 s4 s5 s6")
print("---|-------------------------------------")

# композиция считается как столбец * строчка
for col_el in collumn:
    col_name = getName(col_el)
    out_str = col_name + " | "
    for line_el in line:
        result = composition(line_el, col_el)
        out_str += result + " "

    print(out_str)