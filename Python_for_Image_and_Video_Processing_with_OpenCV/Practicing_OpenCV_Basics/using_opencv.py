import cv2

# Reading the image with cv2
img = cv2.imread("galaxy.jpg", 0)

print(type(img))
print(img)

# Resizing image
resized_image = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))

# Displaying the image
cv2.imshow("Galaxy", resized_image)

# Writing the image to a new file
cv2.imwrite("Galazy_resized_image.jpg", resized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

