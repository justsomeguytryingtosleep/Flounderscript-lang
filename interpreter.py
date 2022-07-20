# Choices++ interpreter.
program = input()
accumulator = 0




for instruction in program:
    if instruction == "+":  # 1
        accumulator += 1
    elif instruction == "-":  # 2
        accumulator -= 1
    elif instruction == "o":  # 3
        print(accumulator)
    elif instruction == "1":  # 4
        accumulator = 1
    elif instruction == "0":  # 5
        accumulator = 0
    elif instruction == "dec":  # 6
        accumulator -= 1
    elif instruction == "print{o}":  # 7
        print(accumulator)
    elif instruction == "alert{o}":  # 8
        print(accumulator)
    elif instruction == "System.print.{o}":  # 9
        print(accumulator)
    elif instruction == ",":  # 10
        accumulator += 10
    elif instruction == "print<o>":  # 11
        print(accumulator)
    elif instruction == "add<+>":   # 12
        accumulator += 1
    elif instruction == "add<+>.print[o]":  # 13
        accumulator += 1
        print(accumulator)
    elif instruction == "add[+]":   # 14
        accumulator += 1

