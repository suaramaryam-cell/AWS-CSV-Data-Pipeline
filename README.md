# AWS-CSV-Data-Pipeline
  
## 1. What it does   
This project demonstrates how to build a **data pipeline** on AWS that ingests raw CSV files, transforms them, and outputs clean structured data.  
It solves **manual CSV cleaning and preparation** by automating extraction, transformation, and loading (ETL) with AWS Glue.  

---

## 2. Introduction  
In modern data engineering, companies need to process raw files into usable formats for analytics and machine learning.  
This project showcases a simple **ETL pipeline** on AWS where:  

- CSV is uploaded to **Amazon S3**.  
- **AWS Glue** reads, transforms, and outputs only the required columns.  
- The final processed dataset is written back to S3 for reporting and analytics.  

## 3. Architecture Diagram  

---

## 4. User Instructions  

### Requirements  
- AWS Account  
- S3 Bucket  
- AWS Glue Studio  

### Steps  
1. Upload your CSV file into an S3 bucket (`s3://your-bucket/input/`).  
2. Open **AWS Glue Studio**.  
3. Create a new job and paste the script provided in this repo.  
4. Update the S3 path in the script to match your bucket.  
5. Assign an IAM role with S3 + Glue permissions.  
6. Run the job and check output in `s3://your-bucket/output/`.  

---

## 5. My Instructions (How I built it)  

This project was built with:  
- **AWS Glue** for ETL  
- **Amazon S3** for storage  
- **IAM Roles** for security  
- **Python (PySpark)** inside Glue scripts  

### Steps I followed:  
- Created an S3 bucket and uploaded `coffee_sales.csv`.  
- Configured a Glue job with a Python script to transform the CSV.  
- Selected worker nodes and IAM roles.  
- Ran the job and verified results in S3.  

---

## 6. Screenshots  

📸 Add these screenshots into a `/screenshots` folder:  

1. Sample CSV File  
   ![Sample CSV](./screenshots/sample_csv.png)  

2. S3 Bucket with CSV Uploaded  
   ![S3 Input](./screenshots/s3_input.png)  

3. AWS Glue Studio Script Editor  
   ![Glue Script](./screenshots/glue_script.png)  

4. Glue Job Run Success  
   ![Job Run](./screenshots/job_success.png)  

5. Output in S3  
   ![Output S3](./screenshots/s3_output.png)  

---

## 7. Contributors Expectations  
If you’d like to contribute:  
- Fork the repo.  
- Add new transformation logic (e.g., aggregations, filtering by date).  
- Submit a pull request with clear explanations.  

---

## 8. Known Issues  
- Currently only works with `.csv` (not zipped files).  
- Data quality checks are basic (column count only).  
- Requires manual update of S3 paths in script.  

---

## 9. Hire Me 💼  
I’m open to **cloud engineering / data engineering** opportunities.  

📧 Email: [suaramaryam@gmail.com](mailto:suaramaryam@gmail.com)  
🔗 LinkedIn: [Your LinkedIn Link]  
🐙 GitHub: [Your GitHub Profile Link]  

---
