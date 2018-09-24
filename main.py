#encoding: utf-8
import pyautogui
import time
import os
from fpdf import FPDF
import img2pdf

def main():

    time.sleep(10)

    page_count = 4046

    for i in range(page_count):
        region = (700, 0, 450, 950)
        pyautogui.screenshot('screenshots\%d.png' % i, region = region)
        pyautogui.press('right')
        time.sleep(0.1)

# both image to pdf coversion methods are SLOW, use Photoshop to better do it
def pages_to_pdf(folder = 'screenshots'):
    pdf = FPDF()
    for i in range(6, 611):
        pdf.add_page()
        image_path = '%s\%d.png' % (folder, i)
        pdf.image(image_path)
    
    pdf.output('output.pdf')
    
def raw_pages_to_pdf(folder = 'screenshots'):

    page_list = ['%s\%d.png' % (folder, i) for i in range(6, 611)]
    with open('output.pdf', 'wb') as f:
        f.write(img2pdf.convert(page_list))

if __name__ == '__main__':
    main()
    # pages_to_pdf()