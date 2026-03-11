import cv2
import face_recognition

from DBConnection import Database


db=Database()
# Create your views here.

qry="SELECT * FROM `myapp_criminals`"
res= db.select(qry)


print(res)





knownimage=[]
knownids=[]
knownnames=[]


for i in res:
    s=i["photo"]
    s=s.replace("/media/","")
    pth="C:\\Users\\hariedappal\\PycharmProjects\\railwayobjectdetection\\media\\"+ s
    print(pth)
    try:
        picture_of_me = face_recognition.load_image_file(pth)
        print(pth)
        my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
        print(my_face_encoding)
        knownimage.append(my_face_encoding)
        knownids.append(i['id'])
        knownnames.append(i['criminalname'])
    except:
        pass








# define a video capture object
vid = cv2.VideoCapture(0)


while(True):

    ret, frame = vid.read()

    cv2.imwrite("a.jpg",frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    picture_of_others = face_recognition.load_image_file("a.jpg")
    # print(pth)
    others_face_encoding = face_recognition.face_encodings(picture_of_others)


    totface=len(others_face_encoding)



    for i in range(totface):
        print("inside check")
        res = face_recognition.compare_faces(knownimage, others_face_encoding[i], tolerance=0.45)
        print(res, "hello")

        cv2.imwrite("D:\\Smart_prison_camera-mdit\\Smart_prison_camera\\a.jpg", frame)

        mpath = "C:\\Users\\hariedappal\\PycharmProjects\\railwayobjectdetection\\media\\detect\\"
        from datetime import datetime

        fd = datetime.now().strftime("%Y%m%d%H%M%S")+ ".jpg"

        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

        print(fd)
        cv2.imwrite(mpath + fd, frame)
        p_ph = "/media/detect/" + fd

        print(p_ph,"ppppppppppppppppppppppppppppp")



        for j, match in enumerate(res):
            l = 0
            if match:
                print("Match found for criminal ID:", knownids[j])
                # e="INSERT INTO `myapp_criminalalert`(`date`,`time`,`PRISONER_id`)VALUES(CURRENT_DATE(),CURTIME(),'"+str(knownids[j])+"')"
                # # e="INSERT INTO  `app_alert` (`Date`,`Title`,`Descriptions`,`Time`,`WARDEN_id`)VALUE(NOW(), 'Escape from jail','"+knownnames[i]+"',CURTIME(),'1')"
                #
                # print(e)
                # db.insert(e)

                d="INSERT INTO `myapp_criminaldetection`(`date`,`photo`,`time`,`CRIMINAL_id`)VALUES(CURDATE(),'"+p_ph+"',CURTIME(),'"+str(knownids[j])+"')"
                # d="INSERT INTO `myapp_video`(`date`,`time`,`photo`,`PRISONER_id`)VALUES(CURDATE(),CURTIME(),'"+p_ph+"','"+str(knownids[j])+"')"
                print(d)

                db.insert(d)

            else:
                print("No Matching found for criminal:")
                # e = "INSERT INTO `myapp_criminalalert`(`date`,`time`,`PRISONER_id`)VALUES(CURRENT_DATE(),CURTIME(),'" + str(1) + "')"
                # e="INSERT INTO  `app_alert` (`Date`,`Title`,`Descriptions`,`Time`,`WARDEN_id`)VALUE(NOW(), 'Escape from jail','"+knownnames[i]+"',CURTIME(),'1')"

                # print(e)
                # db.insert(e)




vid.release()
# Destroy all the windows
cv2.destroyAllWindows()



# import cv2
# import face_recognition
#
# from DBConnection import Database
#
#
# db=Database()
# # Create your views here.
#
# qry="SELECT * FROM `myapp_prisoner`"
# res= db.select(qry)
#
#
# pid=[]
# name=[]
# photo=[]
# photolandmark=[]
#
#
# for i in res:
#
#
#     try:
#
#             mpath="C:\\Users\\muham\\PycharmProjects\\prison\\media\\"+ str(i['photo']).replace("/media/","")
#             known_image = face_recognition.load_image_file(mpath)
#             landmarks = face_recognition.face_encodings(known_image)[0]
#
#
#
#             # print(landmarks)
#             pid.append(i['id'])
#             name.append(i['name'])
#             photo.append(i['photo'])
#             photolandmark.append(landmarks)
#     except:
#         print("error loading photo of",i['name'] )
#
#
#
#
# vid = cv2.VideoCapture(0)
#
#
# while(True):
#
#     ret, frame = vid.read()
#
#     cv2.imwrite("a.jpg",frame)
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#     picture_of_others = face_recognition.load_image_file("a.jpg")
#     # print(pth)
#     others_face_encoding = face_recognition.face_encodings(picture_of_others)
#
#
#     totface=len(others_face_encoding)
#
#
#     ms=""
#
#     for i in range(totface):
#         print("inside check")
#         res = face_recognition.compare_faces(photolandmark, others_face_encoding[i], tolerance=0.5)
#         print(res, "hello")
#
#
#         for k in  range(0,len(res)):
#
#             if res[k] == True:
#
#                 ms= ms+ name[k]
#
#
#     if ms== "":
#         import pyttsx3
#
#         engine = pyttsx3.init()
#         engine.say(str(totface) +" Found .All persons are unknown")
#         engine.runAndWait()
#
#     else:
#
#         import pyttsx3
#
#         engine = pyttsx3.init()
#         engine.say(str(totface) + " Found . Detected persons are "+ ms)
#         engine.runAndWait()
#
#
#
#
#
#
#         import pyttsx3
#
#         engine = pyttsx3.init()
#         engine.say("I will speak this text")
#         engine.runAndWait()
#
#
# vid.release()
# # Destroy all the windows
# cv2.destroyAllWindows()