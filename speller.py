from pyaspeller import YandexSpeller

def speller_word():
    spellers: YandexSpeller = YandexSpeller()
    letters: str = 'в субботу утромъ'
    fixes: str = spellers.spelled(letters)
    print(fixes)


if __name__ == '__main__':
    speller_word()