# Terraform Project

This Terraform project creates an AWS infrastructure with a VPC, a public subnet, an internet gateway, a route table, a security group, and an EC2 instance with a web server.

## Requirements
To use this project, you need the following:

- An AWS account
- AWS CLI installed and configured with your credentials
- Terraform CLI installed on your local machine

## Usage

- Navigate to the Terraform folder
```bash
cd terraform_project
```
- Review the changes that Terraform will make:
```bash
terraform plan
```
- Apply the changes to create the AWS infrastructure:
```bash
terraform apply
```
- When prompted, type yes to confirm the changes.
- Wait for Terraform to create the infrastructure.
- Once the infrastructure is created, you can access the web server on the EC2 instance 
- To destroy the infrastructure when you are done, run:
```bash
terraform destroy
```
- When prompted, type yes to confirm the destruction.


<br>

# Pulumi Project
This Pulumi project creates an AWS infrastructure with a VPC, a public subnet, an internet gateway, a route table, a security group, and an EC2 instance with a web server.

## Requirements
To use this project, you need the following:
 - AWS account
 - Pulumi CLI installed on local machine
 - Python 3.7 or later installed on your local machine
 - The Pulumi AWS Python SDK installed

 ## Usage
 - Navigate to Pulumi Project folder
 ```bash
 cd pulumi_project
 ```
 - Deploy the Pulumi program to create the AWS infrastructure:
 ```bash 
 pulumi up
 ```
 - When prompted, type yes to confirm the changes.
 - Wait for Pulumi to create the infrastructure.
 - Once the infrastructure is created, you can access the web server on the EC2 instance
 - To destroy the infrastructure when you are done, run:
```bash 
pulumi destroy
```
- When prompted, type yes to confirm the destruction.



