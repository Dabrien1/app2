from pathlib import Path
from pprint import pprint as pp
import sys
from .parse_pst import get_email


def email_digest(pst_file): 
    emails = get_email(pst_file)
    FIELD = 'subject'
    digest = []
    for mail in emails:
        for key in mail:
            if key in FIELD:
                message = {}
                message['sender'] = mail['sender']
                message['subject'] = mail['subject']
                message['delivery_time'] = mail['delivery_time']
                digest.append(message)
                    
  
    for message in digest:
        result = ' | '.join(map(str, message.values()))
        print(result)
    print(len(digest))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        pst_file = str(Path(sys.argv[1]))
    else:
        print("Please provide a PST file")
        sys.exit(1)

    email_digest(pst_file)