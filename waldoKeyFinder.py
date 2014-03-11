from PIL import Image, ImageDraw
import numpy, sys

def subimg(imgO1,imgO2):

    img2=numpy.asarray(imgO2)

    img2y=img2.shape[0]
    img2x=img2.shape[1]

    stopy=img2y-2+1
    stopx=img2x-3+1

    for imgXkey in range(0,7):
        box = ( 0, (imgXkey*2), 3, (imgXkey*2)+2)
        cr = imgO1.crop(box)
        img1=numpy.asarray(cr)

        for x1 in range(0,stopx):
            for y1 in range(0,stopy):
                x2=x1+3
                y2=y1+2

                pic=img2[y1:y2,x1:x2]
                test=pic==img1

                if test.all():
                    #Show waldo and the full drawing
                    box = ( x1-33,y1-80,(x1 + 50),(y1 + 100) )
                    cr = imgO2.crop(box)
                    cr.show()
                    dr = ImageDraw.Draw(imgO2)
                    dr.rectangle(box, fill=(119, 243,9))
                    imgO2.show()
                    return x1, y1


    return False



key=Image.open('/home/blackarc/BenDouek_0684070_WaldoFinder/waldoKey.tif')
big=Image.open(sys.argv[1])
print subimg(key, big)
