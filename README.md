
# Fire Detection Alarm System

The Fire Detection Alarm System uses a YOLO model trained with a dataset from Roboflow to detect fire in real-time using a webcam. When fire is detected, an alert sound is played, and a popup message shows 'Fire detected'.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Training the Model](#training-the-model)
  - [Running the Fire Detection Alarm](#running-the-fire-detection-alarm)
- [How It Works](#how-it-works)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## Features
- Real-time fire detection using a webcam.
- Alerts user with a sound when fire is detected.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/FireDetectionAlarm.git
   cd FireDetectionAlarm
   ```

2. Install the required dependencies:
   ```sh
   pip install opencv-python-headless ultralytics pygame roboflow
   ```

## Usage

### Training the Model
The model was trained using a dataset from Roboflow. The following file was used to train the model on Kaggle:

**File: `train_model.py`**

### Running the Fire Detection Alarm
This script runs the trained YOLO model to detect fire in real-time and plays an alert sound when fire is detected.

1. Run the script:
   ```sh
   python fire_detection.py
   ```

**File: `fire_detection.py`**

**Note:** The trained model file `best.pt` is included in the repository for testing.

## How It Works
1. **Training the Model**:
   - The YOLO model is trained using a dataset from Roboflow. The dataset contains images labeled with instances of fire.
   - The model is trained and validated using the provided training script.

2. **Running the Fire Detection Alarm**:
   - The trained YOLO model is loaded.
   - The script captures frames from the webcam and uses the model to detect fire.
   - If fire is detected, an alert sound is played. If no fire is detected, the sound stops.

## Requirements
- Python 3.6+
- OpenCV
- Ultralytics
- Pygame
- Roboflow

You can install the required packages using:
```sh
pip install opencv-python-headless ultralytics pygame roboflow
```

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
