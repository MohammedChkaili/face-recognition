
from array import array
import os
from time import sleep
import time
import tkinter as tk
import numpy as np
import face_recognition as fr
import cv2
import mysql.connector
import tkinter.messagebox as MessageBox
from tkinter import *
from tkinter import filedialog 
import ntpath
from pathlib import Path



video_capture = cv2.VideoCapture(0)




directory="C:/Users/pc/Desktop/rf/faces"



l=[] 

for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
      print(os.path.join(directory, filename))
      
      l+=[os.path.join(directory, filename)]
print (l)

    
s=[]
for i in l:
  j= fr.load_image_file(i)
  s+=[j]


w=[]

for x in s:
  k=fr.face_encodings(x)[0]
  w+=[k]





m=[]

for a in w:

  y=a
  m+=[y]

known_face_encondings=m



file_name=[]
x=[]
for path in l:
  file_name.append(ntpath.basename(path))

for name in file_name:
    
    # finding the index where 
    # the last "." occurs
    k = name.rfind(".")
    x+=[name[:k]]
    
    print(name[:k])

print(x)

known_face_names=x




con = mysql.connector.connect(host="localhost", user="root", password="Mchkaili-80@80", database="app")
cursor = con.cursor()

cursor.execute("select name from admin")
result = cursor.fetchall() 


while True: 
    ret, frame = video_capture.read()
    
    rgb_frame = frame[:, :, ::-1]

    face_locations = fr.face_locations(rgb_frame)
    face_encodings = fr.face_encodings(rgb_frame, face_locations)

    

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

        matches = fr.compare_faces(known_face_encondings, face_encoding)

        name = "Unknown"

        face_distances = fr.face_distance(known_face_encondings, face_encoding)
       
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
        
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, bottom -35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        cv2.putText(frame, "Door state: ", (left - 60, bottom + 50), font, 1.0, (255, 255, 255), 1)
        
        con = mysql.connector.connect(host="localhost", user="root", password="Mchkaili-80@80", database="app")
        cursor = con.cursor()

        cursor.execute("select name from admin")
        ff = cursor.fetchall()
        ui=[]
        for line in ff:
        
          ui+=line  #liste des noms présents dans la base de données
        print(ui)
        
        
          
        print(name)
        print(x)     #x est la liste des noms que le système connait
        
           
        if name in ui:
                
                
                
                cv2.putText(frame, "Acces autorise", (left -40, bottom + 22), font, 1.0, (50, 225, 11), 1)
                cv2.putText(frame, " Locked", (left + 110, bottom +50), font, 1.0, (50, 225, 11), 1)
                illoww="Acces autorise"
                print(illoww)
                
               
               

                
           
                
        else:
                
                
                cv2.putText(frame, "Acces refuse ", (left + 1, bottom + 22), font, 1.0, (0, 0, 255), 1)
                cv2.putText(frame, "Unlocked", (left + 120, bottom +50), font, 1.0, (0, 0, 255), 1)
                illoww="Acces refusé"
                
                
                
                print(illoww)
                
          

      

    cv2.imshow('Facial recognition', frame)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



video_capture.release()
cv2.destroyAllWindows()



