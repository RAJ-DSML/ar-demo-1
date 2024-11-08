<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/RAJ-DSML/ar-demo-1/blob/main/SampleVideo/ArUco_VideoFootage.gif">
    <img src="ArUco_VideoFootage.gif" alt="Logo" width="500" height="450">
  </a>

  <h1 align="center">ArUco Marker Detection and Axis/Cube Visualization with Python</h1>
</p>

<!-- ABOUT THE PROJECT -->
## About The Project

This project demonstrates the use of OpenCV and ArUco library to detect ArUco markers in a live camera feed and overlay a virtual cube with its corresponding axis system on top of the detected marker.

### How to run in you local system?

You need to perform following steps.

* clone
  ```sh
  git clone https://github.com/RAJ-DSML/ar-demo-1.git
  ```
* redirect to the project directory
  ```sh
  cd ar-demo-1
  ```
* create a virtual environment
  ```sh
  python -m venv venv
  ```
* activate that venv
  ```sh
  venv\Scripts\activate
  ```
* install the required packages
  ```sh
  pip install -r requirements.txt
  ```
* run the main python file
  ```sh
  python ar_cube_demo.py
  ```

### Project Structure
The project consists of a single Python script (aruco_cube_overlay.py) and potentially a calibration data file (calibration_data.npz). The calibration data file is not included in this example but is typically generated through a separate camera calibration process.

