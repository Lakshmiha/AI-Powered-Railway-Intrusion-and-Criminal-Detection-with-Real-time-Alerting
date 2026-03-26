# from ultralytics import YOLO
# import cv2
#
# # Path to your trained model
# model_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\runs\train\railway_foreign_object_detection\weights\best.pt"
#
# # Load the model
# model = YOLO(model_path)
#
# # Open webcam (use 0 for default, or 1, 2, etc. for external cameras)
# cap = cv2.VideoCapture(0)
#
# if not cap.isOpened():
#     print("❌ Error: Could not open camera.")
#     exit()
#
# print("🎥 Starting real-time detection... Press 'q' to quit.")
#
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("⚠️ Failed to grab frame.")
#         break
#
#     # Run YOLO prediction on the current frame
#     results = model(frame, conf=0.1)  # Adjust conf threshold as needed
#
#     # Draw predictions on the frame
#     annotated_frame = results[0].plot()
#
#     # Display the annotated frame
#     cv2.imshow("Railway", annotated_frame)
#
#     # Exit on pressing 'q'
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # Cleanup
# cap.release()
# cv2.destroyAllWindows()
# print("✅ Detection stopped and resources released.")

# from ultralytics import YOLO
# import cv2

# Path to your trained model
# model_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\runs\train\railway_foreign_object_detection\weights\best.pt"

# Path to the test image
# image_path=r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\m\railway-1\train\images\C_img_80198_jpg.rf.0234b29f00113e41284b442492201487.jpg"#other objects
# image_path=r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\m\railway-1\train\images\C_img_33971_jpg.rf.a1de02388809d66c26c7ddefe4909742.jpg"#vehicle,people
# image_path=r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\m\railway-1\train\images\C_img_34575_jpg.rf.d79a34a02e783904b6e8969d25e0f694.jpg"#stone
# image_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\m\railway-1\train\images\C_img_21406_jpg.rf.53249547904b96ff18140f88398a27f4.jpg"#stone
# image_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\m\railway-1\train\images\C_img_3251_jpg.rf.b7e13fd45d1d27341d1553d36c0e17f1.jpg"#vehicle
# image_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\m\railway-1\train\images\C_img_1198_jpg.rf.366ee0da9b0668ab6faf94e19d095237.jpg"#tree
# image_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\m\railway-1\train\images\_108970654_gettyimages-497844768-37-_jpg.rf.a6d62d5ab2a5627a42bd195a3eeb57c5.jpg"
# image_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\Railway-foreign-object-detection-1\test\images\image-61-_jpg.rf.28ec6f0c8e61b3954c09331ddaf445cb.jpg"

# Load the YOLO model
# model = YOLO(model_path)
#
# # Read the image
# image = cv2.imread(image_path)
#
# if image is None:
#     print("❌ Error: Could not load the image. Check the file path.")
#     exit()
#
# # Run detection on the image
# results = model(image, conf=0.1)  # Adjust confidence threshold if needed
#
# # Draw predictions on the image
# annotated_image = results[0].plot()
#
# # Show the annotated result
# cv2.imshow("Detection Result", annotated_image)
# cv2.waitKey(0)  # Wait until a key is pressed
# cv2.destroyAllWindows()
#
# # Optionally, save the annotated image
# output_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\output_result.jpg"
# # output_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\output_result.jpg"
# cv2.imwrite(output_path, annotated_image)
# print(f"✅ Detection complete. Result saved at: {output_path}")
from ultralytics import YOLO
import cv2

# -------------------------------
# Load your trained YOLO model
# -------------------------------
model_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\track_new\best.pt"
model = YOLO(model_path)

# Print model's class names
print("\n🔍 Model Classes Loaded from Weights:")
print(model.names)
print("------------------------------------\n")

# -------------------------------
# Open video file or webcam
# -------------------------------
cap = cv2.VideoCapture(r"C:\Users\amaya\Downloads\লাইন পরিবর্তন করে লুপ লাইনে ট্রেন নিয.mp4")
# cap = cv2.VideoCapture(r"C:\Users\amaya\Downloads\or worse yet, an ELECTRIC EEL 🙀 🎥： pjordan922 (TT), #shorts.mp4")
# cap = cv2.VideoCapture(r"C:\Users\amaya\Downloads\Elephant Saved After A Train Driver Noticed It Crossing Track _ Latest _ #Shorts _ CNN News18.mp4")

if not cap.isOpened():
    print("Error: Cannot access video source.")
    exit()

# -------------------------------
# Detection Loop (Only Railway Track)
# -------------------------------
print("Press 'q' to quit.")
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # Resize frame for better display
    frame = cv2.resize(frame, (500, 720))  # (width, height)

    # Run YOLO prediction
    results = model(frame, stream=True)

    # Draw only railway track detections
    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])

            # ✅ Only detect railway track (class id 2)
            if cls != 2:
                continue

            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)

            label = f"Railway Track {conf:.2f}"

            # Green box for railway track
            color = (0, 255, 0)

            # Draw box and label
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    # Display frame (resized)
    cv2.imshow("YOLO Railway Track Detection", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# -------------------------------
# Cleanup
# -------------------------------
cap.release()
cv2.destroyAllWindows()
