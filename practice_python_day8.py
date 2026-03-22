
def validate_name(username):
    if not username:
        return False
    if not username.isalnum():
        return False
    if not (0 <= len(username) <= 20):      # Tên phải có ít nhất 1 ký tự
        return False
    return True

def validate_age(userage):
    if not userage:
        return False
    if not userage.isdigit():
        return False
    if not (0 <= int(userage) <= 130):           # Tuổi phải bắt đầu bằng 1
        return False
    return True

def validate_email(useremail):
    if not useremail:
        return False
    if "@" not in useremail or "." not in useremail:          # mail phải có @mail.com nên minimum là 9
        return False
    return True

def validate_status(userstatus):
    if not userstatus:
        return False
    if userstatus not in ("active", "inactive"):
        return False
    return True

raw_data = [
    "John, 28, john@mail.com, active",
    "Jane, abc, jane@mail, inactive",
    "  , 35, bob@mail.com, active",
    "Alice, 22, alice@mail.com, unknown",
]

for data in raw_data:
    fields = data.split(",")
    name = fields[0].strip()
    age = fields[1].strip()
    email = fields[2].strip()
    status = fields[3].strip()

    name_ok = validate_name(name)
    age_ok = validate_age(age)
    email_ok = validate_email(email)
    status_ok = validate_status(status)

    # ↓ NẰM TRONG loop (thụt vào 1 tab)
    errors = []
    if not name_ok:
        errors.append("name is empty")
    if not age_ok:
        errors.append(f"age={age} (invalid)")
    if not email_ok:
        errors.append(f"email={email} (invalid)")
    if not status_ok:
        errors.append(f"status={status} (invalid)")

    if not errors:
        print(f"[VALID]   {name} | age={age} | {email} | {status}")
    else:
        print(f"[INVALID] {name} | {', '.join(errors)}")
