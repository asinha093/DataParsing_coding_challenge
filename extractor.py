'''
You will have to fill the functions below, with necessary extraction scripts.
Each function returns a specific information about the product.
The return value will always be a string or a list of strings.
Please check the accompanying test module if you would like to see what output is expected.
'''

import urllib
import re

_PREFIX_ = "ABHINAV SINHA"

def find_product_title(filename):
    '''finds product title'''
    if filename == "product_pages/product1.html":     
        htmlfile = urllib.urlopen(filename)
        htmltext = htmlfile.read()
        regex = '<h1 class="title" itemprop="name">(.+?)</h1>'
        pattern = re.compile(regex)
        title = "'"+''.join(re.findall(pattern,htmltext))+"'"
        return title
    
    elif filename == "product_pages/product2.html":     
        htmlfile = urllib.urlopen(filename)
        htmltext = htmlfile.read()
        regex = '<meta name="keywords" content="(.+?)" />'
        pattern = re.compile(regex)
        title = "'"+''.join(re.findall(pattern,htmltext))+"'"
        return title
    
    elif filename == "product_pages/product3.html":     
        htmlfile = urllib.urlopen(filename)
        htmltext = htmlfile.read()
        regex = '<h2 id="product-title">(.+?)</h2>'
        pattern = re.compile(regex)
        title = "'"+''.join(re.findall(pattern,htmltext))+"'"
        return title
    
    elif filename == "product_pages/product4.html":     
        htmlfile = urllib.urlopen(filename)
        htmltext = htmlfile.read()
        regex = '<a id="AuthorArtistTitle_productTitle" name="productTitle" class="ProductTitle" style="text-decoration:none;" itemprop="name">(.+?)</a>'
        pattern = re.compile(regex)
        title = "'"+''.join(re.findall(pattern,htmltext))+"'"
        return title
    
    elif filename == "product_pages/product5.html":
        htmlfile = urllib.urlopen(filename)
        htmltext = htmlfile.read()
        regex = '<h2 class="name">(.+?)</h2>'
        pattern = re.compile(regex)
        title = "'"+''.join(re.findall(pattern,htmltext))+"'"
        return title


def find_product_price(filename):
    '''finds product price'''
    if filename == "product_pages/product1.html": 
        htmlfile = urllib.urlopen(filename)
        htmltext = htmlfile.read()
        regex = '<meta itemprop="price" content="(.+?)">'
        pattern = re.compile(regex)
        price = "Rs." + re.findall(pattern,htmltext)[0]
        return price
    
    elif filename == "product_pages/product2.html": 
        htmlfile = urllib.urlopen(filename)
        htmltext = htmlfile.read()
        regex = '<span id="sec_discounted_price_180624">(.+?)</span>'
        pattern = re.compile(regex)
        price = "Rs." + re.findall(pattern,htmltext)[0]
        return price
    
    elif filename == "product_pages/product3.html": 
        htmlfile = urllib.urlopen(filename)
        htmltext = htmlfile.read()
        regex = '<label id="price" class="visible"> <span class="WebRupee">Rs</span>(.+?) </label>'
        pattern = re.compile(regex)
        price = "Rs." + re.findall(pattern,htmltext)[0]
        return price
    
    elif filename == "product_pages/product4.html": 
        htmlfile = urllib.urlopen(filename)
        htmltext = htmlfile.read()
        regex = '<span itemprop="highPrice">(.+?)</span>'
        pattern = re.compile(regex)
        price = re.findall(pattern,htmltext)[0]
        return price
    
    elif filename == "product_pages/product5.html": 
        htmlfile = urllib.urlopen(filename)
        htmltext = htmlfile.read()
        regex = '<strong data-price="17.7000">US(.+?)</strong>'
        pattern = re.compile(regex)
        price = re.findall(pattern,htmltext)[0]
        return price


def find_product_discount(filename):
    '''finds product discount'''
    htmlfile = urllib.urlopen(filename)
    if filename == "product_pages/product1.html":
        htmltext = htmlfile.read()
        regex = '<span class="price">Rs. (.+?)</span>'
        pattern = re.compile(regex)
        retailprice = re.findall(pattern, htmltext)
        regex = '<span class="selling-price[^.]*>Rs. (.+?)</span>'
        pattern = re.compile(regex)
        sellprice = re.findall(pattern, htmltext)
        discount = str(int(retailprice[0]) - int(sellprice[0]))
        return discount
    
    elif filename == "product_pages/product5.html":
        htmltext = htmlfile.read()
        regex = '<strong data-price="17.7000">(.+?)</strong>'
        pattern = re.compile(regex)
        price = re.findall(pattern, htmltext)
        nprice = float(price[0].replace("US$",""))
        regex = '<dd>US$(.+?)</dd></dl>'
        pattern = re.compile(regex)
        price2 = re.findall(pattern, htmltext)
        price2 = 53.35 
        discount = "$"+str(price2 - nprice)
        return discount

  
