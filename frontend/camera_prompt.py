import cv2

# Set the video codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Specify the codec (XVID is a widely supported codec)
output_file = 'output.avi'  # Output video file name
frame_rate = 30  # Number of frames per second
frame_size = (640, 480)  # Frame size (width, height)
video_writer = cv2.VideoWriter(output_file, fourcc, frame_rate, frame_size)

# Open the default camera
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Failed to open the camera")
    exit()

# Read and write video frames until the user presses 'q'
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame is read correctly, write it to the output video file
    if ret:
        # Display the frame (optional)
        cv2.imshow('Camera', frame)

        # Write the frame to the video file
        video_writer.write(frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoWriter and capture object, and close all windows
video_writer.release()
cap.release()
cv2.destroyAllWindows()
