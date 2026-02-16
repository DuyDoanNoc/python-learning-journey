print("=== PROFESSIONAL EMAIL GENERATOR ===")
print()

# Function to generate professional email
def generate_email(recipient, position, company_name):
    """Generate professional email for job application"""

    my_name = "Duy Doan"
    my_current_role = "Manual Tester"
    my_company = "Simpson Strong-tie"
    my_skills = ["Python", "Manual Testing", "Selenium (learning)", "Git"]

    email = f"""
To: {recipient}
Subject: Application for {position} Position

Dear Hiring Manager,
My name is {my_name}, currently working as a {my_current_role} at {my_company}.
I am writing to express my strong interest in the {position} position at {company_name}.
I have been actively developing my skills in:
"""
    for skill in my_skills:
        email += f" - {skill}\n"
    email += f"""
I am passionate about automation testing and commited to delivering high-quality work.
I would welcome the oppotunity to contribute to {company_name}'s success.
Thank you for considering my application. I look forward to hearing from you.

Best regards,
{my_name}
{my_current_role} -> {position} (Transition In Progress)
Github: https://github.com/DuyDoanNoc
"""
    return email

# Generate sample emails
print(generate_email(
    recipient="recruter@company.com",
    position="Automation Tester",
    company_name="Tech Company"
))

print("\n" + "="*60 + "\n")

# Email signature generator
def generate_signature(name, role, linkedin=None, github=None):
    """Generate email signature"""

    sig = f"""
---
{name}
{role}
"""
    if linkedin:
        sig += f"LinkedIn: {linkedin}\n"
    if github:
        sig += f"Github: {github}\n"

    return sig

print(generate_signature(
    name="Duy Doan",
    role="Manual Tester -> Automation Tester",
    github="https://github.com/DuyDoanNoc"
))