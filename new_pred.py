# # from ultralytics import YOLO
# # import cv2
# #
# # # -------------------------------
# # # Model paths
# # # -------------------------------
# # foreign_object_model_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\runs\train\railway_foreign_object_detection\weights\best.pt"
# # track_model_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\track\best.pt"
# #
# # # -------------------------------
# # # Image path
# # # -------------------------------
# # image_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\m\railway-1\train\images\C_img_50434_jpg.rf.9f04ba282d8b3ec3021fb8d723764789.jpg"
# # # image_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\m\railway-1\train\images\C_img_37124_jpg.rf.71f261204db1307dc5fa8657a115ca56.jpg"
# #
# # # -------------------------------
# # # Load both YOLO models
# # # -------------------------------
# # object_model = YOLO(foreign_object_model_path)
# # track_model = YOLO(track_model_path)
# #
# # # -------------------------------
# # # Load the image
# # # -------------------------------
# # image = cv2.imread(image_path)
# # if image is None:
# #     print("❌ Error: Could not load the image. Check the file path.")
# #     exit()
# #
# # # -------------------------------
# # # Run detections
# # # -------------------------------
# # results_objects = object_model(image, conf=0.25)
# # results_track = track_model(image, conf=0.1)
# #
# # # -------------------------------
# # # Draw detections on image
# # # -------------------------------
# # # Start from original image copy
# # annotated_image = image.copy()
# #
# # # Draw object detections
# # annotated_imageobject = results_objects[0].plot(img=annotated_image, line_width=2)
# #
# # # Draw track detections on the same image
# # annotated_imagetrack = results_track[0].plot(img=annotated_image, line_width=2)
# #
# #
# # #========================
# #
# #
# #
# #
# #
# #
# # #==============================
# #
# # # -------------------------------
# # # Show and save the combined result
# # # -------------------------------
# # cv2.imshow("Detection Result (Objects + Track)", annotated_imagetrack)
# # cv2.waitKey(5)
# #
# #
# # cv2.imshow("Detection Result (Objects + Track)", annotated_imageobject)
# # cv2.waitKey(5)
# # cv2.destroyAllWindows()
# #
# # # Save the output
# # output_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\output_combined_resulttrack.jpg"
# # cv2.imwrite(output_path, annotated_imagetrack)
# #
# #
# # output_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\output_combined_resultobj.jpg"
# # cv2.imwrite(output_path, annotated_imageobject)
# # print(f"✅ Detection complete. Combined result saved at: {output_path}")
#
# # from ultralytics import YOLO
# # import cv2
# # import numpy as np
# # import os
# #
# # # -------------------------------
# # # Model paths
# # # -------------------------------
# # foreign_object_model_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\runs\train\railway_foreign_object_detection\weights\best.pt"
# # track_model_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\track\best.pt"
# #
# # # -------------------------------
# # # Image path
# # # -------------------------------
# # image_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\m\railway-1\train\images\C_img_1198_jpg.rf.366ee0da9b0668ab6faf94e19d095237.jpg"
# # # image_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\m\railway-1\train\images\C_img_81875_jpg.rf.0e484f83b9a054892970bbfbcb3e91ce.jpg"
# # # image_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\m\railway-1\train\images\C_img_73624_jpg.rf.5df0bcf8ab5f769f7e26a8472e410c19.jpg"
# # # image_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\m\railway-1\train\images\C_img_50434_jpg.rf.9f04ba282d8b3ec3021fb8d723764789.jpg"
# # # image_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\m\railway-1\train\images\C_img_37124_jpg.rf.71f261204db1307dc5fa8657a115ca56.jpg"
# #
# # # -------------------------------
# # # Load both YOLO models
# # # -------------------------------
# # object_model = YOLO(foreign_object_model_path)
# # track_model = YOLO(track_model_path)
# #
# # # -------------------------------
# # # Load the image
# # # -------------------------------
# # image = cv2.imread(image_path)
# # if image is None:
# #     print("❌ Error: Could not load the image. Check the file path.")
# #     exit()
# #
# # # -------------------------------
# # # Run detections
# # # -------------------------------
# # results_objects = object_model(image, conf=0.25)
# # results_track = track_model(image, conf=0.1)
# #
# # # -------------------------------
# # # Draw detections separately
# # # -------------------------------
# # annotated_imageobject = results_objects[0].plot(img=image.copy(), line_width=2)
# # annotated_imagetrack = results_track[0].plot(img=image.copy(), line_width=2)
# #
# # # -------------------------------
# # # Extract bounding boxes
# # # -------------------------------
# # object_boxes = results_objects[0].boxes.xyxy.cpu().numpy() if len(results_objects) else []
# # track_boxes = results_track[0].boxes.xyxy.cpu().numpy() if len(results_track) else []
# #
# # # -------------------------------
# # # Function to calculate IoU
# # # -------------------------------
# # def compute_iou(box1, box2):
# #     xA = max(box1[0], box2[0])
# #     yA = max(box1[1], box2[1])
# #     xB = min(box1[2], box2[2])
# #     yB = min(box1[3], box2[3])
# #     interArea = max(0, xB - xA) * max(0, yB - yA)
# #     box1Area = (box1[2] - box1[0]) * (box1[3] - box1[1])
# #     box2Area = (box2[2] - box2[0]) * (box2[3] - box2[1])
# #     iou = interArea / float(box1Area + box2Area - interArea + 1e-6)
# #     return iou
# #
# # # -------------------------------
# # # Check if overlap exists
# # # -------------------------------
# # overlap_found = False
# # for obj_box in object_boxes:
# #     for track_box in track_boxes:
# #         iou = compute_iou(obj_box, track_box)
# #         if iou > 0.1:  # Adjust threshold if needed
# #             overlap_found = True
# #             break
# #     if overlap_found:
# #         break
# #
# # # -------------------------------
# # # Show and save only if overlap exists
# # # -------------------------------
# # if overlap_found:
# #     print("⚠️ Overlap detected between object and track — displaying results...")
# #
# #     # Show results
# #     cv2.imshow("Track Detection", annotated_imagetrack)
# #     cv2.waitKey(500)
# #     cv2.imshow("Object Detection", annotated_imageobject)
# #     cv2.waitKey(0)
# #     cv2.destroyAllWindows()
# #
# #     # Save results
# #     track_output = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\output_combined_resulttrack.jpg"
# #     obj_output = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\output_combined_resultobj.jpg"
# #
# #     cv2.imwrite(track_output, annotated_imagetrack)
# #     cv2.imwrite(obj_output, annotated_imageobject)
# #
# #     print(f"✅ Results saved:\n- Track: {track_output}\n- Object: {obj_output}")
# # else:
# #     print("✅ No overlap detected — skipping output generation.")
#
#
# # from ultralytics import YOLO
# # import cv2
# # import numpy as np
# # import os
# #
# # # -------------------------------
# # # Model paths
# # # -------------------------------
# # foreign_object_model_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\runs\train\railway_foreign_object_detection\weights\best.pt"
# # track_model_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\track\best.pt"
# #
# # # -------------------------------
# # # Image path
# # # -------------------------------
# # image_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\m\railway-1\train\images\C_img_1198_jpg.rf.366ee0da9b0668ab6faf94e19d095237.jpg"
# # # image_path = r"C:\Users\amaya\Desktop\Railway-o bstacle-detection-main\mdit_foreignobjects\m\railway-1\train\images\C_img_81875_jpg.rf.0e484f83b9a054892970bbfbcb3e91ce.jpg"
# # # image_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\m\railway-1\train\images\C_img_73624_jpg.rf.5df0bcf8ab5f769f7e26a8472e410c19.jpg"
# # # image_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\m\railway-1\train\images\C_img_50434_jpg.rf.9f04ba282d8b3ec3021fb8d723764789.jpg"
# # # image_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\m\railway-1\train\images\C_img_37124_jpg.rf.71f261204db1307dc5fa8657a115ca56.jpg"
# #
# # # -------------------------------
# # # Load both YOLO models
# # # -------------------------------
# # object_model = YOLO(foreign_object_model_path)
# # track_model = YOLO(track_model_path)
# #
# # # -------------------------------
# # # Load the image
# # # -------------------------------
# # image = cv2.imread(image_path)
# # if image is None:
# #     print("❌ Error: Could not load the image. Check the file path.")
# #     exit()
# #
# # # -------------------------------
# # # Run detections
# # # -------------------------------
# # results_objects = object_model(image, conf=0.25)
# # results_track = track_model(image, conf=0.1)
# #
# # # -------------------------------
# # # Extract bounding boxes
# # # -------------------------------
# # object_boxes = results_objects[0].boxes.xyxy.cpu().numpy() if len(results_objects) else []
# # track_boxes = results_track[0].boxes.xyxy.cpu().numpy() if len(results_track) else []
# #
# # # -------------------------------
# # # Function to calculate IoU
# # # -------------------------------
# # def compute_iou(box1, box2):
# #     xA = max(box1[0], box2[0])
# #     yA = max(box1[1], box2[1])
# #     xB = min(box1[2], box2[2])
# #     yB = min(box1[3], box2[3])
# #     interArea = max(0, xB - xA) * max(0, yB - yA)
# #     box1Area = (box1[2] - box1[0]) * (box1[3] - box1[1])
# #     box2Area = (box2[2] - box2[0]) * (box2[3] - box2[1])
# #     iou = interArea / float(box1Area + box2Area - interArea + 1e-6)
# #     return iou
# #
# # # -------------------------------
# # # Check for overlap
# # # -------------------------------
# # overlap_found = False
# # for obj_box in object_boxes:
# #     for track_box in track_boxes:
# #         iou = compute_iou(obj_box, track_box)
# #         if iou > 0.1:  # threshold
# #             overlap_found = True
# #             break
# #     if overlap_found:
# #         break
# #
# # # -------------------------------
# # # Combine both detections on ONE image
# # # -------------------------------
# # combined_image = image.copy()
# # combined_image = results_track[0].plot(img=combined_image, line_width=2)
# # combined_image = results_objects[0].plot(img=combined_image, line_width=2)
# #
# # # -------------------------------
# # # Show and save only if overlap exists
# # # -------------------------------
# # if overlap_found:
# #     print("⚠️ Overlap detected between object and track — displaying combined result...")
# #
# #     cv2.imshow("Combined Detection (Track + Object)", combined_image)
# #     cv2.waitKey(0)
# #     cv2.destroyAllWindows()
# #
# #     output_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\output_combined_result.jpg"
# #     cv2.imwrite(output_path, combined_image)
# #
# #     print(f"✅ Combined result saved at: {output_path}")
# # else:
# #     cv2.imshow("Combined Detection (Track + Object)", combined_image)
# #     cv2.waitKey(0)
# #     cv2.destroyAllWindows()
# #
# #     output_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\output_combined_result.jpg"
# #     cv2.imwrite(output_path, combined_image)
# #     print("✅ No overlap detected — skipping output generation.")
#
# from ultralytics import YOLO
# import cv2
# import numpy as np
# import os
# import math
#
# # -------------------------------
# # Model paths
# # -------------------------------
# foreign_object_model_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\runs\train\railway_foreign_object_detection\weights\best.pt"
# track_model_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\track\best.pt"
#
# # -------------------------------
# # Image path
# # -------------------------------
# # image_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\m\railway-1\train\images\_108970654_gettyimages-497844768-235-_jpg.rf.19aa84264a09905d14b31cdb84d3e9d1.jpg"
# # image_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\m\railway-1\train\images\_108970654_gettyimages-497844768-177-_jpg.rf.0beeb543a12d817d5f210e347a70ab4c.jpg"
# image_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\m\railway-1\train\images\_108970654_gettyimages-497844768-242-_jpg.rf.cbf2f3a13999a330dcc31db8b3088d89.jpg"
# # image_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\m\railway-1\train\images\_108970654_gettyimages-497844768-99-_jpg.rf.bc3343c53ee9bfa1f3746a0470b31bb5.jpg"
# # image_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\m\railway-1\train\images\_108970654_gettyimages-497844768-14-_jpg.rf.d635b3f0471a417486880621a08967db.jpg"
# # image_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\m\railway-1\train\images\34_frame174_jpg.rf.f4e84b4e50bad7338ad24ee64068c004.jpg"
# # image_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\m\railway-1\train\images\28_frame203_jpg.rf.b434fd31d6ba41ed7da49fa20b85a10e.jpg"
# # image_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\m\railway-1\train\images\26_frame29_jpg.rf.0a5c29a2b54967ab203a5e42f5530e23.jpg"
# # image_path = r"C:\Users\amaya\Downloads\ChatGPT Image Oct 27, 2025, 09_43_57 AM.png"
# # image_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\m\railway-1\train\images\C_img_1198_jpg.rf.366ee0da9b0668ab6faf94e19d095237.jpg"
#
# # -------------------------------
# # Load both YOLO models
# # -------------------------------
# object_model = YOLO(foreign_object_model_path)
# track_model = YOLO(track_model_path)
#
# # -------------------------------
# # Load the image
# # -------------------------------
# image = cv2.imread(image_path)
# if image is None:
#     print("❌ Error: Could not load the image. Check the file path.")
#     exit()
#
# # -------------------------------
# # Run detections
# # -------------------------------
# results_objects = object_model(image, conf=0.25)
# results_track = track_model(image, conf=0.1)
#
# # -------------------------------
# # Extract bounding boxes
# # -------------------------------
# object_boxes = results_objects[0].boxes.xyxy.cpu().numpy() if len(results_objects) else []
# track_boxes = results_track[0].boxes.xyxy.cpu().numpy() if len(results_track) else []
#
# # -------------------------------
# # Helper functions
# # -------------------------------
# def compute_iou(box1, box2):
#     xA = max(box1[0], box2[0])
#     yA = max(box1[1], box2[1])
#     xB = min(box1[2], box2[2])
#     yB = min(box1[3], box2[3])
#     interArea = max(0, xB - xA) * max(0, yB - yA)
#     box1Area = (box1[2] - box1[0]) * (box1[3] - box1[1])
#     box2Area = (box2[2] - box2[0]) * (box2[3] - box2[1])
#     iou = interArea / float(box1Area + box2Area - interArea + 1e-6)
#     return iou
#
# def compute_center_distance(box1, box2):
#     c1x = (box1[0] + box1[2]) / 2
#     c1y = (box1[1] + box1[3]) / 2
#     c2x = (box2[0] + box2[2]) / 2
#     c2y = (box2[1] + box2[3]) / 2
#     return math.sqrt((c1x - c2x)**2 + (c1y - c2y)**2)
#
# # -------------------------------
# # Check for overlap OR proximity
# # -------------------------------
# overlap_found = False
# distance_threshold = 500  # pixels — adjust as needed
#
# for obj_box in object_boxes:
#     for track_box in track_boxes:
#         iou = compute_iou(obj_box, track_box)
#         distance = compute_center_distance(obj_box, track_box)
#
#         if iou > 0.2 or distance < distance_threshold:
#             overlap_found = True
#             break
#     if overlap_found:
#         break
#
# # -------------------------------
# # Combine both detections on ONE image
# # -------------------------------
# combined_image = image.copy()
# combined_image = results_track[0].plot(img=combined_image, line_width=2)
# combined_image = results_objects[0].plot(img=combined_image, line_width=2)
#
# # -------------------------------
# # Show and save result
# # -------------------------------
# output_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\output_combined_result.jpg"
#
# if overlap_found:
#     print("⚠️ Object and track are overlapping or very close — displaying combined result...")
# else:
#     print("ℹ️ No direct overlap, but combined detection shown anyway.")
#
# cv2.imshow("Combined Detection (Track + Object)", combined_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# cv2.imwrite(output_path, combined_image)
# print(f"✅ Combined result saved at: {output_path}")


