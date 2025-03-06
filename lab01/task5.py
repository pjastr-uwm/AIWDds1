def create_email_message(subject, body, *, sender="notification@example.com", **kwargs):
    temp = {"subject": subject, "body": body, "sender": sender}
    for key, value in kwargs.items():
        temp[key] = value

    return temp


print(create_email_message("AA", "xx", priority="normal"))
