import pulumi
from pulumi_aws import ec2

# Create a VPC
vpc = ec2.Vpc("axat_vpc", cidr_block="10.0.0.0/16")

# Create a public subnet
public_subnet = ec2.Subnet(
    "axat_public_subnet",
    vpc_id=vpc.id,
    cidr_block="10.0.1.0/24",
    map_public_ip_on_launch=True
)

# Create an Internet Gateway
internet_gateway = ec2.InternetGateway("axat_internet_gateway", vpc_id=vpc.id)


# Create a route table for the VPC
route_table = ec2.RouteTable("axat_route_table", vpc_id=vpc.id)

# Create a default route for the public subnet
route = ec2.Route(
    "axat_default_route",
    route_table_id=route_table.id,
    destination_cidr_block="0.0.0.0/0",
    gateway_id=internet_gateway.id
)

# Associate the route table with the public subnet
route_table_association = ec2.RouteTableAssociation(
    "axat_route_table_association",
    subnet_id=public_subnet.id,
    route_table_id=route_table.id
)

# Create a Security Group to allow HTTP(S) traffic
security_group = ec2.SecurityGroup(
    "axat_security_group",
    vpc_id=vpc.id,
    ingress=[
        {
            "protocol": "tcp",
            "from_port": 80,
            "to_port": 80,
            "cidr_blocks": ["0.0.0.0/0"],
        },
        {
            "protocol": "tcp",
            "from_port": 443,
            "to_port": 443,
            "cidr_blocks": ["0.0.0.0/0"],
        },
    ]
)

# Create an EC2 instance running a web server
# Replace `AMI_ID` with the appropriate ID for your region
instance = ec2.Instance(
    "axat_ec2_instance",
    ami="ami-0889a44b331db0194",
    instance_type="t2.micro",
    subnet_id=public_subnet.id,
    vpc_security_group_ids=[security_group.id],
    user_data="""#!/bin/bash
echo "Hello, World!" > index.html
nohup busybox httpd -f -p 80 &
""",
    tags={"Name": "web-server-instance"},
)

# Expose the public IP address of the EC2 instance
pulumi.export("instance_public_ip", instance.public_ip)