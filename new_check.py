# from ultralytics import YOLO
# import cv2
# import numpy as np
# import os
# from datetime import datetime
# from DBConnection import Database
#
# db = Database()
#
# # -------------------------------
# # Model paths
# # -------------------------------
# foreign_object_model_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\runs\train\railway_foreign_object_detection\weights\best.pt"
# track_model_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\track\best.pt"
#
# # -------------------------------
# # Video path
# # -------------------------------
# video_path = r"C:\Users\amaya\Downloads\Elephant Saved After A Train Driver Noticed It Crossing Track _ Latest _ #Shorts _ CNN News18.mp4"
#
# # video_path = r"C:\Users\amaya\Downloads\or worse yet, an ELECTRIC EEL 🙀 🎥： pjordan922 (TT), #shorts.mp4"
# output_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\output_combined_video.mp4"
#
# # -------------------------------
# # Load both YOLO models
# # -------------------------------
# object_model = YOLO(foreign_object_model_path)
# track_model = YOLO(track_model_path)
#
# # -------------------------------
# # Open video
# # -------------------------------
# cap = cv2.VideoCapture(video_path)
# if not cap.isOpened():
#     print("❌ Error: Could not open the video. Check the file path.")
#     exit()
#
# fps = int(cap.get(cv2.CAP_PROP_FPS))
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
#
# # -------------------------------
# # Helper: Compute IoU (intersection over union)
# # -------------------------------
# def compute_iou(box1, box2):
#     x1 = max(box1[0], box2[0])
#     y1 = max(box1[1], box2[1])
#     x2 = min(box1[2], box2[2])
#     y2 = min(box1[3], box2[3])
#
#     inter_w = max(0, x2 - x1)
#     inter_h = max(0, y2 - y1)
#     inter_area = inter_w * inter_h
#
#     area1 = (box1[2] - box1[0]) * (box1[3] - box1[1])
#     area2 = (box2[2] - box2[0]) * (box2[3] - box2[1])
#     union = area1 + area2 - inter_area
#
#     return inter_area / (union + 1e-6)
#
# # -------------------------------
# # Process video frame by frame
# # -------------------------------
# frame_count = 0
#
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#     frame_count += 1
#
#     # Run both detections
#     results_objects = object_model(frame, conf=0.35, verbose=False)
#     results_track = track_model(frame, conf=0.3, verbose=False)
#
#     # Extract boxes
#     object_boxes = results_objects[0].boxes.xyxy.cpu().numpy() if results_objects[0].boxes else []
#     track_boxes = results_track[0].boxes.xyxy.cpu().numpy() if results_track[0].boxes else []
#
#     overlap_found = False
#
#     # ✅ Proceed only if at least one track is detected
#     if len(track_boxes) > 0:
#         # Get track labels (class IDs and names)
#         track_classes = results_track[0].boxes.cls.cpu().numpy() if results_track[0].boxes else []
#         track_names = results_track[0].names  # {id: name}
#
#         print(len(track_boxes), f"Track(s) detected in this frame:{track_names}")
#
#         for obj_box in object_boxes:
#             for idx, track_box in enumerate(track_boxes):
#                 track_label_id = int(track_classes[idx]) if idx < len(track_classes) else -1
#                 track_label_name = track_names.get(track_label_id, "Unknown")
#
#                 iou = compute_iou(obj_box, track_box)
#
#                 if iou > 0.1:  # overlap threshold
#                     overlap_found = True
#                     overlapped_obj = obj_box
#                     print(f"⚠ Overlap Detected with Track Label: {track_label_name}")
#                     break
#             if overlap_found:
#                 break
#     else:
#         overlap_found = False  # no track at all → skip saving
#
#     # -------------------------------
#     # Draw detections on frame
#     # -------------------------------
#     combined_frame = frame.copy()
#     combined_frame = results_track[0].plot(img=combined_frame, line_width=2)
#     combined_frame = results_objects[0].plot(img=combined_frame, line_width=2)
#
#     # Draw labels for tracks
#     if len(track_boxes) > 0:
#         for idx, track_box in enumerate(track_boxes):
#             x1, y1, x2, y2 = [int(x) for x in track_box[:4]]
#             track_label_id = int(track_classes[idx]) if idx < len(track_classes) else -1
#             track_label_name = track_names.get(track_label_id, "Unknown")
#             cv2.putText(combined_frame, f"{track_label_name}", (x1, y1 - 10),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
#
#     # Draw labels for objects
#     for obj_box in object_boxes:
#         x1, y1, x2, y2 = [int(x) for x in obj_box[:4]]
#         cv2.putText(combined_frame, "Object Detected", (x1, y1 - 10),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
#
#     # -------------------------------
#     # Handle overlap / alert condition
#     # -------------------------------
#     if overlap_found:
#         cv2.putText(combined_frame, "⚠ OBJECT ON TRACK", (30, 50),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)
#
#         # Save full frame to media folder
#         mpath = r"C:\Users\amaya\Desktop\firstproject-mdit\firstproject\media\obj_detect\\"
#         os.makedirs(mpath, exist_ok=True)
#         fd = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
#         full_img_path = os.path.join(mpath, fd)
#         cv2.imwrite(full_img_path, combined_frame)
#
#         # ✅ Crop and save only the overlapped object (optional)
#         x1, y1, x2, y2 = [int(x) for x in overlapped_obj[:4]]
#         cropped_obj = frame[y1:y2, x1:x2]
#         crop_path = os.path.join(mpath, "crop_" + fd)
#         cv2.imwrite(crop_path, cropped_obj)
#
#         # Relative path for Django
#         p_ph = "/media/obj_detect/" + fd
#
#         # Timestamp
#         timestamp = datetime.now()
#         date_str = timestamp.strftime("%Y-%m-%d")
#         time_str = timestamp.strftime("%H:%M:%S")
#
#         # Insert DB record
#         place = "kozhikode"
#         q = ("INSERT INTO myapp_objectdetection(`log`, `place`, `time`, `date`) "
#              f"VALUES ('{p_ph}','{place}','{time_str}','{date_str}')")
#         db.insert(q)
#
#         print(f"🧾 Object on track! Frame {frame_count} saved: {p_ph}")
#     else:
#         cv2.putText(combined_frame, "No Object on Track", (30, 50),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
#         print(f"✅ Frame {frame_count}: No overlap (Objects={len(object_boxes)}, Tracks={len(track_boxes)})")
#
#     # -------------------------------
#     # Display + save output video
#     # -------------------------------
#     cv2.imshow("Railway Detection (Video)", combined_frame)
#     out.write(combined_frame)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # -------------------------------
# # Cleanup
# # -------------------------------
# cap.release()
# out.release()
# cv2.destroyAllWindows()
# print(f"\n✅ Video processing complete. Output saved at: {output_path}")

