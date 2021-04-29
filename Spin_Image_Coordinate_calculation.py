import cv2
import math

class Spin_Image_Coordinate_calculation:

    def __init__(self, img, Angle, keep_size):
        self.img_Spin_before = img
        self.img_Spin_after = img
        self.Angle = Angle
        self.keep_size = keep_size

    # 計算旋轉後座標
    def Coordinate_After_Spin(self, Spin_after_img,oldCoordinate):
        Angle_abs= abs(self.Angle)

        Width_Spin_before = self.img_Spin_before.shape[1]
        High_Spin_before = self.img_Spin_before.shape[0]
        Width_Spin_after_img = Spin_after_img.shape[1]
        HIGH_Spin_after_img = Spin_after_img.shape[0]
        # # y位移量
        y_displacement = int(HIGH_Spin_after_img - (High_Spin_before * math.cos(math.radians(Angle_abs))))
        # print("y_displacement=", y_displacement)
        # X位移量
        x_displacement = int((High_Spin_before * math.sin(math.radians(Angle_abs))))
        # print("x_displacement=", x_displacement)
        l_top = []
        r_down = []
        for i in range(len(oldCoordinate) - 1):
            for j in range(len(oldCoordinate[i])):
                if self.Angle < 0:
                    x1 = oldCoordinate[0][j][0] * math.cos(math.radians(Angle_abs)) - oldCoordinate[0][j][
                        1] * math.sin(math.radians(Angle_abs)) + x_displacement
                    y1 = oldCoordinate[0][j][1] * math.cos(math.radians(Angle_abs)) + oldCoordinate[0][j][
                        0] * math.sin(math.radians(Angle_abs))
                    x2 = oldCoordinate[1][j][0] * math.cos(math.radians(Angle_abs)) - oldCoordinate[1][j][
                        1] * math.sin(math.radians(Angle_abs)) + x_displacement
                    y2 = oldCoordinate[1][j][1] * math.cos(math.radians(Angle_abs)) + oldCoordinate[1][j][
                        0] * math.sin(math.radians(Angle_abs))

                else:
                    x1 = oldCoordinate[0][j][0] * math.cos(math.radians(Angle_abs)) + oldCoordinate[0][j][
                        1] * math.sin(math.radians(Angle_abs))
                    y1 = oldCoordinate[0][j][1] * math.cos(math.radians(Angle_abs)) - oldCoordinate[0][j][
                        0] * math.sin(math.radians(Angle_abs)) + y_displacement
                    x2 = oldCoordinate[1][j][0] * math.cos(math.radians(Angle_abs)) + oldCoordinate[1][j][
                        1] * math.sin(math.radians(Angle_abs))
                    y2 = oldCoordinate[1][j][1] * math.cos(math.radians(Angle_abs)) - oldCoordinate[1][j][
                        0] * math.sin(math.radians(Angle_abs)) + y_displacement
                l_top.append((int(x1), int(y1)))
                r_down.append((int(x2), int(y2)))
        return l_top, r_down

    # 旋轉圖片
    def rotation_point(self):
        cols = self.img_Spin_before.shape[1]
        rows = self.img_Spin_before.shape[0]
        M = cv2.getRotationMatrix2D((cols / 2, rows / 2), self.Angle, 1)
        if self.keep_size:

            # 根據旋轉矩陣進行仿射變換
            img_Spin_after = cv2.warpAffine(self.img_Spin_before, M, (cols, rows))
            return img_Spin_after
        else:
            heightNew = int(
                cols * math.fabs(math.sin(math.radians(self.Angle))) + rows * math.fabs(
                    math.cos(math.radians(self.Angle))))
            widthNew = int(
                rows * math.fabs(math.sin(math.radians(self.Angle))) + cols * math.fabs(
                    math.cos(math.radians(self.Angle))))
            M[0, 2] += (widthNew - cols) / 2
            M[1, 2] += (heightNew - rows) / 2
            img_Spin_after = cv2.warpAffine(self.img_Spin_before, M, (widthNew, heightNew))
            return img_Spin_after