# from ultralytics import YOLO
# import cv2
# import numpy as np
# import os
# import math
#
# from DBConnection import Database
#
#
# db=Database()
# # -------------------------------
# # Model paths
# # -------------------------------
# foreign_object_model_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\runs\train\railway_foreign_object_detection\weights\best.pt"
# track_model_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\track\best.pt"
#
# # -------------------------------
# # Video path
# # -------------------------------
# video_path = r"C:\Users\amaya\Downloads\লাইন পরিবর্তন করে লুপ লাইনে ট্রেন নিয.mp4"
# # video_path = r"C:\Users\amaya\Downloads\People Almost Run Over by Train! 😱 #trainvideos #trainaccident #trains #shorts (1).mp4"
# # video_path = r"C:\Users\amaya\Downloads\￼￼￼￼ Crossing Track 😱 Train Accident point ￼￼#shorts #train #accidentnews.mp4"
# # video_path = r"C:\Users\amaya\Downloads\Oh My God! Four Trains On One Railway Track #Viral #Odisha #Trending #Short.mp4"
# # video_path = r"C:\Users\amaya\Downloads\Tree fallen on railway track #beach #viralreels #railway #foryou #railtrack #storm #forest #viral.mp4"
# # video_path = r"C:\Users\amaya\Downloads\Track obstacle detection.mp4"
# # video_path = r"C:\Users\amaya\Downloads\Obstruction test for Railway track Safety 🏭  @RailwayTechShorts  #railwayinfrastructure #1milli.mp4"
# # video_path = r"C:\Users\amaya\Downloads\Elephant Saved After A Train Driver Noticed It Crossing Track _ Latest _ #Shorts _ CNN News18.mp4"
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
# # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 700)
# # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 520)
# # Get video info
# fps = int(cap.get(cv2.CAP_PROP_FPS))
# width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# # width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
#
# # -------------------------------
# # Helper functions
# # -------------------------------
# def compute_iou(box1, box2):
#     xA = max(box1[0], box2[0])
#     yA = max(box1[1], box2[1])
#     xB = min(box1[2], box2[2])
#     yB = min(box1[3], box2[3])
#     interArea = max(0, xB - xA) * max(0, yB - yA)
#     box1Area = (box1[2] - box1[0]) * (box1[3] - box1[1])
#     box2Area = (box2[2] - box2[0]) * (box2[3] - box2[1])
#     return interArea / float(box1Area + box2Area - interArea + 1e-6)
#
# def compute_center_distance(box1, box2):
#     c1x = (box1[0] + box1[2]) / 2
#     c1y = (box1[1] + box1[3]) / 2
#     c2x = (box2[0] + box2[2]) / 2
#     c2y = (box2[1] + box2[3]) / 2
#     return math.sqrt((c1x - c2x)**2 + (c1y - c2y)**2)
#
# # -------------------------------
# # Process video frame by frame
# # -------------------------------
# distance_threshold = 500  # pixels
# frame_count = 0
#
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#     frame_count += 1
#
#     # Run detections
#     results_objects = object_model(frame, conf=0.25, verbose=False)
#     results_track = track_model(frame, conf=0.1, verbose=False)
#
#     # Extract bounding boxes
#     object_boxes = results_objects[0].boxes.xyxy.cpu().numpy() if len(results_objects) else []
#     track_boxes = results_track[0].boxes.xyxy.cpu().numpy() if len(results_track) else []
#
#     overlap_found = False
#     for obj_box in object_boxes:
#         for track_box in track_boxes:
#             iou = compute_iou(obj_box, track_box)
#             distance = compute_center_distance(obj_box, track_box)
#             if iou > 0.2 or distance < distance_threshold:
#                 overlap_found = True
#                 break
#         if overlap_found:
#             break
#
#     # Draw both detections
#     combined_frame = frame.copy()
#     combined_frame = results_track[0].plot(img=combined_frame, line_width=2)
#     combined_frame = results_objects[0].plot(img=combined_frame, line_width=2)
#
#     # Add status text
#     if overlap_found:
#         cv2.putText(combined_frame, "⚠️ OBJECT CLOSE TO TRACK", (30, 50),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)
#     else:
#         cv2.putText(combined_frame, "No Close Object", (30, 50),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
#
#     # Show and write frame
#     cv2.imshow("Railway Detection (Video)", combined_frame)
#     out.write(combined_frame)
#
#     # Stop with 'q'
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
#     print(f"Processed frame {frame_count}", end='\r')
#
# # -------------------------------
# # Cleanup
# # -------------------------------
# cap.release()
# out.release()
# cv2.destroyAllWindows()
# print(f"\n✅ Video processing complete. Output saved at: {output_path}")


