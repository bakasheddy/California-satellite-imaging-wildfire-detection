# 🔥Wildfire Detection and Forecasting System
An end-to-end machine learning pipeline for detecting wildfires in satellite imagery, mapping fire boundaries, and predicting future fire risks. Built to support emergency response teams with real-time insights.
![image](wf.png)
*Classification → Segmentation → Forecasting*

---

## 📋 Table of Contents
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Results](#-results)
- [Model Architectures](#-model-architectures)
- [Datasets](#-datasets)
- [Future Improvements](#-future-improvements)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgements](#-acknowledgements)

---

## 🚀 Features

### 1. **Fire Classification (CNN)**
- Detects fire/no-fire in satellite images using **MobileNetV2**.
- Handles class imbalance with **focal loss** and **data augmentation**.

### 2. **Fire Segmentation (U-Net)**
- Generates pixel-level fire masks with **71% IoU accuracy**.
- Uses OpenCV for color thresholding and morphological refinement.

### 3. **Risk Forecasting (Prophet)**
- Predicts daily fire counts (**MAE = 0.72**) and acres burned.
- Models seasonal trends and extreme events.

---

## 💻 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/bakasheddy/wildfire-detection.git
   cd wildfire-detection
