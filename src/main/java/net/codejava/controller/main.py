import sys
import numpy as np
import face_recognition
import cv2
import mysql.connector
import time
import urllib

var = 0
p = ''


mydb = mysql.connector.connect( 
    host="localhost", user="root", password="Sourav100", database="collegeproject")
mycursor = mydb.cursor()
mycursor.execute(
    "SELECT firstname,photos from user WHERE username = "+sys.argv[1])
for row in mycursor:
    n = row[0]
    p = row[1]

print(p)


video_capture = cv2.VideoCapture(0)
# address = "http://192.168.0.102:8080/video" # [from mobile camera]
# video_capture.open(address)
path = "user-photos\\"
path1 = path+sys.argv[1]+"\\"+p
sou_image = face_recognition.load_image_file(path1)
sou_image = cv2.cvtColor(sou_image, cv2.COLOR_RGB2BGR)
print(path1)
sou_face_encoding = face_recognition.face_encodings(sou_image)[0]
known_face_encoding = [sou_face_encoding]
known_face_names = [n]

name1 = ''
while True:

    ret, frame = video_capture.read()

    rgb_frame = frame[:, :, ::-1]
    face_location = face_recognition.face_locations(rgb_frame)
    face_encoding = face_recognition.face_encodings(rgb_frame, face_location)

    for(top, right, bottom, left), face_encoding in zip(face_location, face_encoding):
        matches = face_recognition.compare_faces(
            known_face_encoding, face_encoding)
        name = "Unknown"
        name1 = name
        face_distance = face_recognition.face_distance(
            known_face_encoding, face_encoding)
        best_match_index = np.argmin(face_distance)
        if matches[best_match_index]:

            name = known_face_names[best_match_index]
            name1 = name

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, bottom - 35),
                      (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, name, (left+6, bottom-6),
                    font, 1.0, (255, 255, 255), 1)


    cv2.imshow('Webcam_facerecognition', frame)

    if cv2.waitKey(10) & 0xFF == ord('k'):

        if (name1 == n and len(face_location)!=0):
            print(name1)
            var = 1
            # time.sleep(10)
            break
        else:
            print("else executed")
            time.sleep(10)
            break

video_capture.release()
cv2.destroyAllWindows()
# print("go") # [Uncomment if required]

if var == 1:
    print("match")
    text_file = open(
        "src\\main\\resources\\templates/out.txt", "w")
    text_file.write(sys.argv[1] + " 1")
    text_file.close()

else:
    print("not match")
    text_file = open(
        "src\\main\\resources\\templates/out.txt", "w")
    text_file.write(sys.argv[1] + " 0")
    text_file.close()
