import time

import easyocr
import yaml

from utils import draw_img_with_bb, perform_OCR

input_path = "input/0.png"
reader = easyocr.Reader(['fr'], gpu=True) # this needs to run only once to load the model into memory


start_time = time.time()
data = perform_OCR(reader, input_path)
print("--- %s seconds ---" % (time.time() - start_time))
print(data)

with open('output/0__step1_OCR.yaml', 'w', encoding="utf-8") as f:
    yaml.dump(data, f, allow_unicode=True, default_flow_style=False)

img = draw_img_with_bb(input_path, data)
img.show()
img.save('output/0__step1_OCR.png')
