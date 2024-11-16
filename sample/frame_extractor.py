import cv2
import time

# 打开视频文件
video_path = './test_video.mp4'  # 替换为您的视频文件路径
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error opening video file")
    exit()

frame_count = 0
fps = cap.get(cv2.CAP_PROP_FPS)
interval = int(fps)  # 保存间隔为1秒

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame_count += 1
    save_count = 0

    if frame_count % interval == 0:
        save_count += 1
        frame_name = f"frame_{save_count}.jpg"
        cv2.imwrite(frame_name, frame)
        print(f"Saved frame {frame_count}")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放视频对象
cap.release()

print("Frames saved: ", frame_count)