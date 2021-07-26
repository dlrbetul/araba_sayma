import cv2

arkaplan = cv2.createBackgroundSubtractorMOG2()#arkaplan temizleme
capture = cv2.VideoCapture("arac.mp4")#video yakala
i = 0#başlangıç araç sayısı
minArea=2100#agirlik minimum
while True:
    ret, frame = capture.read()
    #print(frame.shape)# 720ye 1280
    fgmask = arkaplan.apply(frame, None, 0.021)#maskeleme
    erode=cv2.erode(fgmask,None,iterations=4)#gürültü icin
    moments=cv2.moments(erode,True)
    area=moments['m00']
    # dikey
    cv2.line(frame, (500, 0), (40, 800), (0, 255, 0), 2)
    cv2.line(frame, (540, 0), (200, 1280), (0, 255, 0), 2)
    # dikey  2
    cv2.line(frame, (540, 0), (210, 1280), (0, 255, 255), 2)
    cv2.line(frame, (580, 0), (650, 800), (0, 255, 255), 2)
    # dikey  3
    cv2.line(frame, (582, 0), (652, 800), (255, 255, 255), 2)
    cv2.line(frame, (610, 0), (970, 800), (255, 255, 255), 2)
    # dikey  4
    cv2.line(frame, (615, 0), (975, 800), (0, 0, 0), 2)
    cv2.line(frame, (645, 0), (1255, 800), (0, 0, 0), 2)
    # dikey  5
    cv2.line(frame, (650, 0), (1260, 800), (255, 0, 0), 2)
    cv2.line(frame, (700, 0), (1350, 600), (255, 0, 0), 2)
    # yatay
    cv2.line(frame, (0, 560), (1280, 560), (0, 0, 255), 2)
    cv2.line(frame, (0, 550), (1280, 550), (0, 0, 255), 2)
    # yatay 2
    cv2.line(frame, (0, 575), (1280, 575), (110, 100, 255), 2)
    cv2.line(frame, (0, 565), (1280, 565), (110, 100, 255), 2)
    # yatay 3
    cv2.line(frame, (0, 590), (1280, 590), (255, 100, 255), 2)
    cv2.line(frame, (0, 580), (1280, 580), (255, 100, 255), 2)
    # yatay 4
    cv2.line(frame, (0, 545), (1280, 545), (110, 255, 255), 2)
    cv2.line(frame, (0, 535), (1280, 535), (110, 255, 255), 2)
    # yatay 5
    cv2.line(frame, (0, 530), (1280, 530), (192, 168, 235), 2)
    cv2.line(frame, (0, 520), (1280, 520), (192, 168, 235), 2)
    if moments['m00'] >=minArea:#2100 seçtik
        x=int(moments['m10']/moments['m00'])
        y=int (moments['m01']/moments['m00'])
        print("mom :" + str(moments['m00']) + "x :" + str(x) + " y : " + str(y))
        if x>180 and x<380 and y>550 and y<560: # bu aralıklarda araç geccerse
            i=i+1
            print("dikey1: "+str(i))
        elif x>390 and x<590 and y>565 and y<575:# bu araliklarda araba geciyo
            i=i+1
            print("dikey2:"+str(i))
        elif x > 600 and x < 800 and y > 580 and y < 590:  # bu araliklarda araba geciyo
            i = i + 1
            print("dikey3:" + str(i))
        elif x>810 and x<1010 and y>535 and y<545:# bu araliklarda araba geciyo
            i=i+1
            print("dikey4:"+str(i))
        elif x > 1020 and x < 1220 and y > 520 and y < 530:  # bu araliklarda araba geciyo
            i = i + 1
            print("dikey5:" + str(i))
        cv2.putText(frame,'Sayi: %r' %i, (30,30), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 255, 255), 2)
        cv2.imshow("arac", frame)
        #cv2.imshow("fgmask", fgmask)

    key = cv2.waitKey(10)
    if key == ord('q'):
            break

capture.release()

cv2.destroyAllWindows()