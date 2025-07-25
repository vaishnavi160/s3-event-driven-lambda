# 📦 AWS Lambda Triggered by S3 - Event-Driven Architecture Demo

This project demonstrates how to use **AWS Lambda** to automatically trigger a function when a new object is uploaded to an **Amazon S3** bucket.

---

## 🚀 Overview

Whenever a file is uploaded to a specified S3 bucket, it triggers a Lambda function that:
- Extracts metadata (filename, size, etc.)
- Logs the details to CloudWatch (or performs a simple transformation/task)

This is a basic example of **event-driven serverless architecture** using AWS.

---

## 🛠️ Architecture

User Uploads File → S3 Bucket → S3 Event Notification → Lambda Triggered → Logs Metadata

---
## 🧰 Technologies Used

- AWS Lambda
- Amazon S3
- IAM Roles & Policies
- CloudWatch Logs
- (Optional: AWS CLI / Boto3 / Terraform for deployment)

---

## 📁 Project Structure

├── lambda_function.py
├── event.json               # Sample S3 event for local testing
├── README.md

---

## 📁 Project Structure

- Upload a file to the S3 bucket
- S3 sends an event notification to trigger the Lambda function
- The Lambda function runs and processes the event
- You can view logs in Amazon CloudWatch

---

## 🔒 IAM Permissions
Your Lambda function should have the following minimum permissions:

- "s3:GetObject"
- "logs:CreateLogGroup"
- "logs:CreateLogStream"
- "logs:PutLogEvents

---

## 🧩 Adding Dependencies to Lambda
If your Lambda function uses external Python libraries (e.g., requests, pandas, boto3 outside the default), you’ll need to bundle your code with its dependencies and upload it as a .zip file.

---

## Diagram

<img width="1273" height="530" alt="image" src="https://github.com/user-attachments/assets/f5f34bb5-331f-4242-bb46-40164b0ef25a" />

---

## CloudWatch Logs Output 

<img width="1575" height="634" alt="image" src="https://github.com/user-attachments/assets/8b263f5a-586f-436e-b162-3de902be73a0" />
