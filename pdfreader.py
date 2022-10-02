from io import StringIO
from io import open
from operator import contains
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager
import time
import os

from filter import Filter


# process pd
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
    # get lines
    lines = str(content).split("\n")
    return lines


# get key parts
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


# form Q
def generateQ(parts):
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

