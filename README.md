
# AWS-Course-Project

This repository provides a comprehensive, automated setup for deploying a highly available and scalable web application infrastructure on AWS using a combination of **Terraform**, **AWS CloudFormation**, and **Python (Boto3)** scripts.

---

## 📌 Project Overview

This project illustrates how to architect and implement a cloud-native application environment using industry-standard AWS services. The key features include:

- Provisioning network resources using **Terraform**
- Deployment of a PHP-based application on **EC2** instances
- **MySQL RDS** integration for data persistence
- Dynamic scaling of compute instances with **Auto Scaling Groups**
- Real-time event logging using **AWS Lambda** and **CloudWatch Logs** triggered by S3 uploads
- Manual and programmatic resource operations through **Boto3 scripts**

---

## 📁 Repository Layout

```
cloud-infra-webapp-deployment/
│
├── terraform/                  # Handles VPC, public/private subnets, security groups, ALB, auto scaling
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
│
├── cloudformation/            # CloudFormation stacks for application layer, RDS, and Lambda function
│   ├── infrastructure-extension.yaml
│   ├── autoscaling.yaml
│   └── lambda-s3-logger.yaml
│
├── boto3-scripts/             # Utility scripts for interacting with AWS services programmatically
│   ├── s3upload.py            # Creates an S3 bucket and uploads files
│   ├── ec2.py                 # Retrieves EC2 instance metadata
│   ├── list_instances.py      # Lists running EC2 instances
│   └── lambda-s3-logger.py    # Triggers the Lambda function manually
│
├── Aws Course Project.jpg     # Visual representation of the system architecture
│
├── README.md                  # Detailed documentation and usage guide
```

---

## 🛠️ Setup & Deployment Instructions

### 1. Clone the Repository

Begin by cloning the project to your local system:

```bash
git clone https://github.com/YOUR_USERNAME/cloud-infra-webapp-deployment.git
cd cloud-infra-webapp-deployment
```

### 2. Provision Networking with Terraform

Navigate to the Terraform directory and deploy the foundational network:

```bash
cd terraform
terraform init
terraform apply
```

This step sets up the VPC, subnets, NAT gateway, route tables, and security groups.

### 3. Launch Application and Database with CloudFormation

Deploy EC2, RDS, and Lambda resources using the CloudFormation templates either through the AWS Console or CLI:

```bash
aws cloudformation deploy --template-file ec2-stack.yaml --stack-name ec2-stack --capabilities CAPABILITY_IAM
aws cloudformation deploy --template-file rds-stack.yaml --stack-name rds-stack --capabilities CAPABILITY_IAM
aws cloudformation deploy --template-file lambda-stack.yaml --stack-name lambda-stack --capabilities CAPABILITY_IAM
```

### 4. Upload to S3 and Trigger Lambda

Once deployed, upload any file to the configured S3 bucket to automatically invoke the Lambda function:

```bash
aws s3 cp sample-file.txt s3://your-bucket-name/
```

Check CloudWatch Logs to confirm that the Lambda captured the upload event.

### 5. Use Boto3 Scripts for Manual Interaction

Use Python scripts in the `boto3-scripts/` directory to manage and interact with resources:

- Upload to S3
- List EC2 instances
- Retrieve instance metadata
- Trigger Lambda events

---

✅ Implementation Summary

1. Networking Infrastructure
Created a VPC with a /16 CIDR block.
Configured two public subnets (for the ALB and EC2) and two private subnets (for the RDS).
Established an Internet Gateway for public access and route tables for correct routing.
Used Terraform to automate the provisioning of all networking components.

2. Compute and Database Resources
Deployed EC2 instances behind an Application Load Balancer using CloudFormation.
Configured Launch Templates and Auto Scaling Groups to automatically manage EC2 capacity.
Deployed an RDS MySQL database instance in private subnets with public access disabled.
Verified database connectivity from EC2 instances.

3. Web Application Deployment
Installed and configured a web server on EC2 instances using user data.
Hosted a simple web application accessible via the Load Balancer DNS name.

4. S3 and Lambda Integration
Created an S3 bucket for storing files.
Developed a Lambda function using Python to log file uploads.
Configured the S3 bucket to trigger the Lambda function on each file upload.
Validated logging by checking CloudWatch Logs for file upload events.

5. Monitoring and Observability
Verified that EC2 and RDS metrics appear in CloudWatch.
Confirmed Lambda execution logs are being stored in CloudWatch Logs.

6. Security Configuration
Security Groups created with principle of least privilege:
ALB only allows HTTP (port 80).
EC2 allows inbound traffic only from ALB.
RDS only allows traffic from EC2.
IAM roles assigned to Lambda and EC2 for restricted access to necessary AWS resources.

7. Version Control with GitHub
All Terraform scripts, CloudFormation templates, Lambda code, and Python scripts are maintained in a GitHub repository.
GitHub tracks all changes and supports collaborative development.

## 🖼️ Architecture Summary

This solution architecture features the following components:

- **Custom VPC** with segregated public and private subnets
- **EC2 Instances** running a PHP web application, accessed via an **Application Load Balancer**
- **Auto Scaling Group** for high availability and fault tolerance
- **MySQL RDS Database** hosted in a private subnet for enhanced security
- **Amazon S3** bucket for storing files and static content
- **AWS Lambda Function** that logs S3 file uploads to **CloudWatch Logs**
- **IAM Roles and Policies** that follow least privilege access
- **Security Groups** configured to tightly control traffic flows between layers

---

## 🔒 Security Highlights

- EC2 and RDS security groups are restricted based on application role and subnet location
- IAM roles are scoped to provide minimal access needed for execution
- RDS is isolated within private subnets without public exposure
- All S3 access events are audited through Lambda and CloudWatch

---

## 📈 Testing & Validation

The environment was validated using a combination of:

- Web browser access to the application through ALB
- CLI tools for S3 uploads and Lambda invocations
- CloudWatch monitoring for Lambda and EC2 logs
- Python Boto3 scripts to validate EC2 states and resource management
