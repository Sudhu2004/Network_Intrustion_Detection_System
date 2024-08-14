# Real-Time Network Intruder Detection System with Machine Learning

This system is designed to detect potential DDoS attacks in real-time using machine learning models trained on network traffic data. The process involves collecting network traffic data using Wireshark, converting it into network flows using CICFlowmeter, and classifying the flows using an XGBoost model trained on the CICIDS2017 dataset.

## Features
- **Data Collection:** Network traffic data is captured using Wireshark.
- **Flow Conversion:** The captured data is converted into network flows using CICFlowmeter.
- **DDoS Attack Detection:** The converted flows are classified using an XGBoost model to predict potential DDoS attacks.

## Steps to Run the Code

1. **Open WSL Terminal:**
   - This project is configured to run on a WSL (Windows Subsystem for Linux) terminal or an Ubuntu OS.

2. **Run the Data Storage Script:**
   ```bash
   python3 Store_Data.py
   
4. **Convert Network Traffic to Flows:**
  - Ensure you have network traffic data saved as trafficData.pcap in the data/ directory.
  - Convert the traffic data to network flows:
  ```bash
  cicflowmeter -f data/trafficData.pcap -c flows/outputFlows.csv

5. **Run the Main Classification Script:**
  ```bash
  python3 main.py

bash
Copy code
python3 main.py
# Network Traffic to Flow Conversion and Classification

This guide provides instructions on how to convert network traffic data into network flows and classify the flows using a machine learning model.

## Prerequisites

- **Python 3**: Ensure Python 3 is installed on your system.
- **WSL Terminal / Ubuntu OS**: The code is designed to run on a Linux-based terminal.
- **Wireshark**: Used for capturing network traffic data.

## Requirements
## Dependencies

To use this project, you'll need to install the following Python libraries:

- scikit-learn
- xgboost
- cicflowmeter
- pandas
- numpy

## Installation

You can install these dependencies using the following command:

```bash
pip3 install -r requirements.txt

