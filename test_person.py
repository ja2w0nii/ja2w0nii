import torch
import cv2
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

img = cv2.imread('pic.jpg')
results = model(img)
results.save()

result = results.pandas().xyxy[0].to_numpy()
result = [item for item in result if item[6]=='person']

tmp_img = cv2.imread('pic.jpg')
print(tmp_img.shape)
cropped = tmp_img[int(result[4][1]):int(result[4][3]), int(result[4][0]):int(result[4][2])] #자르고 싶은 영역
print(cropped.shape)
cv2.imwrite('people5.png', cropped)
cv2.rectangle(tmp_img, (int(results.xyxy[0][4][0].item()), int(results.xyxy[0][4][1].item())), (int(results.xyxy[0][4][2].item()), int(results.xyxy[0][4][3].item())), (255,255,255))
cv2.imwrite('result5.png', tmp_img)