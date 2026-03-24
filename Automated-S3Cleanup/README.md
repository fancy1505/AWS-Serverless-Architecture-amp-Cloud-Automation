# Automated S3 Bucket Cleanup Using AWS Lambda and Boto3
# Concept Diagram
 # User
  │
  ▼
# AWS Lambda
  │
  │ Uses IAM Role
  ▼
# IAM Role (AmazonS3FullAccess)
  │
  ▼
# Amazon S3 Bucket
  │
  ▼
# Deletes files older than 30 days

# Step 1: S3 Setup
1.	Open the **Amazon S3 console.
2.	Click Create bucket.
3.	Uploaded several files to the bucket, Ensuring that some files will be deleted after test.
   <img width="940" height="391" alt="image" src="https://github.com/user-attachments/assets/0cab0de5-facf-4220-9a7f-da0fa9d95aa3" />
  # Upload Files for testing purpose
  <img width="940" height="411" alt="image" src="https://github.com/user-attachments/assets/e35b9fe3-b1a2-4a6b-82a7-163fd956ce73" />
  <img width="940" height="391" alt="image" src="https://github.com/user-attachments/assets/8049e30f-895c-4fc3-a72c-4200f354ebba" />
 # Step 2: Create IAM Role for Lambda
1.	Open the **AWS Identity and Access Management console.
2.	Click Roles → Create Role.
3.	Choose AWS Service → Lambda.
4.	Attach the policy:Step 2: Create IAM Role for Lambda
1.	Open the **AWS Identity and Access Management console.
2.	Click Roles → Create Role.
3.	Choose AWS Service → Lambda.
4.	Attach the policy:
	<img width="940" height="412" alt="image" src="https://github.com/user-attachments/assets/537c46b2-df2f-4e80-bb56-29d140eb85c5" />
  
  # Step 3: Create Lambda Function
  <img width="940" height="512" alt="image" src="https://github.com/user-attachments/assets/b1874f7b-370c-41a1-ab83-6b3618fae97e" />
  
  # Step 4: Lambda Python Code (Boto3)
  <img width="940" height="446" alt="image" src="https://github.com/user-attachments/assets/76e9c4d8-8ed1-486a-9dea-25666a594431" />
  
  # Step 6: Created Test Event for output
# After Writing the Code
1️⃣ Click Deploy
2️⃣ Click Test
3️⃣ Create test event:
<img width="940" height="471" alt="image" src="https://github.com/user-attachments/assets/6aeeab7b-77a8-421d-9a14-6911786297cb" />
# Expected Log Output
In Amazon CloudWatch logs we observed 
<img width="940" height="467" alt="image" src="https://github.com/user-attachments/assets/7a15c4d9-2221-4a5d-8b3a-eb3acc2193ea" />











