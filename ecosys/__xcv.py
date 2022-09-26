# import numpy as np
# import cv2 as cv2
# import cv2.aruco as aruco
# import os,time

# os.putenv('OPENCV_IO_MAX_IMAGE_PIXELS',f'{pow(2,40)}')


# def display(camera):
#     while (cv2.waitKey(1) & 0xFF) != ord('q'):
#         try:
#             frame = camera.shot()
#             cv2.imshow("Press q to end", frame)
#             time.sleep(0.04)
#         except:
#             pass

# def get_median_mean(row_biases):
#     if not np.any(row_biases): return np.array([])
#     y_bias = row_biases[:,0]
#     q1 = np.quantile(y_bias,0.25)
#     q3 = np.quantile(y_bias,0.75)
#     iqr = q3 - q1
#     norm = (y_bias>=q1-1.5*iqr) *(y_bias<=q3+1.5*iqr)
#     if not np.any(norm):
#         bias = np.mean(row_biases,axis=0)
#         bias = 0
#         print("not good results.")
#     else:
#         bias = np.mean(row_biases[norm],axis=0)
#     return bias


# def evaluate_lap(image):
#     imagegray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     return cv2.Laplacian(imagegray, cv2.CV_64F).var()
    
# def cv_display(cap):
#     while True:
#         try:
#             ret, frame = cap.read()
#             if ret:
#                 lcscores=evaluate_lap(frame)
#                 cv2.putText(frame,str(int(lcscores)),(50,50),1,2,(255,255,255),2)
#                 frame = cv2.resize(frame,(960,720))
#                 cv2.imshow("To Focus Press 'Q' to continue...",frame)
#         except:
#             pass
#         if cv2.waitKey(1) & 0xFF ==ord('q'):
#             break
#     cv2.destroyAllWindows()

# def img_display(img):
#     y,x,z = img.shape
#     if y>x: 
#         ny,nx = 720,int(720*x/y)
#     else:
#         ny,nx = int(y/x*960),960
#     while True:
#         frame = cv2.resize(img,(nx,ny))
#         cv2.imshow("To exit Press 'Q' ...",frame)
#         if cv2.waitKey(1) & 0xFF ==ord('q'):
#             break
#     cv2.destroyAllWindows()

# def img_display_origin(img):
#     while True:
#         cv2.imshow("To exit Press 'Q' ...",img)
#         if cv2.waitKey(1) & 0xFF ==ord('q'):
#             break
#     cv2.destroyAllWindows()



# class CvService():

#     def label_score(image):
#         _image = image.copy()
#         imagegray = cv2.cvtColor(_image,cv2.COLOR_BGR2GRAY)
#         _text = cv2.Laplacian(imagegray, cv2.CV_64F).var()
#         image = cv2.putText(image,str(int(_text)),(50,50),1,2,(255,255,255),2)
#         return image        

#     def get_img_score(imagegray):
#         score = cv2.Laplacian(imagegray, cv2.CV_64F).var()
#         return score
        
#     @classmethod
#     def get_gray_img_score(cls,imagegray):
#         if imagegray is not None:
#             return cls.get_img_score(imagegray)
#         else:
#             return 0
#     @classmethod
#     def get_color_img_score(cls,image_color):
#         if image_color is not None:
#             imagegray = cv2.cvtColor(image_color,cv2.COLOR_RGB2GRAY)
#             return cls.get_img_score(imagegray)
#         else:
#             return 0
#     @classmethod
#     def get_img_file_score(cls,filename):
#         imagegray = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
#         return cls.get_gray_img_score(imagegray)

#     def evaluate_lap(image):
#         imagegray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#         return cv2.Laplacian(imagegray, cv2.CV_64F).var()
#     @classmethod    
#     def cv_display(cls,cap_src):
#         while True:
#             try:
#                 ret, frame = cap_src()
#                 if ret:
#                     lcscores=cls.evaluate_lap(frame)
#                     cv2.putText(frame,str(int(lcscores)),(50,50),1,2,(255,255,255),2)
#                     frame = cv2.resize(frame,(960,720))
#                     cv2.imshow("To Focus Press 'Q' to continue...",frame)
#             except:
#                 pass
#             if cv2.waitKey(1) & 0xFF ==ord('q'):
#                 break
#         cv2.destroyAllWindows()
#     def img_display(img):
#         y,x,z = img.shape
#         if y>x: 
#             ny,nx = 720,int(720*x/y)
#         else:
#             ny,nx = int(y/x*960),960
#         while True:
#             frame = cv2.resize(img,(nx,ny))
#             cv2.imshow("To exit Press 'Q' ...",frame)
#             if cv2.waitKey(1) & 0xFF ==ord('q'):
#                 break
#         cv2.destroyAllWindows()
#     def img_display_origin(img):
#         while True:
#             cv2.imshow("To exit Press 'Q' ...",img)
#             if cv2.waitKey(1) & 0xFF ==ord('q'):
#                 break
#         cv2.destroyAllWindows()

# def get_img_score(imagegray):
#     score = cv2.Laplacian(imagegray, cv2.CV_64F).var()
#     return score
# def get_gray_img_score(imagegray):
#     if imagegray is not None:
#         return get_img_score(imagegray)
#     else:
#         return 0
# def get_color_img_score(image_color):
#     if image_color is not None:
#         imagegray = cv2.cvtColor(image_color,cv2.COLOR_RGB2GRAY)
#         return get_img_score(imagegray)
#     else:
#         return 0
# def get_img_file_score(filename):
#     imagegray = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
#     return get_gray_img_score(imagegray)
