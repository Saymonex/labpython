#Napisz program, który podany przez użytkownika ciąg znaków szyfruje przy
#użyciu szyfru Cezara i wyświetla zaszyfrowany tekst.

SZYFR = 2


def szyfruj(txt):
    zaszyfrowny = ""
    for i in range(len(txt)):
        if ord(txt[i]) > 122 - SZYFR:
            zaszyfrowny += chr(ord(txt[i]) + SZYFR - 26)
        else:
            zaszyfrowny += chr(ord(txt[i]) + SZYFR)
    return zaszyfrowny


def main(args):
    tekst = input("Podaj ciąg do zaszyfrowania:\n")
    print("Ciąg zaszyfrowany:\n", szyfruj(tekst))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
