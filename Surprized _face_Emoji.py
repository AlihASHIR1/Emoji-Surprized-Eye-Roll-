import cv2 as cv
import numpy as np

## Emoji Setting
blank=np.zeros(shape=[550,650,3],dtype=np.uint8)
blank[:]=(255,255,200)
circle=cv.circle(blank,(320,270),160,(0,255,255),cv.FILLED)
eyebrow1=cv.ellipse(blank,(255,170),(0,30),85,0,360,(0,0,0),2)
eyebrow2=cv.ellipse(blank,(395,170),(0,30),275,0,360,(0,0,0),2)
eye1=cv.circle(blank,(250,220),35,(255,255,255),cv.FILLED)
eye2=cv.circle(blank,(395,220),35,(255,255,255),cv.FILLED)
eyeball1=cv.circle(blank,(250,220),14,(0,0,0),cv.FILLED)
eyeball2=cv.circle(blank,(395,220),14,(0,0,0),cv.FILLED)
mouth=cv.ellipse(blank,(320,330),(60,80),90,0,360,(25,100,180),cv.FILLED)
emoji=cv.putText(blank,"Suprized Faced emoji",(150,75),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
cv.imshow('circle',emoji)
cv.waitKey(0)