from ultralytics import YOLO
import cv2
import numpy as np
import os
from datetime import datetime
from DBConnection import Database

db = Database()

# -------------------------------
# Model paths
# -------------------------------
foreign_object_model_path = r"C:\Users\hariedappal\Downloads\mdit_foreignobjects-object-detection\mdit_foreignobjects\m\runs\train\railway_foreign_object_detection\weights\best.pt"
# foreign_object_model_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\runs\train\railway_foreign_object_detection\weights\best.pt"
# track_model_path = r"C:\Users\amaya\Desktop\firstproject-mdit\checking\Rail_track_checking\runs\train\railway_track_detection\weights\best.pt"
track_model_path = r"C:\Users\hariedappal\Downloads\mdit_foreignobjects-object-detection\mdit_foreignobjects\track_new\best.pt"
# track_model_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\track_new\best.pt"
# track_model_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\track\best.pt"

# -------------------------------
# Video path
# -------------------------------
# video_path = r"C:\Users\amaya\Downloads\Generated File November 03, 2025 - 2_00PM.mp4"#tree
# video_path = r"C:\Users\amaya\Downloads\38833FF26BA1D.UnigramPreview_g9c9v27vpyspw!App\Generated File November 03, 2025 - 1_08PM.mp4"
# video_path = r"C:\Users\amaya\Downloads\Generated File November 03, 2025 - 12_59PM.mp4"#car
# video_path = r"C:\Users\amaya\Downloads\Generated File November 03, 2025 - 12_58PM.mp4"
# video_path = r"C:\Users\amaya\Downloads\vecteezy_an-asian-mother-and-daughters-run-together-on-the-railroad_6303385.mov"
# video_path = r""
# video_path = r"C:\Users\amaya\Downloads\লাইন পরিবর্তন করে লুপ লাইনে ট্রেন নিয.mp4"

