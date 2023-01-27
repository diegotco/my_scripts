# define file paths
file_a = 'admin_users.txt'
file_b = 'zd_users.txt'

# open files and read email addresses
with open(file_a, 'r') as f:
    emails_a = set(f.read().splitlines())

with open(file_b, 'r') as f:
    emails_b = set(f.read().splitlines())

# find matching emails
matching_emails = emails_a.intersection(emails_b)

# save matching emails to a new list
with open('matched_users.txt', 'w') as f:
    for email in matching_emails:
        f.write(email + '\n')