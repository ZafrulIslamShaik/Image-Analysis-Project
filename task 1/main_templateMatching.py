import cv2
import matchingAlgorithm

def main():
    # reading source image and template image
    sourceImage = cv2.imread("Z:\img analysis project final\images/3.jpg")
    templateImage = cv2.imread("Z:\img analysis project final\words/6.jpg")
    print(templateImage.shape)

    # scaling the template
    IMG_SIZE = 31
    resizedTemp = cv2.resize(templateImage, (IMG_SIZE, IMG_SIZE))
    # cv2.imshow("template image",new_array)

    gray = cv2.cvtColor(sourceImage, cv2.COLOR_RGB2GRAY)
    templateImage1 = cv2.cvtColor(resizedTemp, cv2.COLOR_RGB2GRAY)
    h_temp, w_temp = templateImage1.shape

    # call of template matching function
    pt = matchingAlgorithm.template_matching_NCC(gray, templateImage1)
    # drawing the rectangle for the template found
    cv2.rectangle(sourceImage, (pt[0], pt[1]), (pt[0] + w_temp, pt[1] + h_temp), (0, 0, 256), 2)

    # output of template matching
    cv2.imshow("output1image.png", sourceImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()