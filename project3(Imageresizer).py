import cv2

# Configurable parameters
source="pic2019.jpg"
destination='newImage2.jpeg'
scale_percent =300

Image=cv2.imread(source , cv2.IMREAD_UNCHANGED)

#percent by which file resized
#cv2.imshow("Sandeep",Image)

#calculate 50 percent of original dimension
new_width=  int(Image.shape[1] * scale_percent/100 )
new_height=  int(Image.shape[0] * scale_percent/100 )


output= cv2.resize(Image ,(new_width,new_height))

cv2.imwrite( destination, output)
cv2.waitKey(0)