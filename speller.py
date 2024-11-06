from pyaspeller import YandexSpeller


def speller_word():
    spellers = YandexSpeller()
    letters: list[str] = ['Колакал', 'Малако']
    fixes = spellers.spelled(' '.join(letters))
    print(fixes)


if __name__ == '__main__':
    speller_word()
