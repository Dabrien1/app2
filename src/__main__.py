from curses import beep
import os
import sys
from playsound import playsound
from datetime import datetime, timedelta

from .parse_pst import get_email

FIELD = "subject"
LAST_HOUR_TEST = datetime(2022, 7, 16, 18, 0, 0, 0) - timedelta(
    hours=1
)  # only used for dev purposes

LAST_HOUR = datetime.now() - timedelta(hours=1)  # for 'real time' use


def is_windows():
    """
    https://stackoverflow.com/a/1325587
    """
    return os.name == "nt"


def open_text_file(text_file):
    open_cmd = "start" if is_windows() else "open"
    os.system(f"{open_cmd} {text_file}")  # noqa S605


def email_digest(pst_file):
    emails = get_email(pst_file)
    digest = []
    
    for mail in emails:
        for key in mail:
            if key in FIELD:
                if mail["delivery_time"] >= LAST_HOUR_TEST:
                    digest.append(
                        {
                            "sender": mail["sender"],
                            "subject": mail["subject"],
                            "delivery_time": mail["delivery_time"],
                        }
                    )

    # TODO: write to a file
    with open('digest.txt', 'w') as output:
        for message in digest:
            result = " | ".join(str(val) for val in message.values())
            output.write(f'{result}\n')
        output.close()
        return  
        
    # return filename


def main(pst_file):
    digest_file = email_digest(pst_file)
    #url = urllib.request.urlopen('https://soundbible.com/2218-Service-Bell-Help.html#google_vignette')
    # TODO: play audio sound
    #playsound(url)
    open_text_file(digest_file)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        pst_file = sys.argv[1]
    else:
        print("Please provide a PST file")
        sys.exit(1)

    main(pst_file)