# from ultralytics import YOLO
# import cv2
# import numpy as np
# import os
# import math
# import datetime
#
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
# video_path = r"C:\Users\amaya\Downloads\লাইন পরিবর্তন করে লুপ লাইনে ট্রেন নিয.mp4"
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
# # Helper functions
# # -------------------------------
# def compute_iou(box1, box2):
#     xA = max(box1[0], box2[0])
#     yA = max(box1[1], box2[1])
#     xB = min(box1[2], box2[2])
#     yB = min(box1[3], box2[3])
#     interArea = max(0, xB - xA) * max(0, yB - yA)
#     box1Area = (box1[2] - box1[0]) * (box1[3] - box1[1])
#     box2Area = (box2[2] - box2[0]) * (box2[3] - box2[1])
#     return interArea / float(box1Area + box2Area - interArea + 1e-6)
#
# def compute_center_distance(box1, box2):
#     c1x = (box1[0] + box1[2]) / 2
#     c1y = (box1[1] + box1[3]) / 2
#     c2x = (box2[0] + box2[2]) / 2
#     c2y = (box2[1] + box2[3]) / 2
#     return math.sqrt((c1x - c2x)**2 + (c1y - c2y)**2)
#
# # -------------------------------
# # Process video frame by frame
# # -------------------------------
# distance_threshold = 10  # pixels
# frame_count = 0
#
# # Directory to save detected obstacle frames
# save_dir = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\detected_frames"
# os.makedirs(save_dir, exist_ok=True)
#
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#     frame_count += 1
#
#     # Run detections
#     results_objects = object_model(frame, conf=0.25, verbose=False)
#     results_track = track_model(frame, conf=0.1, verbose=False)
#
#     # Extract bounding boxes
#     object_boxes = results_objects[0].boxes.xyxy.cpu().numpy() if len(results_objects) else []
#     track_boxes = results_track[0].boxes.xyxy.cpu().numpy() if len(results_track) else []
#
#     overlap_found = False
#     for obj_box in object_boxes:
#         for track_box in track_boxes:
#             iou = compute_iou(obj_box, track_box)
#             distance = compute_center_distance(obj_box, track_box)
#             if iou > 0.2 or distance < distance_threshold:
#                 overlap_found = True
#                 break
#         if overlap_found:
#             break
#
#     # Draw both detections
#     combined_frame = frame.copy()
#     combined_frame = results_track[0].plot(img=combined_frame, line_width=2)
#     combined_frame = results_objects[0].plot(img=combined_frame, line_width=2)
#
#     # Add status text and DB insertion
#     if overlap_found:
#         cv2.putText(combined_frame, "⚠️ OBJECT CLOSE TO TRACK", (30, 50),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)
#
#         # Save current frame image
#         # Save current frame image
#         from datetime import datetime
#
#         mpath = r"C:\Users\amaya\Desktop\firstproject-mdit\firstproject\media\obj_detect\\"
#         os.makedirs(mpath, exist_ok=True)
#
#         fd = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
#         full_img_path = os.path.join(mpath, fd)
#
#         # Save the frame (combined_frame)
#         cv2.imwrite(full_img_path, combined_frame)
#
#         # Relative path for Django (to store in DB)
#         p_ph = "/media/obj_detect/" + fd
#
#
#
#
#
#         #=============================
#         timestamp = datetime.now()
#         date_str = timestamp.strftime("%Y-%m-%d")
#         time_str = timestamp.strftime("%H:%M:%S")
#         # img_filename = f"detected_{frame_count}_{timestamp.strftime('%Y%m%d_%H%M%S')}.jpg"
#         # img_path = os.path.join(save_dir, img_filename)
#         # cv2.imwrite(img_path, combined_frame)
#
#         # Insert record into DB
#         place = "kozhikode"  # replace with GPS/location if available
#         q = "INSERT INTO myapp_objectdetection(`log`, `place`, `time`, `date`) VALUES ('"+p_ph+"','"+place+"','"+time_str+"','"+date_str+"')"
#         # values = (img_path, place, time_str, date_str)
#         db.insert(q)
#         print(f"🧾 Inserted detection record for frame {frame_count}")
#
#     else:
#         cv2.putText(combined_frame, "No Close Object", (30, 50),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
#
#     # Show and write frame
#     cv2.imshow("Railway Detection (Video)", combined_frame)
#     out.write(combined_frame)
#
#     # Stop with 'q'
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
#     print(f"Processed frame {frame_count}", end='\r')
#
# # -------------------------------
# # Cleanup
# # -------------------------------
# cap.release()
# out.release()
# cv2.destroyAllWindows()
# print(f"\n✅ Video processing complete. Output saved at: {output_path}")
#

