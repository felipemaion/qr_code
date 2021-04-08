#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Script to generate QR-CODE for the BOLLHOFF's products .
Usage: 
1 - Add display 'name' and shorten link 'url' to a dict (product). 
    1.1 If you are performing a bulk operation. Add the product dict to the list 'products'.
2 - Call 'convert(product:dict)' or 'convert_all(products:list)'

Requirements: pyqrcode, pillow

Notes: 
    (1) for the first run, you may need to add a dummy 'test.png' file to your folder.
    (2) the font of your choice must be in the folder if you want to use it (optional)
    (3) for the bulk operation, use links with same pattern, otherwise QR-CODE will be different amoung them.
"""

# author: Felipe Maion 
# e-mail: felipe.maion@gmail.com

import pyqrcode
from PIL import Image, ImageDraw, ImageFont


def clean_name(name):
    return name.replace(" ", "_").replace("®","").lower() + ".png"

def convert(product, show=True):
    W = 410
    H = 410
    url = pyqrcode.QRCode(product["url"],error = 'H')
    url.png('test.png',scale=10)
    im = Image.open('test.png')
    im = im.convert("RGBA")
    box = (135,135,270,270)
    im.crop(box)
    region =  Image.open('logoBSC.png')
    region = region.resize((box[2] - box[0], box[3] - box[1]))
    im.paste(region,box)
    w, h = ImageDraw.Draw(im).textsize(product["name"])
    position = ((W-w*2)/2, 10)
    
    # Font must be in the same folder. 
    font = ImageFont.truetype("ArchivoBlack-Regular.ttf", 18)
    font2 = ImageFont.truetype("ArchivoBlack-Regular.ttf", 14)

    ImageDraw.Draw(im).text(
                            position,  # Coordinates
                            product["name"],  # Text
                            (0, 0, 0),  # Color
                            font=font)
    ImageDraw.Draw(im).text(
                            (300, 380),  # Coordinates
                            "[ SCAN ME ]",  # Text
                            (0, 0, 0),  # Color
                            font=font2)    
    if show: im.show()
    im.save("qr_codes/"+ clean_name(product["name"]))
    print(f"{clean_name(product['name'])} saved at: ./qr_codes/{clean_name(product['name'])}")


def convert_all(products):    
    for product in products:
        convert(product, show=False)

if __name__ == "__main__":
    # Felipe's Products
    flexitol_metalic = {"name":"FLEXITOL® METAL", "url":"https://youtu.be/39ztuWJMt-0"}
    flexitol_hybrid = {"name":"FLEXITOL® HYBRID", "url":"https://youtu.be/in7gyRkusN4"}
    flexitol_plastic = {"name":"FLEXITOL® PLASTIC", "url":"https://youtu.be/7gkERfVmonk"}
    flexitol_kink = {"name":"FLEXITOL® KinK", "url":"https://youtu.be/QfFDQSDJa48"}
    flexitol_eco = {"name":"FLEXITOL® Eco", "url":"https://youtu.be/aNfMv1HCdBU"}
    flexitol_system = {"name":"FLEXITOL® SYSTEM", "url":"https://youtu.be/n6HldL4E6jY"}
    # wo_flexitol = {"name":"", "url":""} # without youtube link??
    snaploc = {"name":"SNAPLOC®", "url":"https://youtu.be/FL9M38tTHYs"}
    quickloc = {"name":"QUICKLOC®", "url":"https://youtu.be/j-n_QAlsEwA"}
    sitec_clip = {"name":"SITEC® CLIP", "url":"https://youtu.be/0W6vsvQGo6A"}
    sitec_spring = {"name":"SITEC® SPRING", "url":"https://youtu.be/OEbUGTIixEg"}
    sitec_pin = {"name":"SITEC® PIN", "url":"https://youtu.be/lnFVL69HWgY"}
    sitec_rivet = {"name":"SITEC® RIVET", "url":"https://youtu.be/cOY-sT8KbZM"}
    onsert_manual = {"name":"ONSERT® MANUAL TOOL", "url":"https://youtu.be/TTqeGlxQ2Bo"}
    onsert_mini = {"name":"ONSERT® MINI MANUAL TOOL", "url":"https://youtu.be/U1RiEfvlGuc"}
    onsert_auto = {"name":"ONSERT® AUTOMATION DEMO", "url":"https://youtu.be/nUBYu5QSvpU"}
    tepro = {"name":"TEPRO® KinK", "url":"https://youtu.be/d1Ae0XtEmjw"}


    # Ciloto's Products
    rivset = {"name":"RIVSET®","url":"https://youtu.be/ixR4eqRJGRc"}
    rivquick_varigrip = {"name": "RIVQUICK® VARIGRIP", "url":"https://youtu.be/er2z5UaY92M"}
    rivquick_std = {"name": "RIVQUICK® STD", "url":"https://youtu.be/u9EnPAgo8p4"}
    rivclinch = {"name": "RIVCLINCH®", "url": "https://youtu.be/P1iMcCI70R0"}

    # Henrique's Products
    hitsert = {"name":"HITSERT®", "url":"https://youtu.be/9MZhXutWfRM"}
    quicksert = {"name":"QUICKSERT®", "url":"https://youtu.be/rDJfKSor9kE"}
    spreadsert = {"name": "SPREDSERT®", "url":"https://youtu.be/l9uwoUx3-Jw"}
    helicoil_free_running = {"name": "HELICOIL® FREE RUNNING", "url":"https://youtu.be/bp31p8jSWaM"}
    helicoil_screwlock = {"name": "HELICOIL® SCREWLOCK", "url":"https://youtu.be/-_azEsNkA9Q"}
    imtec_co = {"name": "IMTEC® CO", "url": "https://youtu.be/hE_82vAZlHo"}
    imtec_cf = {"name": "IMTEC® CF", "url":"https://youtu.be/PDQxDeImeUA"}

    # Eduardo's Products
    kapti_nut = {"name":"KAPTI NUT®", "url":"https://youtu.be/luvSWrN55bc"}
    rivkle_pt = {"name":"RIVKLE®", "url":"https://youtu.be/luvSWrN55bc"}


    # All
    products = [flexitol_metalic, 
                flexitol_hybrid, 
                flexitol_plastic, 
                flexitol_kink,
                flexitol_eco,
                flexitol_system,
                # wo_flexitol, 
                snaploc, 
                quickloc, 
                sitec_clip, 
                sitec_spring, 
                sitec_pin, 
                sitec_rivet, 
                onsert_manual,
                onsert_mini, 
                onsert_auto,
                rivset,
                rivquick_varigrip,
                rivquick_std,
                rivclinch,
                hitsert,
                quicksert,
                spreadsert,
                helicoil_free_running,
                helicoil_screwlock,
                imtec_co,
                imtec_cf,
                kapti_nut,
                rivkle_pt
                ]
    convert_all(products)



