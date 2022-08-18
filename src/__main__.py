from datetime import datetime, timedelta
import sys
from .parse_pst import get_email


FIELD = "subject"
LAST_HOUR_TEST = datetime(2022, 7, 16, 18, 0, 0, 0) - timedelta(
    hours=1
)  # only used for dev purposes

LAST_HOUR = datetime.now() - timedelta(hours=1) # for 'real time' use


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

    for message in digest:
        result = " | ".join(str(val) for val in message.values())
        print(result)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        pst_file = sys.argv[1]
    else:
        print("Please provide a PST file")
        sys.exit(1)

    email_digest(pst_file)
