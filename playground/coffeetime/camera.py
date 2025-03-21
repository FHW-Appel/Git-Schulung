import cv2

def main():
    # Open a connection to the USB camera (usually device 0)
    """ cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return """
    cap2 = cv2.VideoCapture(1)

    if not cap2.isOpened():
        print("Error: Could not open camera.")
        return
    while True:
        # Capture frame-by-frame
        """  ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        # Display the resulting frame
        cv2.imshow('USB Camera', frame) """
        # Capture frame-by-frame
        ret, frame2 = cap2.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        # Display the resulting frame
        cv2.imshow('USB Camera2', frame2)
        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()