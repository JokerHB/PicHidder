import PicHide


def demo():

    hidder = PicHide.Hidder()

    hidder.hideZip('./demo/test_src.jpg', './demo/hide_src.zip', './demo/zip_dest.jpg')
    hidder.displayZip('./demo/zip_dest.jpg', './demo/zip_dest')

    hidder.hideString('./demo/test_src.jpg', 'hello world', './demo/str_dest.png')
    hidder.hideString('./demo/test_src.jpg', 'hhhhhhhhhhh', './demo/str_dest.bmp')
    hidder.displayString('./demo/str_dest.bmp')

    hidder.hideText('./demo/test_src.jpg', './demo/text_src.txt', './demo/text_dest.png')
    hidder.displayText('./demo/text_dest.png', './demo/text_dest.txt')

    hidder.hideImage('./demo/test_src.jpg', './demo/hide_src.jpg', './demo/hide_dest.png')
    hidder.displayImage('./demo/hide_dest.png', './demo/display_dest.png')


hidder = PicHide.Hidder()
hideFunction = '*11.hide zip in pic\n*12.hide string in pic\n*13.hide text in pic\n*14.hide pic in pic'
displayFunction = '*21.display zip in pic\n*22.display string in pic\n*23.display text in pic\n*24.display pic in pic'
starLine = '***************************************************'
function = 0

try:
    function = str(raw_input('please in put function:\n' + hideFunction + '\n' + starLine + '\n' + displayFunction + '\n'))
except BaseException:
    print 'please input the corrected number'

if function == '11':
    src = str(raw_input('please input the src pic path\n'))
    target = str(raw_input('please input the zip path\n'))
    dest = str(raw_input('please input the output file path\n'))

    hidder.hideZip(src, target, dest)

elif function == '12':
    src = str(raw_input('please input the src pic path\n'))
    content = str(raw_input('please input string content\n'))
    dest = str(raw_input('please input the output file path\n'))

    hidder.hideString(src, content, dest)

elif function == '13':
    src = str(raw_input('please input the src pic path\n'))
    target = str(raw_input('please input the text path\n'))
    dest = str(raw_input('please input the output file path\n'))

    hidder.hideText(src, target, dest)

elif function == '14':
    src = str(raw_input('please input the src pic path\n'))
    target = str(raw_input('please input the pic path\n'))
    dest = str(raw_input('please input the output file path\n'))

    hidder.hideImage(src, target, dest)

elif function == '21':
    print '#warning \n if u using windows, rename the filename into *.zip\n else using this function'
    src = str(raw_input('please input the src pic path\n'))
    target = str(raw_input('please input the target zip path\n'))

    hidder.displayZip(src, target)

elif function == '22':
    src = str(raw_input('please input the src pic path\n'))
    
    hidder.displayString(src)

elif function == '24':
    src = str(raw_input('please input the src pic path\n'))
    target = str(raw_input('please input the target pic path\n'))

    hidder.displayImage(src, target)

else:
    print 'please input the corrected number'
    exit(0)

exit(0)