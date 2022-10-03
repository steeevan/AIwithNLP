from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from filter import Filter
from io import StringIO
from operator import contains
from io import open
import time
import os




'''
read_pdf
This script allows to be given a pdf file with its directory, and be able to scan in the data from  the pdf.

'''
def read_pdf(pdf):
    # controller which operates on the device
    resource = PDFResourceManager()
    rets = StringIO()
    laparams = LAParams()
    # main control for scanning in pdf
    device = TextConverter(resource, rets, laparams=laparams)
    process_pdf(resource, device, pdf)
    device.close()
    content = rets.getvalue()
    rets.close()
    # get lines
    lines = str(content).split("\n")
    return lines



def key_parts(path):
    list_of_content = []
    list_of_keys = []
    try:
        with open(path, "rb") as my_pdf:
            list_of_content = read_pdf(my_pdf)
            # print(len(list_of_content))

            for i in range(50, len(list_of_content) - 200):
                if len(list_of_content[i]) >= 15:
                    list_of_keys.append(list_of_content[i])
    except:
        pass
    return list_of_keys



def generate(parts):
    str = ""
    for part in parts:
        # print(part)
        str += part
    flt = Filter(str)
    res = flt.filter()
    return res


def read_all(in_directory, out_directory, key_directory):
    for filename in os.listdir(in_directory):
        f = os.path.join(in_directory, filename)
        name = filename.split('.')[0]
        try:
            if os.path.isfile(f):
                ret = generateQ(key_parts(f))
                txt_name = os.path.join(out_directory, f'{name}.txt')
                print(f'OUT: {txt_name}')
                with open(txt_name, "w") as txt:
                    txt.write(ret)
                    txt.close()
        except:
            try:
                os.remove(key_directory + name + '.pdf.txt')
            except FileNotFoundError:
                pass

read_pdf('copus/19690031409.pdf')

