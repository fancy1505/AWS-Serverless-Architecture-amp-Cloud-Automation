# AWS-Serverless-Architecture-amp-Cloud-Automation
# elb-5xx-error-alert-lambda
# System flow:
•	User Traffic → ELB → CloudWatch → Lambda → SNS → Email
•	ELB generates 5xx errors 
•	CloudWatch stores metrics 
•	Lambda checks metrics every 5 mins 
•	If errors > threshold → sends alert via SNS
# Step1: Launched EC2 Instance and Connected to EC2 and ran below commands
sudo yum update -y
sudo yum install httpd -y
sudo systemctl start httpd
sudo systemctl enable httpd
<img width="932" height="304" alt="image" src="https://github.com/user-attachments/assets/f8016e8d-462f-4c2e-b3d5-1e78506ecd7a" />
<img width="940" height="375" alt="image" src="https://github.com/user-attachments/assets/3731593f-e1c4-44b2-bfb1-7b7c5c9a4283" />
<img width="940" height="632" alt="image" src="https://github.com/user-attachments/assets/303ab990-7977-49c5-9b61-60b9c6a4b327" />
# ELB(Elastic load balancer) has been setup
<img width="940" height="489" alt="image" src="https://github.com/user-attachments/assets/9679eee5-640a-4a21-84b0-61ca9014614f" />
<img width="940" height="445" alt="image" src="https://github.com/user-attachments/assets/5b64408b-b46d-4dc2-b334-0c62fffec2b2" />
<img width="940" height="428" alt="image" src="https://github.com/user-attachments/assets/6cd9ff04-7f4b-41b7-90ea-a90537c32220" />

# Step 2: Created SNS Topic (Notification System)
<img width="940" height="238" alt="image" src="https://github.com/user-attachments/assets/b44c129b-b154-4cf6-a9eb-2e3424cf254e" />
<img width="940" height="346" alt="image" src="https://github.com/user-attachments/assets/34f50095-01b1-415b-83fe-e6dafc5e7490" />

# Step 3: Created IAM Role for Lambda
<img width="940" height="379" alt="image" src="https://github.com/user-attachments/assets/7cf78334-e0bb-4362-8cc2-809570c7c68e" />
<img width="940" height="409" alt="image" src="https://github.com/user-attachments/assets/b9db5c8b-56b9-4ef3-9807-f312b0cc84bf" />

# Step 4: Created Lambda Function
<img width="940" height="387" alt="image" src="https://github.com/user-attachments/assets/735e31e0-adf7-4d46-aaaa-df9f245e0dd8" />

# Deployed code in lambda function
<img width="940" height="495" alt="image" src="https://github.com/user-attachments/assets/5ec7699d-169c-4e4b-9cd8-945aafeb12fa" />

# Configured schedule event bridge for every 5 mins
<img width="940" height="454" alt="image" src="https://github.com/user-attachments/assets/db728136-ec99-4524-bc3f-b2792376930b" />
# Expected output
<img width="940" height="502" alt="image" src="https://github.com/user-attachments/assets/0619f016-2b7a-42a0-86c7-077034d28c43" />
<img width="940" height="473" alt="image" src="https://github.com/user-attachments/assets/73ff998e-ff25-499e-8398-f4bddc9f4bd6" />
<img width="940" height="391" alt="image" src="https://github.com/user-attachments/assets/7e48756e-2411-404e-ac6f-e14e00161897" />
















