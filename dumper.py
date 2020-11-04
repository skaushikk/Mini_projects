import os
import sys
path = r'D:\CourseWork\Harward CS109\a-2017\Lectures'

f = []
for (dirpath, dirnames, filenames) in os.walk(path):
    print(filenames)
    print(dirpath)
    #
    f.extend(filenames)
    # break

# from PyPDF2 import PdfFileMerger
#
# merger = PdfFileMerger()
# for pdf in f:
#     if pdf[-3:] == 'pdf':
#         merger.append(path + '\\' + pdf)
#
# merger.write(path + '\\' + "final.pdf")
# merger.close()