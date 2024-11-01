import re


def generate_regex_patterns(emails):
    regex_emails = {}
    for email in emails:
        # Constructing regex pattern for each email address
        domain = email.split('@')[-1]
        regex_pattern = r"[\w.%+-]+@" + re.escape(domain) + r"\b"
        regex_emails[email] = regex_pattern

    return regex_emails

# Write Regex to File
def write_regex_patterns_to_document(output_file_path, regex_emails):
    with open(output_file_path, "w") as file:
        file.write("Regex patterns for email addresses:\n")
        for email, regex_pattern in regex_emails.items():
            file.write(f"{email}: {regex_pattern}\n")

# Read emails from emails.txt
def read_emails_from_file(emails_file_path):
    with open(emails_file_path, "r") as file:
        emails = file.read().splitlines()
    return emails

# Main function
def main():
    # Google Alert Center Email Addresses added to emails.txt
    emails_file_path = "emails.txt"
    output_file_path = "regex_patterns.txt"

    emails = read_emails_from_file(emails_file_path)

    # Generate regex patterns for filtered emails
    regex_emails = generate_regex_patterns(emails)

    # Write regex patterns to a text document
    write_regex_patterns_to_document(output_file_path, regex_emails)
    print(f"Regex patterns for email addresses written to {output_file_path}")


if __name__ == "__main__":
    main()
