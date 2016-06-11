from PIL import Image, ImageOps
import stepic
import os

class Hidder(object):

    #*********************** Coding ****************************

    # hide zip in image
    # srcPath: input image path
    # targetPath: hidden zip path
    # outputPath: final output path, default: ./final.jpg/png/bmp/...etc
    def hideZip(self, srcPath, targetPath, outputPath):
        # open the file
        try:
            im_src = open(srcPath, 'rb')
        except IOError:
            print 'can not open the %s' % srcPath
            exit(0)

        try:
            zip_src = open(targetPath, 'rb')
        except IOError:
            print 'can not open the %s' % targetPath
            exit(0)
        try:
            im_dest = open(outputPath, 'wb')
        except IOError:
            print 'can not create the %s' % outputPath

        im_dest.write(im_src.read() + zip_src.read())

        im_dest.close()
        zip_src.close()
        im_src.close()

    # hide image in image
    # srcPath: input image path
    # targetPath: hidden image path
    # outputPath: final output path, default: ./final.jpg/png/bmp/...etc
    def hideImage(self, srcPath, targetPath, outputPath, s=4):
        try:
            im_src = open(srcPath, 'rb')
        except IOError:
            print 'can not open the %s' % srcPath
            exit(0)
        try:
            im_dest = open(outputPath, 'wb')
        except IOError:
            print 'can not open the %s' % outputPath
            exit(0)
        im_dest.write(im_src.read())
        im_dest.close()
        im_src.close()
        try:
            src = Image.open(outputPath)
        except IOError:
            print 'can not open the %s' % srcPath
            exit(0)

        key = ImageOps.autocontrast(Image.open(targetPath).resize(src.size))

        for x in range(src.size[0]):
            for y in range(src.size[1]):
                p = src.getpixel((x,y))
                q = key.getpixel((x,y))
                r = p[0] - (p[0] % s) + (s * q[0] / 255)
                g = p[1] - (p[1] % s) + (s * q[1] / 255)
                b = p[2] - (p[2] % s) + (s * q[2] / 255)
                src.putpixel((x,y), (r, g, b))
        src.save(outputPath)

    # hide text in image
    # srcPath: input image path
    # targetPath: hidden text path
    # outputPath: final output path, default: ./final.jpg/png/bmp/...etc
    def hideText(self, srcPath, targetPath, outputPath):
        try:
            text_src = open(targetPath, 'rb')
        except IOError:
            print 'can not open the %s' % targetPath
            exit(0)
        self.hideString(srcPath, text_src.read(), outputPath)
        text_src.close()

    # hide text in image
    # srcPath: input image path
    # targetPath: hidden text path
    # outputPath: final output path, default: ./final.jpg/png/bmp/...etc
    def hideString(self, srcPath, string, outputPath):
        try:
            im_src = Image.open(srcPath)
        except IOError:
            print 'can not open the %s' % srcPath
            exit(0)

        im_src = stepic.encode(im_src, string)
        im_src.save(outputPath)
        im_src.close()

    #*********************** Decode ****************************

    # display zip in image
    # srcPath: input image path
    # targetPath: output zip path, default:
    def displayZip(self, srcPath, targetPath):
        os.system('unzip -o ' + srcPath + ' -d ' + targetPath)


    # display Image in image
    # srcPath: input image path
    # targetPath: output zip path, default:
    def displayImage(self, srcPath, targetPath, s=4):
        try:
            im_src = open(srcPath, 'rb')
        except IOError:
            print 'can not open the %s' % srcPath
            exit(0)
        try:
            im_dest = open(targetPath, 'wb')
        except IOError:
            print 'can not open the %s' % targetPath
            exit(0)

        im_dest.write(im_src.read())
        im_src.close()
        im_dest.close()
        try:
            src = Image.open(targetPath)
        except IOError:
            print 'can not open the %s' % targetPath
            exit(0)
        for x in range(src.size[0]):
            for y in range(src.size[1]):
                p = src.getpixel((x,y))
                r = (p[0] % s) * 255 / s;
                g = (p[1] % s) * 255 / s;
                b = (p[2] % s) * 255 / s;
                src.putpixel((x,y), (r, g, b))
        src.save(targetPath);

    # display text in image
    # srcPath: input image path
    def displayText(self, srcPath, targetPath):
        try:
            text_dest = open(targetPath, 'wb')
        except IOError:
            print 'can not create the %s' % targetPath
            exit(0)

        text_dest.write(self.displayString(srcPath, False))
        text_dest.close()

    # display string in image
    # srcPath: input image path
    # targetPath: output zip path, default:
    def displayString(self, srcPath, isDisplay=True):
        try:
            im_src = Image.open(srcPath)
        except IOError:
            print 'can not open the %s' % srcPath
            exit(0)

        # im_src.show()

        str_dest = stepic.decode(im_src)
        data = str_dest.decode()
        if isDisplay:
            print data
        return data
