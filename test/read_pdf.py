from io import StringIO
from io import open
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, process_pdf


def read_pdf(pdf):
    # resource manager
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    # device
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    process_pdf(rsrcmgr, device, pdf)
    device.close()
    content = retstr.getvalue()
    retstr.close()
    # 获取所有行
    lines = str(content).split("\n")

    units = [1, 2, 3, 5, 7, 8, 9, 11, 12, 13]
    header = '\x0cUNIT '
    # print(lines[0:100])
    count = 0
    flag = False
    text = open('words.txt', 'w+')
    for line in lines:
        if line.startswith(header):
            flag = False
            count += 1
            if count in units:
                flag = True
                print(line)
                text.writelines(line + '\n')
        if '//' in line and flag:
            text_line = line.split('//')[0].split('. ')[-1]
            print(text_line)
            text.writelines(text_line + '\n')
    text.close()


def _main():
    my_pdf = open('/Users/admin/Desktop/Richard_P._Feynman.pdf', "rb")
    read_pdf(my_pdf)
    my_pdf.close()


if __name__ == '__main__':
    # _main()
    # exit(0)

    my_pdf = open('/Users/admin/Desktop/Richard_P._Feynman.pdf', "rb")

    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    # device
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    process_pdf(rsrcmgr, device, my_pdf)
    device.close()
    content = retstr.getvalue()
    retstr.close()
    lines = str(content).split("\n")
    for line in lines:
        print(line)
        '''
        The stories in this book were collected intermittently and informally during seven years of very enjoyable drumming with Richard Feynman. I have found each story by itself to be amusing, and the collection taken together to be amazing: That one person could have so many wonderfully crazy things happen to him in one life is sometimes hard to believe. That one person could invent so much innocent mischief in one life is surely an inspiration!
        RALPH LEIGHTON
        Introduction
        I hope these won't be the only memoirs of Richard Feynman. Certainly the reminiscences here give a true picture of much of his character ­­ his almost compulsive need to solve puzzles, his provocative mischievousness, his indignant impatience with pretension and hypocrisy, and his talent for one­upping anybody who tries to one­up him! This book is great reading: outrageous, shocking, still warm and very human.
        For all that, it only skirts the keystone of his life: science. We see it here and there, as background material in one sketch or another, but never as the focus of his existence, which generations of his students and colleagues know it to be. Perhaps nothing else is possible. There may be no way to construct such a series of delightful stories about himself and his work: the challenge and frustration, the excitement that caps insight, the deep pleasure of scientific understanding that has been the wellspring of happiness in his life.
        I remember when I was his student how it was when you walked into one of his lectures. He would be standing in front of the hall smiling at us all as we came in, his fingers tapping out a complicated rhythm on the black top of the demonstration bench that crossed the front of the lecture hall. As latecomers took their seats, he picked up the chalk and began spinning it rapidly through his fingers in a manner of a professional gambler playing with a poker chip, still smiling happily as if at some secret joke. And then ­­ still smiling ­­ he talked to us about physics, his diagrams and equations helping us to share his understanding. It was no secret joke that brought the smile and the sparkle in his eye, it was physics. The joy of physics! The joy was contagious. We are fortunate who caught that infection. Now here is your opportunity to be exposed to the joy of life in the style of Feynman.
        ALBERT R. HIBBS
        Senior Member of the Technical Staff, Jet Propulsion Laboratory,
        California Institute of Technology
        '''