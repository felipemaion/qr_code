# qr_code
Code to generate QR-CODE from a url, adding a logo and a title.

Requirements (pip install): pyqrcode, pillow

Usage: 
1 - Add display 'name' and shorten link 'url' to a dict (product). ```product = ["name":"TITLE", "url":"your_url"]```
    1.1 If you are performing a bulk operation. Add the product dict to the list 'products'. ``` products = [product1, product2,...] ```
2 - Call 'convert(product:dict)' or 'convert_all(products:list)'



Notes: 
    (1) for the first run, you may need to add a dummy 'test.png' file to your folder.
    (2) the font of your choice must be in the folder if you want to use it (optional)
    (3) for the bulk operation, use links with same pattern, otherwise QR-CODE will be different amoung them.
