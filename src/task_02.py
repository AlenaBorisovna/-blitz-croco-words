from pptx import Presentation

FILE_NAME = 'D:\Учеба\-blitz-croco-words\src\croco-blitz-source\Osennyaya_igra_11.pptx'


def get_file():
    prs = Presentation(FILE_NAME)

    print(f'Содержимое пресентации: {len(prs.slides)}')

    for slide in prs.slides:
        print(f'Слайд {slide.slide_id}')


if __name__ == '__main__':
    get_file()
