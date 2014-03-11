from PIL import Image, ImageDraw
import numpy, sys, math



tolerance = 30

def isSimilar(rgb1, rgb2):
    diff1 = math.fabs(int(rgb1[0]) - int(rgb2[0]))
    diff2 = math.fabs(int(rgb1[1]) - int(rgb2[1]))
    diff3 = math.fabs(int(rgb1[2]) - int(rgb2[2]))
    #print str(rgb1) + " " + str(rgb2)
    #print str(diff1) + " " + str(diff2) + " " + str(diff2)
    if(diff1<=tolerance and diff2<=tolerance and diff3<=tolerance):
        return True
    return False


def compareSubImg(subImg, imgKey):
    count = 0
    accept = 0
    for subx in range (0, 2):
        for suby in range (0, 3):
            count+=1
            if( isSimilar(subImg[subx][suby], imgKey[subx][suby]) ):
                accept += 1
                if(accept > 5):
                    print "Accepted in a row: " + str(accept)

    if(accept > 5):
        print "Don't panic, Waldo has been located!"
        return True
    #print "----------------------------" + str(count)
    return False


def subimg(imgO1,imgO2):

    img2=numpy.asarray(imgO2)
    img1=numpy.asarray(imgO1)

    img1y=img1.shape[0]
    img1x=img1.shape[1]

    img2y=img2.shape[0]
    img2x=img2.shape[1]

    stopy=img2y-img1y+1
    stopx=img2x-img1x+1

    for x1 in range(0,stopx):
        for y1 in range(0,stopy):
            x2=x1+img1x
            y2=y1+img1y

            pic=img2[y1:y2,x1:x2]
            if(compareSubImg(pic, img1)):
                box = ( x1-33,y1-80,(x1 + 50),(y1 + 100) )
                cr = imgO2.crop(box)
                cr.show()
                dr = ImageDraw.Draw(imgO2)
                dr.rectangle(box, fill=(119, 243,9))
                imgO2.show()
                return x1, y1

    return False



key=Image.open('waldoAvgKey.tif')
big=Image.open(sys.argv[1])
tolerance = int(sys.argv[2])
print subimg(key, big)


