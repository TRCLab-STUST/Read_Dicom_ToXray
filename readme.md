#環境為資料夾中的 Xray_Painting_forDicome.yaml

主要功能由 "Dicom_Interpretation" 與 "Spin_Image_Coordinate_calculation" 提供，詳細功能如下

    """Dicom_Interpretation
    
    Dicom_Interpretation 用途讀取Dicom內容、取的Xray原圖、取的骨裂方框
    
    Dicom_Interpretation 使用方法 : dicom_Interpretation (dicom檔的I0000000路徑 , dicom檔的I0000001路徑)
    
    WHIRLING_BEFOR_IMG 為 Xray 原圖的像素點
    BEFOR_COORDINATE 為 Xray 骨裂位置方框座標 (左上角,右下角)
    """
    
    """ Spin_Image_Coordinate_calculation
    
    Spin_Image_Coordinate_calculation用途為旋轉圖片與計算旋轉後的方框做標
    
    *** img為要旋轉的圖片、Angle為要旋轉的角度 、 BEYOND_BOUNDARY 為是否要超出邊界(True、False)
    ANGLE_CLASS 使用方法 : SPIN_calcalation_coordinate (要旋轉的Xray ,要旋轉的角度"透過 ANGLE_SET 修改" ,旋轉前的骨裂座標
                                                                             ,是否超出邊界"透過 BEYOND_BOUNDARY 修改") ***
    WHIRLING_AFTER_IMG 為旋轉後的Xray
    AFTER_COORDINATE 為旋轉後的座標 (左上角,右下角)
    
    """