# video_path = r"C:\Users\amaya\Downloads\Must be the god with this guy #train #car #nearly.mp4"

video_path = r"C:\Users\hariedappal\Downloads\Elephant_Saved_After_A_Train_Driver_Noticed_It_Crossing_Track_Latest.mp4"
# video_path = r"C:\Users\amaya\Downloads\or worse yet, an ELECTRIC EEL 🙀 🎥： pjordan922 (TT), #shorts.mp4"
# video_path = r"C:\Users\amaya\Downloads\Elephant Saved After A Train Driver Noticed It Crossing Track _ Latest _ #Shorts _ CNN News18.mp4"
output_path = r"C:\Users\hariedappal\Downloads\mdit_foreignobjects-object-detection\mdit_foreignobjects\output_combined_video.mp4"
# output_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\output_combined_video.mp4"

# -------------------------------
# Load both YOLO models
# -------------------------------
object_model = YOLO(foreign_object_model_path)
track_model = YOLO(track_model_path)
print(object_model.names)

# -------------------------------
# Open video
# -------------------------------
cap = cv2.VideoCapture(r"C:\Users\hariedappal\Downloads\Elephant_Saved_After_A_Train_Driver_Noticed_It_Crossing_Track_Latest.mp4")
# cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("❌ Error: Could not open the video. Check the file path.")
    exit()

fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# -------------------------------
# Helper: Compute IoU (intersection over union)
# -------------------------------
def compute_iou(box1, box2):
    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[2], box2[2])
    y2 = min(box1[3], box2[3])

    inter_w = max(0, x2 - x1)
    inter_h = max(0, y2 - y1)
    inter_area = inter_w * inter_h

    area1 = (box1[2] - box1[0]) * (box1[3] - box1[1])
    area2 = (box2[2] - box2[0]) * (box2[3] - box2[1])
    union = area1 + area2 - inter_area

    return inter_area / (union + 1e-6)

# -------------------------------
# Process video frame by frame
# -------------------------------
frame_count = 0

