import os
import cv2
import matplotlib.pyplot as plt

# read image
image_path = os.path.join('.','data','bird.jpg')

img = cv2.imread(image_path)
# write image

cv2.imwrite(os.path.join('.','data','bird_out2.jpg'), img)

# visualize the image
# Convert the image from BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Display the image using matplotlib
plt.imshow(img_rgb)
plt.axis('off')  # Hide axes
plt.show()