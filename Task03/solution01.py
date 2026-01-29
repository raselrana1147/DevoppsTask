port_number="8080"

port_int=int(port_number)

if port_int in range(1,65636):
    print("Valid")
else:
    print("Invalid")


