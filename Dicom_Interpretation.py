import pydicom
import cv2
import numpy as np

class dicom_Interpretation:

    def __init__(self, Dicom_FileName_o0, Dicom_FileName_o1):
        self.Dicom_FileName_o0 = Dicom_FileName_o0
        self.Dicom_FileName_o1 = Dicom_FileName_o1
        self.Dicom_0_nparray = None
        self.Dicom_1_nparray = None

    # 讀取dicom
    def openDicom(self):
        self.Dicom_0_nparray = pydicom.read_file(self.Dicom_FileName_o0)
        self.Dicom_1_nparray = pydicom.read_file(self.Dicom_FileName_o1)

    # 取得Xray PIXEL
    def getImgPixel(self):
        img_pixel = self.Dicom_0_nparray.pixel_array
        image_scale = cv2.convertScaleAbs(img_pixel - np.min(img_pixel),
                                          alpha=(255.0 / min(np.max(img_pixel) - np.min(img_pixel), 10000)))
        return image_scale
        # print(img_pixel)

    # 取得DICOM中骨裂方框位置
    def getCoordinate(self):
        POINT_TOP_LEFT = []
        POINT_LOWER_RIGHT = []
        for dataset_item in self.Dicom_1_nparray[0x70, 0x01][0][0x70, 0x09]:
            push_buffer = []
            for item in dataset_item[0x70, 0x22]:
                push_buffer.append(item)
                if len(push_buffer) >= 10:
                    # print(push_buffer)
                    x1 = int(push_buffer[0])
                    y1 = int(push_buffer[1])
                    x2 = int(push_buffer[2])
                    y2 = int(push_buffer[5])

                    if (x1 > x2):
                        x1 = int(push_buffer[2])
                        x2 = int(push_buffer[0])
                    if (y1 > y2):
                        y1 = int(push_buffer[5])
                        y2 = int(push_buffer[1])
                    point1 = (x1, y1)  # 左上（xmin、ymin）
                    point2 = (x2, y2)  # 右下
                    POINT_TOP_LEFT.append(point1)
                    POINT_LOWER_RIGHT.append(point2)

        return POINT_TOP_LEFT, POINT_LOWER_RIGHT