# from ultralytics import YOLO
# import cv2
# import numpy as np
# import os
# import math
# import datetime
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
# video_path = r"C:\Users\amaya\Downloads\লাইন পরিবর্তন করে লুপ লাইনে ট্রেন নিয.mp4"
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
# # Helper functions
# # -------------------------------
# def compute_iou(box1, box2):
#     xA = max(box1[0], box2[0])
#     yA = max(box1[1], box2[1])
#     xB = min(box1[2], box2[2])
#     yB = min(box1[3], box2[3])
#     interArea = max(0, xB - xA) * max(0, yB - yA)
#     box1Area = (box1[2] - box1[0]) * (box1[3] - box1[1])
#     box2Area = (box2[2] - box2[0]) * (box2[3] - box2[1])
#     return interArea / float(box1Area + box2Area - interArea + 1e-6)
#
# # -------------------------------
# # Process video frame by frame
# # -------------------------------
# frame_count = 0
#
# # Directory to save detected obstacle frames
# save_dir = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\detected_frames"
# os.makedirs(save_dir, exist_ok=True)
#
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#     frame_count += 1
#
#     # Run detections
#     results_objects = object_model(frame, conf=0.25, verbose=False)
#     results_track = track_model(frame, conf=0.1, verbose=False)
#
#     # Extract bounding boxes
#     object_boxes = results_objects[0].boxes.xyxy.cpu().numpy() if len(results_objects) else []
#     track_boxes = results_track[0].boxes.xyxy.cpu().numpy() if len(results_track) else []
#
#     overlap_found = False
#     for obj_box in object_boxes:
#         for track_box in track_boxes:
#             iou = compute_iou(obj_box, track_box)
#             # ✅ Only trigger when object is *inside* the track region
#             if iou > 0.2:
#                 overlap_found = True
#                 break
#         if overlap_found:
#             break
#
#     # Draw both detections
#     combined_frame = frame.copy()
#     combined_frame = results_track[0].plot(img=combined_frame, line_width=2)
#     combined_frame = results_objects[0].plot(img=combined_frame, line_width=2)
#
#     # Add status text and DB insertion
#     if overlap_found:
#         cv2.putText(combined_frame, "⚠ OBJECT ON TRACK", (30, 50),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)
#
#         # Save current frame image to Django media folder
#         from datetime import datetime
#
#         mpath = r"C:\Users\amaya\Desktop\firstproject-mdit\firstproject\media\obj_detect\\"
#         os.makedirs(mpath, exist_ok=True)
#
#         fd = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
#         full_img_path = os.path.join(mpath, fd)
#         cv2.imwrite(full_img_path, combined_frame)
#
#         # Relative path for Django (to store in DB)
#         p_ph = "/media/obj_detect/" + fd
#
#         # Timestamp for DB
#         timestamp = datetime.now()
#         date_str = timestamp.strftime("%Y-%m-%d")
#         time_str = timestamp.strftime("%H:%M:%S")
#
#         # Insert record into DB
#         place = "kozhikode"  # replace with GPS/location if available
#         q = "INSERT INTO myapp_objectdetection(`log`, `place`, `time`, `date`) VALUES ('" + p_ph + "','" + place + "','" + time_str + "','" + date_str + "')"
#         db.insert(q)
#         print(f"🧾 Inserted detection record for frame {frame_count}: {p_ph}")
#
#     else:
#         cv2.putText(combined_frame, "No Object on Track", (30, 50),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
#
#     # Show and write frame
#     cv2.imshow("Railway Detection (Video)", combined_frame)
#     out.write(combined_frame)
#
#     # Stop with 'q'
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
#     print(f"Processed frame {frame_count}", end='\r')
#
# # -------------------------------
# # Cleanup
# # -------------------------------
# cap.release()
# out.release()
# cv2.destroyAllWindows()
# print(f"\n✅ Video processing complete. Output saved at: {output_path}")


