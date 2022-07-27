program = open('Choices++.txt' , 'r')
accumulator = 0
program = program.readlines()


L = [line.rstrip() for line in program]
for n in L:
    if n == "+":
        accumulator += 1
    elif n == "-":  # 2
        accumulator -= 1
    elif n == "o":  # 3
        print(accumulator)
    elif n == "1":  # 4
        accumulator = 1
    elif n == "0":  # 5
        accumulator = 0
    elif n == "dec":  # 6
        accumulator -= 1
    elif n == "print{o}":  # 7
        print(accumulator)
    elif n == "alert{o}":  # 8
        print(accumulator)
    elif n == "System.print.{o}":  # 9
        print(accumulator)
    elif n == ",":  # 10
        accumulator += 10
    elif n == "print<o>":  # 11
        print(accumulator)
    elif n == "add<+>":   # 12
        accumulator += 1
    elif n == "add<+>.print[o]":  # 13
        accumulator += 1
        print(accumulator)
    elif n == "add[+]":   # 14
        accumulator += 1


