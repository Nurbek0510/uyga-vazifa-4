def ortacha(ballar):
    if len(ballar) == 0:
        return "Ballar yo'q"

    yigindi = 0

    for ball in ballar:
        yigindi = yigindi + ball

    return yigindi / len(ballar)


assert ortacha([60, 80]) == 70.0
assert ortacha([]) == "Ballar yo'q"

print(ortacha([60, 80]))
print(ortacha([]))