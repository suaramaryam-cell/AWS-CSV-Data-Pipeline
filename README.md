# AWS-CSV-Data-Pipeline
  
## 1. What it does   
This project demonstrates how to build a **data pipeline** on AWS that ingests raw CSV files, transforms them, and outputs clean structured data.  
It helps **manual CSV cleaning and preparation** by automating extraction, transformation, and loading (ETL) with AWS Glue.  

## 2. Introduction  
Companies need to process raw files into usable formats for analytics and machine learning.  
This project showcases a simple **ETL pipeline** on AWS where:  
- CSV is uploaded to **Amazon S3**.  
- **AWS Glue** reads, transforms, and outputs only the required columns.  
- The final processed dataset is written back to S3 for reporting and analytics.  

## 3. Architecture Diagram  

## 4. User Instructions  
### Requirements  
  - S3 Bucket  
- AWS Glue Studio
- IAM
- Lambda
 
### Steps  
1. Upload your CSV file into an S3 bucket   
2. Open **AWS Glue Studio**.  
3. Create a new job and paste the script provided in AWS Lambda  
4. Update the S3 path in the script to match your bucket.  
5. Assign an IAM role with S3 + Glue permissions.  
6. Run the job and check output in s3.  


## 5. My Instructions (How I built it)  

This project was built with:  
- **AWS Glue** for ETL  
- **Amazon S3** for storage  
- **IAM Roles** for security  
- **Python** for AWS Lambda

### Steps I followed:  
- Created an S3 bucket and uploaded my CSV file 
- Configured a Glue job with a Python script in lambda to transform the CSV.  
- Selected worker nodes and IAM roles.  
- Ran the job and verified results in S3.  

  <img width="1366" height="768" alt="2025-09-21" src="https://github.com/user-attachments/assets/5cc57645-b4d5-449d-a954-66848578752f" />
  <img width="1366" height="768" alt="2025-09-21 (5)" src="https://github.com/user-attachments/assets/e65d18e4-b850-4121-bd2d-1c6a2305d0af" />
  <img width="1366" height="768" alt="2025-09-21 (4)" src="https://github.com/user-attachments/assets/953c40a2-0129-4122-9850-62b14e6e9ca3" />
  <img width="1366" height="768" alt="2025-09-21 (3)" src="https://github.com/user-attachments/assets/5f4cd908-5f61-4b41-83ba-e7db9dc8e225" />
  <img width="1366" height="768" alt="2025-09-21 (2)" src="https://github.com/user-attachments/assets/145d5594-37e2-4638-8c71-ee41a62d86e1" />
  <img width="1366" height="768" alt="2025-09-21 (1)" src="https://github.com/user-attachments/assets/10839c2e-de4b-451e-babe-7d7c260cecb9" />
  
## 8. My Issues  
- Currently only works with CSV (not zipped files).  
- Data quality checks are basic (column count only).  
- Requires manual update of S3 paths in script.  

## 9. Hire Me 💼  
   Email: suaramaryam@gmail.com

 LinkedIn: www.linkedin.com/in/maryam-suara
  


