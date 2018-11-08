# -- coding: utf-8 --
from PIL import Image
import argparse

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
#获取参数
def get_param():
    # 命令行输入参数处理
    parser = argparse.ArgumentParser()
    # 输入文件
    parser.add_argument('file')
    # 输出文件
    parser.add_argument('-o', '--output')
    # 输出字符画宽
    parser.add_argument('--width', type=int, default=80)
    # 输出字符画长
    parser.add_argument('--height', type=int, default=80)
    # 获取参数
    args = parser.parse_args()
    IMG = args.file
    WIDTH = args.width
    HEIGTH = args.height
    OUTPUT = args.output
    return IMG, WIDTH, HEIGTH, OUTPUT

#将256灰度映射到70个字符上
def get_char(r, g, b, alpha = 256):
    if alpha == 0:
        return ''
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1) / length
    return  ascii_char[int(gray / unit)]


# 将字符输出到文件
def write_file(out_file_name, content):
    if out_file_name:
        with open(out_file_name, 'w') as f:
            f.write(content)
    else:
        with open("output.txt", 'w') as f:
            f.write(content)

def main(file, width, height, out_file):
    im = Image.open(file)
    im = im.resize((width, height), Image.NEAREST)
    txt = ""
    for i in range(height):
        for j in range(width):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'
    print(txt)
    write_file(out_file, txt)

if __name__ == '__main__':
    file, width, height, out_file = get_param()
    main(file, width, height, out_file)