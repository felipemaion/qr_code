# QR CODE
<p align="center">

<img src="qr_codes/flexitol_eco.png" alt="Example of QR-CODE">
<br />
Script to generate QR-CODE from a url, adding a logo and a title.
</p> 


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip install pillow
pip install pyqrcode
```

## Usage
1 - Add display 'name' and shorten link 'url' to a dict (product).   
```
product = {"name":"TITLE", "url":"your_url"}
```  
  
1.1 If you are performing a bulk operation. Add the product dict to the list 'products'.   
``` 
products = [product1, product2,...] 
```  
  
2 - Call:  
  
```
convert(product:dict)
```   
  
or bulk usage: 
  
```
convert_all(products:list)
```  
  
  
  
## Notes:  
    (1) for the first run, you may need to add a dummy 'test.png' file to your folder.  
    (2) the font of your choice must be in the folder if you want to use it (optional)  
    (3) for the bulk operation, use links with same pattern, otherwise QR-CODE size will be different amoung them.  

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate. (Well, the __main__ is pretty much a test :-/ )

## License
[MIT](https://choosealicense.com/licenses/mit/)