while True:

    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.resize(frame, (500, 720))  # (width, height)

    if not ret:
        break
    frame_count += 1

    # Run both detections
    results_objects = object_model(frame, conf=0.35, verbose=False)
    results_track = track_model(frame, conf=0.1, verbose=False)


    # Extract boxes
    object_boxes = results_objects[0].boxes.xyxy.cpu().numpy() if results_objects[0].boxes else []
    track_boxes = results_track[0].boxes.xyxy.cpu().numpy() if results_track[0].boxes else []

    overlap_found = False

    # -------------------------------
    # Filter only 'rail-track' detections
    # -------------------------------
    if len(track_boxes) > 0:
        track_classes = results_track[0].boxes.cls.cpu().numpy() if results_track[0].boxes else []
        track_names = results_track[0].names  # {id: name}

        print(len(track_boxes), f"Track(s) detected in this frame: {track_names}")

        rail_track_boxes = []
        for idx, track_box in enumerate(track_boxes):
            track_label_id = int(track_classes[idx]) if idx < len(track_classes) else -1
            track_label_name = track_names.get(track_label_id, "Unknown")

            if track_label_name == "rail-track" or track_label_name == "trains":
                rail_track_boxes.append(track_box)

        # ✅ Proceed only if at least one 'rail-track' detected
        if len(rail_track_boxes) > 0:
            for obj_box in object_boxes:
                for track_box in rail_track_boxes:
                    iou = compute_iou(obj_box, track_box)
                    if iou > 0.1:  # overlap threshold
                        overlap_found = True
                        overlapped_obj = obj_box
                        print("⚠ Overlap Detected with 'rail-track'")
                        break
                if overlap_found:
                    break
        else:
            overlap_found = False  # no rail-track detected
    else:
        overlap_found = False

    # -------------------------------
    # Draw detections on frame
    # -------------------------------
    combined_frame = frame.copy()

    # Draw only rail-track boxes
    if len(track_boxes) > 0:
        for idx, track_box in enumerate(track_boxes):
            track_label_id = int(results_track[0].boxes.cls.cpu().numpy()[idx])
            track_label_name = results_track[0].names.get(track_label_id, "Unknown")

            if track_label_name == "rail-track":
                x1, y1, x2, y2 = [int(x) for x in track_box[:4]]
                cv2.rectangle(combined_frame, (x1, y1), (x2, y2), (0, 255, 255), 3)
                cv2.putText(combined_frame, "rail-track", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    # Draw object boxes
    for obj_box in object_boxes:
        x1, y1, x2, y2 = [int(x) for x in obj_box[:4]]
        cv2.rectangle(combined_frame, (x1, y1), (x2, y2), (255, 255, 0), 2)
        cv2.putText(combined_frame, "Object Detected", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

    # -------------------------------
    # Handle overlap / alert condition
    # -------------------------------
    if overlap_found:
        cv2.putText(combined_frame, "⚠ OBJECT ON RAIL TRACK", (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)

        # Save full frame to media folder
        mpath = r"C:\Users\hariedappal\PycharmProjects\railwayobjectdetection\media\obj_detect\\"
        # mpath = r"C:\Users\amaya\Desktop\firstproject-mdit\firstproject\media\obj_detect\\"
        os.makedirs(mpath, exist_ok=True)
        fd = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
        full_img_path = os.path.join(mpath, fd)
        cv2.imwrite(full_img_path, combined_frame)

        # ✅ Crop and save only the overlapped object (optional)
        x1, y1, x2, y2 = [int(x) for x in overlapped_obj[:4]]
        cropped_obj = frame[y1:y2, x1:x2]
        crop_path = os.path.join(mpath, "crop_" + fd)
        cv2.imwrite(crop_path, cropped_obj)

        # Relative path for Django
        p_ph = "/media/obj_detect/" + fd

        # Timestamp
        timestamp = datetime.now()
        date_str = timestamp.strftime("%Y-%m-%d")
        time_str = timestamp.strftime("%H:%M:%S")

        # Insert DB record
        place = "kozhikode"
        q = ("INSERT INTO myapp_objectdetection(`log`, `place`, `time`, `date`) "
             f"VALUES ('{p_ph}','{place}','{time_str}','{date_str}')")
        db.insert(q)

        print(f"🧾 Object on rail-track! Frame {frame_count} saved: {p_ph}")
    else:
        # cv2.putText(combined_frame, "No Object on Rail Track", (30, 50),
        #             cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
        print(f"✅ Frame {frame_count}: No overlap (Objects={len(object_boxes)}, Tracks={len(track_boxes)})")

    # -------------------------------
    # Display + save output video
    # -------------------------------
    cv2.imshow("Railway Detection (Video)", combined_frame)
    out.write(combined_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# -------------------------------
# Cleanup
# -------------------------------
cap.release()
out.release()
cv2.destroyAllWindows()
print(f"\n✅ Video processing complete. Output saved at: {output_path}")
