import cv2
import os
import matplotlib.pyplot as plt
from Dicom_Interpretation import dicom_Interpretation
from Spin_Image_Coordinate_calculation import Spin_Image_Coordinate_calculation

if __name__ == '__main__':
    dicom_o0 = "./5844847/I0000000"
    dicom_o1 = "./5844847/I0000001"
    """
       DICOM_READ_CLASS 用途讀取Dicom內容、取的Xray原圖、取的骨裂方框

       *** DICOM_READ_CLASS 使用方法 : dicom_Interpretation (dicom檔的I0000000路徑 , dicom檔的I0000001路徑) ***

       WHIRLING_BEFOR_IMG 為 Xray 原圖的像素點
       BEFOR_COORDINATE 為 Xray 骨裂位置方框座標 (左上角,右下角)
       """
    DICOM_READ_CLASS = dicom_Interpretation(dicom_o0, dicom_o1)

    DICOM_READ_CLASS.openDicom()

    WHIRLING_BEFOR_IMG = DICOM_READ_CLASS.getImgPixel()

    BEFOR_COORDINATE = DICOM_READ_CLASS.getCoordinate()

    # 畫出骨裂方框
    for i in range(len(BEFOR_COORDINATE[0])):
        cv2.rectangle(WHIRLING_BEFOR_IMG, BEFOR_COORDINATE[0][i], BEFOR_COORDINATE[1][i], (0, 0, 255), 10)
    plt.imshow(WHIRLING_BEFOR_IMG)
    plt.show()

    # 旋轉圖片與計算旋轉後方框座標

    """ 
    ANGLE_CLASS 用途為旋轉圖片與計算旋轉後的方框做標

    *** ANGLE_SET 為要旋轉的角度 、 BEYOND_BOUNDARY 為是否要超出邊界(True、False)
    ANGLE_CLASS 使用方法 : SPIN_calcalation_coordinate (要旋轉的Xray ,要旋轉的角度"透過 ANGLE_SET 修改" ,旋轉前的骨裂座標
                                                                             ,是否超出邊界"透過 BEYOND_BOUNDARY 修改") ***
    WHIRLING_AFTER_IMG 為旋轉後的Xray
    AFTER_COORDINATE 為旋轉後的座標 (左上角,右下角)

    """

    ANGLE_SET = -175
    BEYOND_BOUNDARY = False

    # ANGLE_CLASS
    ANGLE_CLASS = Spin_Image_Coordinate_calculation(WHIRLING_BEFOR_IMG, ANGLE_SET, BEYOND_BOUNDARY)

    WHIRLING_AFTER_IMG = ANGLE_CLASS.rotation_point()

    AFTER_COORDINATE = ANGLE_CLASS.Coordinate_After_Spin(WHIRLING_AFTER_IMG, BEFOR_COORDINATE)

    # 繪製旋轉後座標
    for j in range(len(AFTER_COORDINATE[0])):
        cv2.rectangle(WHIRLING_AFTER_IMG, AFTER_COORDINATE[0][j], AFTER_COORDINATE[1][j], (255, 0, 0), 10)

    # cv2.imwrite("AFTOR11.png", WHIRLING_AFTER_IMG)

    plt.imshow(WHIRLING_AFTER_IMG)
    plt.show()