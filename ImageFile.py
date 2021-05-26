import numpy as np
import struct
from PIL import Image

class ImageFile():

    def getBMP(self, filepath):
        # 先将位图打开
        f = open(filepath,'rb')             # 打开对应的文件
        # 下面部分用来读取BMP位图的基础信息
        f_type = str(f.read(2))             # 这个就可以用来读取 文件类型 需要读取2个字节
        file_size_byte = f.read(4)          # 这个可以用来读取文件的大小 需要读取4个字节
        f.seek(f.tell()+4)                  # 跳过中间无用的四个字节
        file_ofset_byte = f.read(4)         # 读取位图数据的偏移量
        f.seek(f.tell()+4)                  # 跳过无用的两个字节
        file_wide_byte = f.read(4)          # 读取宽度字节
        file_height_byte = f.read(4)        # 读取高度字节
        f.seek(f.tell()+2)                  # 跳过中间无用的两个字节
        file_bitcount_byte = f.read(4)      # 得到每个像素占位大小

        #下面就是将读取的字节转换成指定的类型
        f_size, = struct.unpack('i', file_size_byte)
        f_ofset, = struct.unpack('i', file_ofset_byte)
        f_wide, = struct.unpack('i', file_wide_byte)
        f_height, = struct.unpack('i', file_height_byte)
        f_bitcount, = struct.unpack('i', file_bitcount_byte)
        print("类型:", f_type, "大小:", f_size, "位图数据偏移量:", f_ofset, "宽度:", f_wide, "高度:", f_height, "位图:", f_bitcount)

        # 然后来读取颜色表
        color_table = np.empty(shape=[256, 4], dtype=int)
        f.seek(54) #跳过文件信息头和位图信息头
        for i in range(0, 256):
            b=struct.unpack('B', f.read(1))[0]
            g = struct.unpack('B', f.read(1))[0]
            r = struct.unpack('B', f.read(1))[0]
            alpha = struct.unpack('B', f.read(1))[0]
            color_table[i][0] = r
            color_table[i][1] = g
            color_table[i][2] = b
            color_table[i][3] = 255

        # 下面部分用来读取BMP位图数据区域,将数据存入numpy数组
        # 首先对文件指针进行偏移
        f.seek(f_ofset)
        # 因为图像是8位伪彩色图像，所以一个像素点占一个字节，即8位
        img = np.empty(shape=[f_height, f_wide, 4], dtype=int)
        cout = 0
        """
            然后就是来读取位图数据了，读取位图数据的时候，我们一定要注意，
            数据的排列方式是从左到右，从下到上！
            还有一个while循环，是用来判断行像素是否为4的倍数，
            如果不是我们还要将填充的用字节给读取扔掉
        """
        for y in range(0, f_height):
            for x in range(0,f_wide):
                cout = cout + 1
                index = struct.unpack('B', f.read(1))[0]
                img[f_height - y - 1, x] = color_table[index]
            while cout % 4 != 0:
                f.read(1)
                cout = cout+1
        f.close()
        return img

    def ndarry2image(self, ndarry):
        # ndarray 转 图片
        ndarry = ndarry.astype("uint8")
        # ndarry = cv2.cvtColor(ndarry, cv2.COLOR_BGR2RGB)
        ndarry = Image.fromarray(ndarry)
        ndarry = ndarry.toqpixmap()
        return ndarry