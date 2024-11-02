# Помнится, занимались надписями таким шрифтом в тетрадях в клеточку

from PIL import Image, ImageDraw

WORD = 'URBAN URAGAN' #Любое слово из заданных букв, можно BURAN или URA или ARRRRRRR, любой длины
PSIZE = 39 #Размер клеточки
COLOR = (0, 170, 255)
LETTER = {'A': ((2,1,3),(1,0,1),(1,1,1),(1,0,1),(1,0,1)),
          'R': ((1,1,3),(1,0,1),(1,1,6),(1,0,1),(1,0,1)),
          'B': ((1,1,3),(1,0,1),(1,1,6),(1,0,1),(1,1,4)),
          'U': ((1,0,1),(1,0,1),(1,0,1),(1,0,1),(5,1,4)),
          'N': ((1,0,1),(1,3,1),(1,5,1),(1,0,1),(1,0,1)),
          ' ': ((0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)),
          'G': ((2,1,1),(1,0,0),(1,0,0),(1,0,1),(5,1,4))}

def drawletter(draw, letter, offset):
    offs = offset * 4
    for i in (1,2,3):
        for j in (1,2,3,4,5):
            if LETTER[letter][j - 1][i - 1] == 0:
                pass
            elif LETTER[letter][j-1][i-1] == 1:
                draw.rectangle([(i + offs) * PSIZE, j * PSIZE, (i + 1 + offs) * PSIZE, (j + 1) * PSIZE],
                               fill=COLOR)
            elif LETTER[letter][j-1][i-1] == 2:
                draw.polygon(
                    [(i + offs) * PSIZE, (j + 1) * PSIZE, (i + 1 + offs) * PSIZE, (j + 1) * PSIZE, (i + 1 + offs) * PSIZE,
                     (j) * PSIZE], fill=COLOR)
            elif LETTER[letter][j-1][i-1] == 3:
                draw.polygon(
                    [(i + offs) * PSIZE, j * PSIZE, (i + 1 + offs) * PSIZE, (j + 1) * PSIZE, (i + offs) * PSIZE,
                     (j + 1) * PSIZE], fill=COLOR)
            elif LETTER[letter][j-1][i-1] == 4:
                draw.polygon(
                    [(i + offs) * PSIZE, j * PSIZE, (i + offs) * PSIZE, (j + 1) * PSIZE, (i + 1 + offs) * PSIZE,
                     (j) * PSIZE], fill=COLOR)
            elif LETTER[letter][j-1][i-1] == 5:
                draw.polygon(
                    [(i + 1 + offs) * PSIZE, j * PSIZE, (i + 1 + offs) * PSIZE, (j + 1) * PSIZE, (i + offs) * PSIZE,
                     j * PSIZE], fill=COLOR)
            elif LETTER[letter][j-1][i-1] == 6:
                draw.polygon(
                    [(i + offs) * PSIZE, j * PSIZE, (i + 1 + offs) * PSIZE, j * PSIZE, (i + 0.5 + offs) * PSIZE,
                     (j + 0.5) * PSIZE, (i + 1 + offs) * PSIZE, (j + 1) * PSIZE, (i + offs) * PSIZE, (j + 1) * PSIZE], fill=COLOR)
            # Здесь должно быть еще несколько графических элементов, но для заданного набора букв они не нужны
            # Поэтому я не стал их делать


# Создаем новое изображение размером под длину слова, учитывая размер "пикселя"
img = Image.new('RGB', (PSIZE*4*len(WORD)+PSIZE, PSIZE*7), color=(255, 255, 255))

# Получаем объект для рисования
draw = ImageDraw.Draw(img)

#Рисуем каждую букву в слове
offset = 0
for l in WORD:
    drawletter(draw, l, offset)
    offset +=1

img.show()