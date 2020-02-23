import cv2
import glob
 
image=glob.glob('*.jpg')
#li=['a.jpg','b.jpg','c.jpg','d.jpg','e.jpg']
for i in image:
    img = cv2.imread(i,1)
    # print(type(img))
    # print(img.shape)
    # print(img)
    resized_img = cv2.resize(img,(1600,900))
    cv2.imwrite(f'resized{i}.jpg',resized_img)



    # cv2.imshow("my image",resized_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()