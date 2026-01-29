virtual_machine = {
    "id": "vm-101",
    "ip": "192.168.1.10",
    "status": "running",
    "region": "us-east-1"
}

virtual_machine['status']="stopped"
virtual_machine['instance_type']="t3.large"
print(virtual_machine)
