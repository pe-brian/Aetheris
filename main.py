import time

import easyocr

from utils import add_sufix_for_output_file, draw_img_with_bb, perform_OCR

input_path = "img/0.png"
reader = easyocr.Reader(['fr'], gpu=True) # this needs to run only once to load the model into memory

start_time = time.time()
data = perform_OCR(reader, input_path)
print("--- %s seconds ---" % (time.time() - start_time))
print(data)

img = draw_img_with_bb(input_path, data)
img.show()
img.save(add_sufix_for_output_file(input_path))
