provider "aws" {
  region = "us-west-2"
}

# Creating a VPC
resource "aws_vpc" "my_vpc" {
  cidr_block = "10.0.0.0/16"
}

# Creating a public subnet within the VPC
resource "aws_subnet" "public_subnet" {
  vpc_id     = aws_vpc.my_vpc.id
  cidr_block = "10.0.1.0/24"
}

# Creating an internet gateway
resource "aws_internet_gateway" "my_igw" {
  vpc_id = aws_vpc.my_vpc.id
}

# Creating a route table
resource "aws_route_table" "my_route_table" {
  vpc_id = aws_vpc.my_vpc.id
}

# Creating a route to the internet gateway
resource "aws_route" "my_route" {
  route_table_id         = aws_route_table.my_route_table.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.my_igw.id
}

# Creating a security group
resource "aws_security_group" "my_sg" {
  name_prefix = "my_sg"
  vpc_id      = aws_vpc.my_vpc.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Creating EC2 instance with a web server
resource "aws_instance" "my_ec2_instance" {
  ami           = "ami-04e914639d0cca79a"
  instance_type = "t2.micro"
  vpc_security_group_ids = [aws_security_group.my_sg.id]
  subnet_id     = aws_subnet.public_subnet.id

  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install -y httpd
              systemctl start httpd
              systemctl enable httpd
              echo "<html><body><h1>Hello, World!</h1></body></html>" > /var/www/html/index.html
              EOF
}

output "public_dns_name" {
  value = aws_instance.my_ec2_instance.public_dns
}