# from ultralytics import YOLO
# import cv2
# import numpy as np
# import os
# import math
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
# video_path = r"C:\Users\amaya\Downloads\লাইন পরিবর্তন করে লুপ লাইনে ট্রেন নিয.mp4"
# # video_path = r"C:\Users\amaya\Downloads\Elephant Saved After A Train Driver Noticed It Crossing Track _ Latest _ #Shorts _ CNN News18.mp4"
#
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
#     xA = max(box1[0], box2[0])
#     yA = max(box1[1], box2[1])
#     xB = min(box1[2], box2[2])
#     yB = min(box1[3], box2[3])
#     interArea = max(0, xB - xA) * max(0, yB - yA)
#     box1Area = (box1[2] - box1[0]) * (box1[3] - box1[1])
#     box2Area = (box2[2] - box2[0]) * (box2[3] - box2[1])
#     return interArea / float(box1Area + box2Area - interArea + 1e-6)
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
#     results_track = track_model(frame, conf=0.25, verbose=False)
#
#     # Extract boxes
#     object_boxes = results_objects[0].boxes.xyxy.cpu().numpy() if len(results_objects) else []
#     track_boxes = results_track[0].boxes.xyxy.cpu().numpy() if len(results_track) else []
#
#     overlap_found = False
#     for obj_box in object_boxes:
#         for track_box in track_boxes:
#             iou = compute_iou(obj_box, track_box)
#             # ✅ Only save if object is inside the track (IoU threshold)
#             if iou > 0.3:
#                 overlap_found = True
#                 break
#         if overlap_found:
#             break
#
#     # Draw detections on frame
#     combined_frame = frame.copy()
#     combined_frame = results_track[0].plot(img=combined_frame, line_width=2)
#     combined_frame = results_objects[0].plot(img=combined_frame, line_width=2)
#
#     if overlap_found:
#         cv2.putText(combined_frame, "⚠ OBJECT ON TRACK", (30, 50),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)
#
#         # Save frame to Django media folder only if object on track
#         mpath = r"C:\Users\amaya\Desktop\firstproject-mdit\firstproject\media\obj_detect\\"
#         os.makedirs(mpath, exist_ok=True)
#         fd = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
#         full_img_path = os.path.join(mpath, fd)
#         cv2.imwrite(full_img_path, combined_frame)
#
#         # Relative path for Django (DB storage)
#         p_ph = "/media/obj_detect/" + fd
#
#         # Timestamp
#         timestamp = datetime.now()
#         date_str = timestamp.strftime("%Y-%m-%d")
#         time_str = timestamp.strftime("%H:%M:%S")
#
#         # Insert only when object is on track
#         place = "kozhikode"
#         q = ("INSERT INTO myapp_objectdetection(`log`, `place`, `time`, `date`) "
#              "VALUES ('" + p_ph + "','" + place + "','" + time_str + "','" + date_str + "')")
#         db.insert(q)
#         print(f"🧾 Inserted detection record for frame {frame_count}: {p_ph}")
#
#     else:
#         cv2.putText(combined_frame, "No Object on Track", (30, 50),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
#
#     # Display + save output video
#     cv2.imshow("Railway Detection (Video)", combined_frame)
#     out.write(combined_frame)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
#     print(f"Processed frame {frame_count}", end='\r')
#
# # -------------------------------
# # Cleanup
# # -------------------------------
# cap.release()
# out.release()
# cv2.destroyAllWindows()
# print(f"\n✅ Video processing complete. Output saved at: {output_path}")


