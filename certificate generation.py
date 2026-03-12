import cv2

template = cv2.imread('certificate.png')
cv2.putText(template, 'Hello', (107,88), cv2.FONT_HERSHEY_TRIPLEX, 2, (51, 65, 102), 2, cv2.LINE_AA)
#cv2.putText(template, '23', (631,1245), cv2.FONT_HERSHEY_TRIPLEX, 2, (51, 65, 102), 2, cv2.LINE_AA)
cv2.imwrite(f'C:\\Users\\prano\\OneDrive\\Desktop\\NEIL\\Quizzenberg Project file\\Generated certificates\\hello.png',template)
print('Processing Certificate...')