import cv2


def camera():
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_file = './backend/data/camera_video.mp4'
    frame_rate = 24
    frame_size = (640, 480)
    video_writer = cv2.VideoWriter(output_file, fourcc, frame_rate, frame_size)

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Failed to open the camera")
        exit()

    while True:
        ret, frame = cap.read()

        if ret:
            cv2.imshow('Camera', frame)
            video_writer.write(frame)

        if cv2.waitKey(1) == ord('q'):
            break

    video_writer.release()
    cap.release()
    cv2.destroyAllWindows()
