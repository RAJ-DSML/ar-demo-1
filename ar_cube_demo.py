import cv2
import numpy as np

# Load camera calibration data from the .npz file
with np.load('calibration_data.npz') as data:
    camera_matrix = data['camera_matrix']
    dist_coeffs = data['dist_coeffs']

# Define ArUco dictionary and detection parameters
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
parameters = cv2.aruco.DetectorParameters()

# Define 3D points for the cube
cube_points = np.float32([
    [0, 0, 0], [0, 0.05, 0], [0.05, 0.05, 0], [0.05, 0, 0],      # Base square
    [0, 0, -0.05], [0, 0.05, -0.05], [0.05, 0.05, -0.05], [0.05, 0, -0.05]  # Top square
])

# Define the 3D points for the axis
axis_length = 0.05
axis_points = np.float32([
    [0, 0, 0], [axis_length, 0, 0], [0, axis_length, 0], [0, 0, -axis_length]
])

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect ArUco markers in the frame
    corners, ids, _ = cv2.aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
    
    if ids is not None and len(ids) > 0:
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)

        # Estimate pose of each marker
        rvec, tvec, _ = cv2.aruco.estimatePoseSingleMarkers(corners, 0.05, camera_matrix, dist_coeffs)

        for i in range(len(ids)):
            # Project axis points
            imgpts, _ = cv2.projectPoints(axis_points, rvec[i], tvec[i], camera_matrix, dist_coeffs)
            origin = tuple(imgpts[0].ravel().astype(int))

            # Draw the X axis in red, Y axis in green, and Z axis in blue
            frame = cv2.line(frame, origin, tuple(imgpts[1].ravel().astype(int)), (0, 0, 255), 3)
            frame = cv2.line(frame, origin, tuple(imgpts[2].ravel().astype(int)), (0, 255, 0), 3)
            frame = cv2.line(frame, origin, tuple(imgpts[3].ravel().astype(int)), (255, 0, 0), 3)

            # Project cube points and draw the cube
            cube_imgpts, _ = cv2.projectPoints(cube_points, rvec[i], tvec[i], camera_matrix, dist_coeffs)
            frame = cv2.drawContours(frame, [cube_imgpts[:4].astype(int)], -1, (255, 0, 0), 3)

            for j in range(4):
                pt1 = tuple(cube_imgpts[j][0].ravel().astype(int))
                pt2 = tuple(cube_imgpts[j+4][0].ravel().astype(int))
                frame = cv2.line(frame, pt1, pt2, (0, 255, 0), 3)


            frame = cv2.drawContours(frame, [cube_imgpts[4:].astype(int)], -1, (0, 0, 255), 3)

    # Display the frame with overlay
    cv2.imshow('ArUco Cube Overlay', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
