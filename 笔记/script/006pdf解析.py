# encoding: utf-8
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

import requests
import urllib3
import io


# pip install pdfminer3k

def PDFparse(url):
    pdf_content = ''

    with urllib3.PoolManager() as http:
        r = http.request('GET', url)

        with io.BytesIO(r.data) as fp:
            # fp = open(path, 'rb')
            praser = PDFParser(fp)
            doc = PDFDocument()
            praser.set_document(doc)
            doc.set_parser(praser)
            doc.initialize()

            if not doc.is_extractable:
                raise PDFTextExtractionNotAllowed
            else:
                rsrcmgr = PDFResourceManager()
                laparams = LAParams()
                device = PDFPageAggregator(rsrcmgr, laparams=laparams)
                interpreter = PDFPageInterpreter(rsrcmgr, device)

                # 循环遍历列表，每次处理一个page的内容
                for page in doc.get_pages():  # doc.get_pages() 获取page列表
                    # 利用解释器的process_page()方法解析读取单独页数
                    interpreter.process_page(page)
                    layout = device.get_result()
                    for x in layout:
                        if (isinstance(x, LTTextBoxHorizontal)):
                            line = x.get_text()
                            pdf_content += line
                # print(pdf_content)
    return pdf_content



def func2():
    # pip install pdfplumber==0.5.21
    import pdfplumber as ppl

    pdf_path = "公告test.pdf"
    pdf = ppl.open(pdf_path)

    for page in pdf.pages:
        print(page.extract_text())


if __name__ == '__main__':
    # path = "../公告test.pdf"
    # fp = open(path, 'rb').read()  # 读取二进制
    url = "http://disc.static.szse.cn/download/disc/disk03/finalpage/2022-09-09/d09a4fa8-cc54-45fe-858c-769ba0b56504.PDF"
    pdf_res = PDFparse(url)
    print(pdf_res)

