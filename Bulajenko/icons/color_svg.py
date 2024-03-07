import os
import re
from lxml import etree


def color_svg(path: str):
    svgFill = 'none'
    svgStroke = '#ffffff'

    count = 0

    filenames = [f for f in os.listdir(path) if f.endswith('.svg')]

    for filename in filenames:
        file_name_without_extension = filename.split(os.sep)[-1].removesuffix('.svg')
        # print(file_name_without_extension)
        if file_name_without_extension[-1] == '_':
            continue
        else:
            tree = etree.parse(open(filename, 'r+'))
            for element in tree.iter():
                if element.tag.split("}")[1] == "svg":
                    element.set("fill", svgFill)
                    element.set("stroke", svgStroke)
            # tree.write(file_name_without_extension)
            tree.write(f'{path}{os.sep}{file_name_without_extension}_.svg')
            count += 1
        # print(f'Записан - {count} файл')

    print(f'Обработано - {len(filenames)} файлов')






if __name__ == '__main__':
    color_svg(os.path.dirname((os.path.abspath(__file__))))