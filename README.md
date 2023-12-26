# Face Emotion Recognition using DeepFace and Flask

## Overview

This is a simple Flask application for real-time emotion detection using a webcam. The application captures emotions from the webcam, displays live streaming, and allows users to start and stop emotion detection tests. The results, including timestamps and detected emotions, can be downloaded after the test.

## Requirements

- Python 3.x
- Flask
- OpenCV
- DeepFace


## Setup

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/emotion-detection-flask.git
    ```

2. **Navigate to the Project Directory:**

    ```bash
    cd emotion-detection-flask
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask Application:**

    ```bash
    python app.py
    ```

    The application will be running at [http://localhost:5000/](http://localhost:5000/). Open this URL in your web browser.

5. **Usage:**

    - Click on "Start Test" to initiate emotion detection.
    - Click on "Stop Test" to end the test and download the results.

6. **Customization:**

    - Adjust the Flask app configuration in `app.py` if needed.
    - Modify the HTML templates in the `templates` folder for UI changes.
    - Customize the design in the CSS section of the HTML templates.

## Issues and Contributions

If you encounter any issues or would like to contribute to the project, feel free to open an issue or submit a pull request.


