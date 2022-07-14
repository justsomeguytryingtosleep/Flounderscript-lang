accumulator = 0
program = input()

for instruction in program:
    if instruction == "+":
        accumulator += 1
    if instruction == "-":
        accumulator -= 1
    if instruction == "o":
        print(accumulator)
    if instruction == "1":
        accumulator = 1
    if instruction == "0":
        accumulator = 0