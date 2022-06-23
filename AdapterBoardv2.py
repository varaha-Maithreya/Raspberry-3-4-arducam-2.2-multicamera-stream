    import RPi.GPIO as gp
    import os
    import cv2 as cv
    import numpy as np
    import time


    camNum = 4
    adapter_info = {"A": {"i2c_cmd": "i2cset -y 0 0x70 0x00 0x04",
                          "gpio_sta": [0, 0, 1],
                          },
                    "B": {
                        "i2c_cmd": "i2cset -y 0 0x70 0x00 0x05",
                        "gpio_sta": [1, 0, 1],
                    },
                    "C": {
                        "i2c_cmd": "i2cset -y 0 0x70 0x00 0x06",
                        "gpio_sta": [0, 1, 0],
                    },
                    "D": {
                        "i2c_cmd": "i2cset -y 0 0x70 0x00 0x07",
                        "gpio_sta": [1, 1, 0],
                    },
                    }
    camera = cv.VideoCapture(0)
    width = 320
    height = 240

    def __init__():
        gp.setwarnings(False)
        gp.setmode(gp.BOARD)
        gp.setup(7, gp.OUT)
        gp.setup(11, gp.OUT)
        gp.setup(12, gp.OUT)

    def choose_channel(index):
        channel_info = adapter_info.get(index)
        if channel_info is None:
            print("Can't get this info")
        os.system(channel_info["i2c_cmd"])  # i2c write
        gpio_sta = channel_info["gpio_sta"]  # gpio write
        gp.output(7, gpio_sta[0])
        gp.output(11, gpio_sta[1])
        gp.output(12, gpio_sta[2])

    def select_channel(index):
        channel_info = adapter_info.get(index)
        if channel_info is None:
            print("Can't get this info")
        gpio_sta = channel_info["gpio_sta"]  # gpio write
        gp.output(7, gpio_sta[0])
        gp.output(11, gpio_sta[1])
        gp.output(12, gpio_sta[2])

    def init(width, height):
        for i in range(camNum):
            height = height
            width = width
            choose_channel(chr(65 + i))
            camera.set(3, width)
            camera.set(4, height)
            ret, frame = camera.read()
            if ret == True:
                print("camera %s init OK" % (chr(65 + i)))
                pname = "image_" + chr(65 + i) + ".jpg"
                cv.imwrite(pname, frame)
                time.sleep(1)

    def preview():
        font = cv.FONT_HERSHEY_PLAIN
        fontScale = 1
        fontColor = (255, 255, 255)
        lineType = 1
        factor = 20
        black = np.zeros(((height + factor) * 2, width * 2, 3), dtype=np.uint8)
        i = 0
        while True:
            select_channel(chr(65 + i))
            ret, frame = camera.read()
            ret, frame = camera.read()
            ret, frame = camera.read()
            frame.dtype = np.uint8
            if i == 0:
                black[factor:factor + height, 0:width, :] = frame
                bottomLeftCornerOfText = (factor, factor)
                index = chr(65 + i)
            elif i == 1:
                black[factor:factor + height, width:width * 2, :] = frame
                bottomLeftCornerOfText = (factor + width, factor)
                index = chr(65 + i)
            elif i == 2:
                black[factor * 2 + height:factor * 2 + height * 2, 0:width, :] = frame
                bottomLeftCornerOfText = (factor, factor * 2 + height)
                index = chr(65 + i)
            elif i == 3:
                black[factor * 2 + height:factor * 2 + height * 2, width:width * 2, :] = frame
                bottomLeftCornerOfText = (factor + width, factor * 2 + height)
                index = chr(65 + i)
            i = i + 1
            if i == camNum:
                i = 0
            cv.putText(black, 'CAM ' + index, bottomLeftCornerOfText, font, fontScale, fontColor, lineType)
            cv.imshow("Arducam Multi Camera Demo", black)
            if cv.waitKey(1) & 0xFF == ord('q'):
                del frame
                camera.release()
                cv.destroyAllWindows()
                break


    def previewOne():
        font = cv.FONT_HERSHEY_PLAIN
        fontScale = 1
        fontColor = (255, 255, 255)
        lineType = 1
        factor = 20
        black = np.zeros(((height + factor) * 2, width * 2, 3), dtype=np.uint8)

        while True:
            select_channel(chr(65))
            ret, frame = camera.read()

            frame.dtype = np.uint8

            black[factor:factor + height, 0:width, :] = frame
            bottomLeftCornerOfText = (factor, factor)


            cv.putText(black, 'CAM ' + 'A', bottomLeftCornerOfText, font, fontScale, fontColor, lineType)
            cv.imshow("Arducam Multi Camera Demo", black)
            if cv.waitKey(1) & 0xFF == ord('q'):
                del frame
                camera.release()
                cv.destroyAllWindows()
                break


    def previewTwo():
        font = cv.FONT_HERSHEY_PLAIN
        fontScale = 1
        fontColor = (255, 255, 255)
        lineType = 1
        factor = 20
        black = np.zeros(((height + factor) * 2, width * 2, 3), dtype=np.uint8)

        while True:
            select_channel(chr(66))
            ret, frame = camera.read()

            frame.dtype = np.uint8


            black[factor:factor + height, width:width * 2, :] = frame
            bottomLeftCornerOfText = (factor + width, factor)

            cv.putText(black, 'CAM ' + 'B', bottomLeftCornerOfText, font, fontScale, fontColor, lineType)
            cv.imshow("Arducam Multi Camera Demo", black)
            if cv.waitKey(1) & 0xFF == ord('q'):
                del frame
                camera.release()
                cv.destroyAllWindows()
                break


    def previewThree():
        font = cv.FONT_HERSHEY_PLAIN
        fontScale = 1
        fontColor = (255, 255, 255)
        lineType = 1
        factor = 20
        black = np.zeros(((height + factor) * 2, width * 2, 3), dtype=np.uint8)
        i = 0
        while True:
            select_channel(chr(67))

            ret, frame = camera.read()
            frame.dtype = np.uint8


            black[factor * 2 + height:factor * 2 + height * 2, 0:width, :] = frame
            bottomLeftCornerOfText = (factor, factor * 2 + height)



            cv.putText(black, 'CAM ' + 'C', bottomLeftCornerOfText, font, fontScale, fontColor, lineType)
            cv.imshow("Arducam Multi Camera Demo", black)
            if cv.waitKey(1) & 0xFF == ord('q'):
                del frame
                camera.release()
                cv.destroyAllWindows()
                break


    def previewFour():
        font = cv.FONT_HERSHEY_PLAIN
        fontScale = 1
        fontColor = (255, 255, 255)
        lineType = 1
        factor = 20
        black = np.zeros(((height + factor) * 2, width * 2, 3), dtype=np.uint8)

        while True:
            select_channel(chr(68))

            ret, frame = camera.read()
            frame.dtype = np.uint8


            black[factor * 2 + height:factor * 2 + height * 2, width:width * 2, :] = frame
            bottomLeftCornerOfText = (factor + width, factor * 2 + height)


            cv.putText(black, 'CAM ' + 'D', bottomLeftCornerOfText, font, fontScale, fontColor, lineType)
            cv.imshow("Arducam Multi Camera Demo", black)
            if cv.waitKey(1) & 0xFF == ord('q'):
                del frame
                camera.release()
                cv.destroyAllWindows()
                break

        previewOne()
        previewTwo()
        previewThree()
        previewFour()
