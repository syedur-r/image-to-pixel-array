import cv2
import csv
import easygui
import glob


# csv columns - change emotion number according to which data you load - same for usage
emotion = 0
usage = "Training"

# csv file
f = open('result.csv', 'w', newline='')
writer = csv.writer(f)
# header to match the FER csv
header = ['emotion', 'pixels', 'Usage']
writer.writerow(header)

# load directory using a GUI
path = easygui.diropenbox()

# loop through each image file
for img in glob.glob(path+"/*.png"):
    # load single image
    image = cv2.imread(img)

    # grayscale conversion
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # resize to 48 x 48
    dim = (48, 48)
    resized = cv2.resize(gray, dim, interpolation = cv2.INTER_AREA)

    # 2D to 1D array
    k = []
    for i in range(48):
        for j in range(48):
            k.append(resized[i,j])

    # print(k)

    # get rid of brackets and commas of the k list
    content = ' '.join(map(str, k))
    # each row's data:
    data = [emotion, content, usage]
    # write a row after each iteration
    writer.writerow(data)

# close csv
f.close()

# kept that in case we need to reuse: save or view the output images
# cv2.imwrite("out.png", resized)

# cv2.imshow('ko',resized)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
