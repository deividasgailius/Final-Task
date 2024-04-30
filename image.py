def hangman_image(wrong):
    if wrong == 0:
        print("\n------")
        print(" |  |")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")

    elif wrong == 1:
        print("\n------")
        print(" |   |")
        print(" O   |")
        print("     |")
        print("     |")
        print("    ===")
    elif wrong == 2:
        print("\n------")
        print(" |   |")
        print(" O   |")
        print(" |   |")
        print("     |")
        print("    ===")
    elif wrong == 3:
        print("\n------")
        print(" |  |")
        print(" O  |")
        print("/|  |")
        print("    |")
        print("   ===")
    elif wrong == 4:
        print("\n------")
        print(" |  |")
        print(" O  |")
        print("/|\ |")
        print("    |")
        print("   ===")
    elif wrong == 5:
        print("\n------")
        print(" |  |")
        print(" O  |")
        print("/|\ |")
        print("/   |")
        print("   ===")
    elif wrong == 6:
        print("\n------")
        print(" |   |")
        print(" O   |")
        print("/|\  |")
        print("/ \  |")
        print("    ===")


hangman_image(wrong=6)
