import re 

input = "rahul rahul@ibm.com 5034534795 priyanka 847589347258  priya@c.com"

emails = re.findall(r'[\w\.-]+@[\w\.-]+', input)

for email in emails:
    print(email)


