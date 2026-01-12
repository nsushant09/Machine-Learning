import cv2
import face_recognition

passport_image = face_recognition.load_image_file("Passport Photo.jpg")
passport_face_locations = face_recognition.face_locations(passport_image)

if len(passport_face_locations) == 0:
    raise ValueError("No face found in Passport Photo.jpg")

passport_face_encoding = face_recognition.face_encodings(
    passport_image, known_face_locations=passport_face_locations
)[0]

video_capture = cv2.VideoCapture(0)

if not video_capture.isOpened():
    raise RuntimeError("Could not open video device. Check camera permissions.")

print("Press 'q' to quit.")

while True:
    result, video_frame = video_capture.read()
    if result is False:
        break

    rgb_frame = video_frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Compare live face with passport face
        matches = face_recognition.compare_faces(
            [passport_face_encoding], face_encoding, tolerance=0.6
        )
        face_distance = face_recognition.face_distance(
            [passport_face_encoding], face_encoding
        )[0]

        if matches[0]:
            label = f"Match ({face_distance:.2f})"
            color = (0, 255, 0)  # green
        else:
            label = f"No match ({face_distance:.2f})"
            color = (0, 0, 255)  # red

        # Draw rectangle and label
        cv2.rectangle(video_frame, (left, top), (right, bottom), color, 2)
        cv2.rectangle(video_frame, (left, bottom - 20), (right, bottom), color, cv2.FILLED)
        cv2.putText(
            video_frame,
            label,
            (left + 2, bottom - 5),
            cv2.FONT_HERSHEY_DUPLEX,
            0.5,
            (255, 255, 255),
            1,
        )

    # Show the frame
    cv2.imshow("Face Match", video_frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()


