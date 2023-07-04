import msvcrt
def input_select(options, campo):
    print(campo)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    while True:
        key = msvcrt.getch()
        key = key.decode("utf-8")

        if key.isdigit() and int(key) in range(1, len(options) + 1):
            index = int(key) - 1
            print("Seleccionado:",options[index])
            return options[index]
