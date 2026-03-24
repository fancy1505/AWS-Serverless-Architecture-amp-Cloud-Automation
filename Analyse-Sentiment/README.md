# Analyze Sentiment of User Reviews Using AWS Lambda, Boto3, and Amazon Comprehend
<img width="940" height="551" alt="image" src="https://github.com/user-attachments/assets/be69664f-e2b6-4d3b-9752-09582ac9b268" />
# Created IAM Role for Lambda
<img width="940" height="281" alt="image" src="https://github.com/user-attachments/assets/a0dbf6ff-0be0-48a5-ba83-2a614c161335" />
<img width="940" height="409" alt="image" src="https://github.com/user-attachments/assets/d90bf257-78aa-4105-be9f-3e71796cd5b9" />
# Created Lambda Function
1. Go to Lambda
•	Open AWS Console → Lambda 
•	Click Create Function 
2. Configure
•	Function name: sentiment-analysis-function 
•	Runtime: latest Python 
•	Execution role:
 Choose Use existing role → select lambda-comprehend-role
<img width="940" height="422" alt="image" src="https://github.com/user-attachments/assets/84fbbee7-0d0d-4b30-9644-fb98071978b8" />
# Added Python Code (Boto3 + Comprehend)
<img width="940" height="854" alt="image" src="https://github.com/user-attachments/assets/72494087-e848-4b66-9d95-5b08f65f7c66" />
<img width="940" height="654" alt="image" src="https://github.com/user-attachments/assets/66d10f8a-2d5f-4175-8eaa-c396a0f548e0" />


# EXPECTED OUTPUT status code should be 200 but here it is showing 500 because Your account has NOT activated Amazon Comprehend yet as it is very chargeable but understood the concept and all steps are fine.
<img width="940" height="520" alt="image" src="https://github.com/user-attachments/assets/f63bfdba-4227-4c9c-b4d5-13f79426bc46" />
<img width="940" height="443" alt="image" src="https://github.com/user-attachments/assets/e1a7036d-18b3-4339-9321-eea87d07ef4a" />