# from ultralytics import YOLO
# import cv2
# import numpy as np
# import os
# import math
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
# video_path = r"C:\Users\amaya\Downloads\Ip Man 4： The Finale ｜ Final Fight Scene.mp4"
# # video_path = r"C:\Users\amaya\Downloads\Elephant Saved After A Train Driver Noticed It Crossing Track _ Latest _ #Shorts _ CNN News18.mp4"
# # video_path = r"C:\Users\amaya\Downloads\Must be the god with this guy #train #car #nearly.mp4"
# # video_path = r"C:\Users\amaya\Downloads\electric train horn sound Amazing #foryou #babifreitas #explore.mp4"
# # video_path = r"C:\Users\amaya\Downloads\লাইন পরিবর্তন করে লুপ লাইনে ট্রেন নিয.mp4"
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
#     xA = max(box1[0], box2[0])
#     yA = max(box1[1], box2[1])
#     xB = min(box1[2], box2[2])
#     yB = min(box1[3], box2[3])
#     interArea = max(0, xB - xA) * max(0, yB - yA)
#     box1Area = (box1[2] - box1[0]) * (box1[3] - box1[1])
#     box2Area = (box2[2] - box2[0]) * (box2[3] - box2[1])
#     return interArea / float(box1Area + box2Area - interArea + 1e-6)
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
#     results_track = track_model(frame, conf=0.25, verbose=False)
#
#     # Extract boxes
#     object_boxes = results_objects[0].boxes.xyxy.cpu().numpy() if len(results_objects) else []
#     track_boxes = results_track[0].boxes.xyxy.cpu().numpy() if len(results_track) else []
#
#     overlap_found = False
#     for obj_box in object_boxes:
#         for track_box in track_boxes:
#             iou = compute_iou(obj_box, track_box)
#             # ✅ Only save if object is inside the track (IoU threshold)
#             if iou > 0.1:
#                 overlap_found = True
#                 break
#         if overlap_found:
#             break
#
#     # Draw detections on frame
#     combined_frame = frame.copy()
#     combined_frame = results_track[0].plot(img=combined_frame, line_width=2)
#     combined_frame = results_objects[0].plot(img=combined_frame, line_width=2)
#
#     # ✅ Show “Object Detected” above each object box
#     for obj_box in object_boxes:
#         x1, y1, x2, y2 = [int(x) for x in obj_box[:4]]
#         label = "Object Detected"
#         cv2.putText(combined_frame, label, (x1, y1 - 10),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
#
#     if overlap_found:
#         cv2.putText(combined_frame, "⚠ OBJECT ON TRACK", (30, 50),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)
#
#         # Save frame to Django media folder only if object on track
#         mpath = r"C:\Users\amaya\Desktop\firstproject-mdit\firstproject\media\obj_detect\\"
#         os.makedirs(mpath, exist_ok=True)
#         fd = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
#         full_img_path = os.path.join(mpath, fd)
#         cv2.imwrite(full_img_path, combined_frame)
#
#         # Relative path for Django (DB storage)
#         p_ph = "/media/obj_detect/" + fd
#
#         # Timestamp
#         timestamp = datetime.now()
#         date_str = timestamp.strftime("%Y-%m-%d")
#         time_str = timestamp.strftime("%H:%M:%S")
#
#         # Insert only when object is on track
#         place = "kozhikode"
#         q = ("INSERT INTO myapp_objectdetection(`log`, `place`, `time`, `date`) "
#              "VALUES ('" + p_ph + "','" + place + "','" + time_str + "','" + date_str + "')")
#         db.insert(q)
#         print(f"🧾 Inserted detection record for frame {frame_count}: {p_ph}")
#
#     else:
#         cv2.putText(combined_frame, "No Object on Track", (30, 50),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
#
#     # Display + save output video
#     cv2.imshow("Railway Detection (Video)", combined_frame)
#     out.write(combined_frame)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
#     print(f"Processed frame {frame_count}", end='\r')
#
# # -------------------------------
# # Cleanup
# # -------------------------------
# cap.release()
# out.release()
# cv2.destroyAllWindows()
# print(f"\n✅ Video processing complete. Output saved at: {output_path}")
#

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
# # track_model_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\track_new\best.pt"
# track_model_path = r"C:\Users\amaya\Desktop\Railway-obstacle-detection-main\mdit_foreignobjects\track\best.pt"
#
# # -------------------------------
# # Video path
# # -------------------------------
# # video_path = r"C:\Users\amaya\Downloads\Elephant Saved After A Train Driver Noticed It Crossing Track _ Latest _ #Shorts _ CNN News18.mp4"
#
# # video_path = r"C:\Users\amaya\Downloads\Elephant Saved After A Train Driver Noticed It Crossing Track _ Latest _ #Shorts _ CNN News18.mp4"
# video_path = r"C:\Users\amaya\Downloads\or worse yet, an ELECTRIC EEL 🙀 🎥： pjordan922 (TT), #shorts.mp4"
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
#     results_track = track_model(frame, conf=0.3, verbose=False)  # higher conf for fewer false tracks
#
#     # Extract boxes
#     object_boxes = results_objects[0].boxes.xyxy.cpu().numpy() if results_objects[0].boxes else []
#     track_boxes = results_track[0].boxes.xyxy.cpu().numpy() if results_track[0].boxes else []
#
#     overlap_found = False
#
#     # ✅ Proceed only if at least one track is detected
#     if len(track_boxes) > 0:
#
#         print(len(track_boxes),"amaya")
#
#
#
#         for obj_box in object_boxes:
#             for track_box in track_boxes:
#
#                 need lables corresponding track box
#                 iou = compute_iou(obj_box, track_box)
#                 if iou > 0.1:  # overlap threshold
#                     overlap_found = True
#                     overlapped_obj = obj_box  # store the object box for cropping
#                     break
#             if overlap_found:
#                 break
#     else:
#         overlap_found = False  # no track at all → skip saving
#
#     # Draw detections on frame
#     combined_frame = frame.copy()
#     combined_frame = results_track[0].plot(img=combined_frame, line_width=2)
#     combined_frame = results_objects[0].plot(img=combined_frame, line_width=2)
#
#     # Add text labels
#     for obj_box in object_boxes:
#         x1, y1, x2, y2 = [int(x) for x in obj_box[:4]]
#         cv2.putText(combined_frame, "Object Detected", (x1, y1 - 10),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
#
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
#     # Display + save output video
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
