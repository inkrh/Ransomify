from PIL import Image
import random
import string


##TODO create a larger source character set, including all ascii symbols
##TODO create source images for common words for a better appearance
##TODO alter stringToImage to handle the above

def stringToImage(s):
    o = []
    for l in s:
        if l.upper() in string.ascii_uppercase:
            d = "1"
            if random.randint(1,20) > 10:
                d = "2"
                
            o = o +[d+"/"+l.upper()+".png"]
        else:
            o = o + ["ignore"]
    return o



def sentence(s):
    chars = stringToImage(s)
    i = Image.new('RGBA',(len(chars)*110,200),(255,255,255,0))
    mIndex = len(chars)
    for l in range(mIndex):
        if not "ignore" in chars[l]:
            im = Image.open(chars[l])
##            im = im.rotate(random.randint(0-random.randint(0,20),random.randint(0,20)))
            i.paste(im,(l*110,0))

    return i

def ImageMerge(i1,i2,left,top):
    r,g,b,a = i1.split()
    t = Image.merge("RGB",(r,g,b))
    m = Image.merge("L",(a,))
    i2.paste(t,(left,top),m)
    return i2

def process(text, image):
    i = Image.open(image)
    t = sentence(text)
    w,h = t.size
    iw,ih = i.size
    
    if w > iw:
        nh = (iw/w)*h
        print("Resizing to fit - " + str((iw,nh)))    
        t = t.resize((iw,nh))
    c = (iw/2)-(w/2)
    
    return ImageMerge(t,i,c,0)


def Ransomify(text, image, saveas):
    if not saveas.endswith(".png"):
        saveas = saveas + ".png"
        
    print("Adding " + text + " to " + image + " and saving as " + saveas + ".")
    process(text, image).save(saveas, "PNG")
    print("Done.")
