from pyvncorenlp import VNCoreNLP

if __name__ == '__main__':
    nlp = VNCoreNLP('http://localhost:4567')
    text = 'Ông Nguyễn Khắc Chúc  đang làm việc tại Đại học Quốc gia Hà Nội.'
    output = nlp.analyze(text)
    print(output)