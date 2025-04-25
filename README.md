# 🪣 S3 Lifecycle Buddy

Automate Amazon S3 lifecycle policies using Python and AWS CLI — from bucket creation to cleanup.

---

## 📌 Project Overview

**S3 Lifecycle Buddy** is a fully automated Python tool that manages the entire lifecycle of an S3 bucket using code — no Console clicks required.

This project handles:
- ✅ Region-aware **S3 bucket creation**
- ✅ Lifecycle policy application via **inline JSON**
- ✅ Upload of a **test object**
- ✅ Optional cleanup that deletes both the object and the bucket

It’s a real-world cloud automation use case for **cost optimization**, **policy enforcement**, and **DevOps-style AWS control**.

---

## 🎯 Why This Project Matters

AWS storage can quietly rack up costs without proper management. This script demonstrates how to:
- Enforce data retention using lifecycle rules
- Reduce cloud waste from forgotten dev/test buckets
- Automate cleanup workflows to avoid manual intervention

---

## 🛠️ Technologies Used

- **Python 3**
- **AWS CLI** – for command-line resource management
- **boto3** – AWS SDK for Python
- **subprocess** – to bridge Python with CLI commands

---

## 📁 Project Structure

```
s3-lifecycle-buddy/
├── s3_lifecycle.py       # Main Python script
├── README.md              # Project documentation
├── test_upload.txt        # Auto-generated test file
├── .gitignore             # Git cleanup rules
└── venv/       

```
---

## 🚀 How It Works

1. **Bucket Creation**  
   Creates an S3 bucket using AWS CLI logic that adjusts automatically for `us-east-1` region behavior.

2. **Lifecycle Policy**  
   Applies a lifecycle policy via inline JSON to automatically delete objects after 1 day.

3. **Test Upload**  
   Generates and uploads a sample file to validate the lifecycle configuration.

4. **Cleanup (Optional)**  
   Deletes all objects and the bucket using:
   ```bash
   aws s3 rb s3://bucket-name --force
   ```

   ---

## ▶️ How to Run

### 🧱 Prerequisites

- Python 3 installed
- AWS CLI installed and configured (run: aws configure)
- Virtual environment (optional but recommended)
- Boto3 installed in your environment

---

### 📦 Setup Steps

```
# 1. Create a virtual environment (optional but recommended)
python -m venv venv

# 2. Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

# 3. Install boto3 if not already installed
pip install boto3

# 4. Run the script
python s3_lifecycle.py

```

---

📎 License
MIT License — Free to use, modify, and distribute.