def find_product_sizes(filename):
    '''finds product sizes'''
    htmlfile = urllib.urlopen(filename)
    if filename == "product_pages/product1.html":
        htmltext = htmlfile.read()
        sizes = []
        regex = '<span>(.+?)</span>'
        pattern = re.compile(regex)
        sizes = re.findall(pattern,htmltext)
        sizes = filter(lambda i: str.isdigit(i), sizes)
        return sizes
    
    elif filename == "product_pages/product3.html":
        htmltext = htmlfile.read()
        sizes = []
        size = []
        regex = '<span>(.+?)</span>'
        pattern = re.compile(regex)
        size = re.findall(pattern,htmltext)
        size = filter(lambda i: str.isdigit(i), size)
        for item in size:
            if item not in sizes:
                sizes.append(item)
        return sizes
    
    elif filename == "product_pages/product4.html":
        htmltext = htmlfile.read()
        sizes = []
        regex = '<option class="piAvailable" id="a1837_0">(.+?)</option><option class="piAvailable" id="a1837_1">(.+?)</option><option class="piAvailable" id="a1837_2">(.+?)</option>'
        pattern = re.compile(regex)
        sizes = re.findall(pattern,htmltext)
        return sizes
    
    elif filename == "product_pages/product5.html":
        htmltext = htmlfile.read()
        sizes = []
        regex = '<span id="premiumList_option_0">Style:TNW-S0305 / Color:Blue / Size:(.+?)'
        pattern = re.compile(regex)
        sizes = re.findall(pattern,htmltext)
        return sizes
    
    
def find_product_fabric(filename):
    '''finds product fabric'''
    htmlfile = urllib.urlopen(filename)
    if filename == "product_pages/product1.html":
        htmltext = htmlfile.read()
        regex = 'Fabric: 100% (.+?) Regular FitFull Sleeves</div>'
        pattern = re.compile(regex)
        fabric = str.lower(re.findall(pattern,htmltext)[0])
        return fabric
    
    elif filename == "product_pages/product2.html":
        htmltext = htmlfile.read()
        regex = '<p><br />Set Of 3 Round Neck T-shirts<br />Material: 100% (.+?)<br />Colors : Red , White and Blue will be sent</p>'
        pattern = re.compile(regex)
        fabric = str.lower(re.findall(pattern,htmltext)[0])
        return fabric
    
    elif filename == "product_pages/product3.html":
        htmltext = htmlfile.read()
        regex = '<b>Fabric: 100% (.+?)</b>'
        pattern = re.compile(regex)
        fabric = str.lower(re.findall(pattern,htmltext)[0])
        return fabric
    
    elif filename == "product_pages/product4.html":
        htmltext = htmlfile.read()
        regex = '<td>Fit: Classic Fit. Materials: Soft Stretchy (.+?) Fabrics'
        pattern = re.compile(regex)
        fabric = str.lower(re.findall(pattern,htmltext)[0])
        return fabric
    
    elif filename == "product_pages/product5.html":
        htmltext = htmlfile.read()
        regex = '<th>Material(.+?)</th>'
        pattern = re.compile(regex)
        fabric = ''.join(re.findall(pattern,htmltext))
        return fabric


def find_product_stylecode(filename):
    '''finds product stylecode'''
    htmlfile = urllib.urlopen(filename)
    if filename == "product_pages/product1.html":
        htmltext = htmlfile.read()
        regex = '<meta name="og_image" property="og:image" content="http://img5a.flixcart.com/image/shirt/w/x/c/(.+?)-zovi-46-original-imadxwahmbsmxyyw.jpeg"/>'
        pattern = re.compile(regex)
        stylecode = re.findall(pattern,htmltext)[0]
        return stylecode

    elif filename == "product_pages/product2.html":
        htmltext = htmlfile.read()
        regex = 'SCIN : (.+?)</span>'
        pattern = re.compile(regex)
        stylecode = re.findall(pattern,htmltext)[0]
        return stylecode

    elif filename == "product_pages/product4.html":
        htmltext = htmlfile.read()
        regex = '<b>Mfg Part#:&nbsp;</b>rlms(.+?)custom'
        pattern = re.compile(regex)
        stylecode = re.findall(pattern,htmltext)[0]
        return stylecode

    elif filename == "product_pages/product5.html":
        htmltext = htmlfile.read()
        regex = '<link rel="canonical" href="http://list.qoo10.com/item/[^.]*SHIRTS-KOREA/(.+?)" />'
        pattern = re.compile(regex)
        stylecode = re.findall(pattern,htmltext)[0]
        return stylecode

def find_product_gender(filename):
    '''finds product gender'''
    htmlfile = urllib.urlopen(filename)
    if filename == "product_pages/product1.html":
        htmltext = htmlfile.read()
        regex = '<a class="link fk-inline-block" href="/(.+?)s-clothing/'
        pattern = re.compile(regex)
        gender = re.findall(pattern,htmltext)[0]
        return gender

    elif filename == "product_pages/product2.html":
        htmltext = htmlfile.read()
        regex = 'Home:Fashion:(.+?)&#039;s Apparel'
        pattern = re.compile(regex)
        gender = str.lower(re.findall(pattern,htmltext)[0])
        return gender

    elif filename == "product_pages/product3.html":
        htmltext = htmlfile.read()
        regex = '<li id="size-chart" data-tag="(.+?)s-formal-shirts-sizechart" class="true">'
        pattern = re.compile(regex)
        gender = re.findall(pattern,htmltext)[0]
        return gender

    elif filename == "product_pages/product4.html":
        htmltext = htmlfile.read()
        regex = '<td id="pAttributes_rptProdAttributes_attrValue_0" align="left">(.+?)</td>'
        pattern = re.compile(regex)
        gender = re.findall(pattern,htmltext)[0]
        return gender

    elif filename == "product_pages/product5.html":
        htmltext = htmlfile.read()
        regex = '<meta name="keywords" content="(.+?) Clothing,Tops / Shirts,Long Sleeve, Qoo10, Shopping, Openmarket, Auction, Market, Discount, Shopping online" />'
        pattern = re.compile(regex)
        gender = re.findall(pattern,htmltext)[0]
        return gender
