import cv2 as cv
import numpy as np

## Emoji Setting
blank=np.zeros(shape=[550,650,3],dtype=np.uint8)
blank[:]=(255,255,200)
circle=cv.circle(blank,(310,270),160,(0,255,255),cv.FILLED)
eye1=cv.circle(blank,(245,230),35,(255,255,255),cv.FILLED)
eye2=cv.circle(blank,(380,230),35,(255,255,255),cv.FILLED)
eyeball1=cv.circle(blank,(245,205),14,(0,0,0),cv.FILLED)
eyeball2=cv.circle(blank,(380,205),14,(0,0,0),cv.FILLED)
mouth=cv.line(blank,(250,330),(380,330),(25,100,180),5)
emoji=cv.putText(blank,"Eye Roll emoji",(150,75),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
cv.imshow('circle',emoji)
cv.waitKey(0)