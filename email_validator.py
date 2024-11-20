def email_validator(email):
    # Local part
    mail = "muiz @gmail.com@mail.com"
    part = email.split("@")
    local_part = part[0]
    local = True
    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    upper_letters = lower_letters.upper()
    digits = "0123456789"
    characters = "!#$%&'*+-/=?^_`{|}~"
    period = "."
    hyphen = "-"

    if len(part) != 2:
        local = False

    if local_part[0] in period:
        local = False
    elif local_part[-1] in period:
        local = False
    elif ".." in local_part:
        local = False

    for x in local_part:
        if x not in lower_letters and x not in upper_letters and x not in digits and x not in characters:
            local = False


    # Domain part
    domain_part = part[1]
    domain = True

    if domain_part[0] in period:
        domain = False
    elif domain_part[-1] in period or domain_part[-1] in hyphen:
        domain = False
    elif ".." in domain_part:
        domain = False
    elif "--" in domain_part:
        domain = False
    elif "-." in domain_part:
        domain = False

    label = domain_part.split(".")
    if len(label) < 2:
        domain = False

    TLD = label[-1]
    if len(TLD) < 2:
        domain = False
    elif TLD[0] in hyphen:
        domain = False

    label1 = label[0]
    for y in label1:
        if y not in lower_letters and y not in upper_letters and y not in digits and y not in hyphen:
            domain = False


    if local and domain and len(email) <= 253:
        print("True")
    else:
        print("False")

email = input("Enter your email: ")
email_validator(email)
