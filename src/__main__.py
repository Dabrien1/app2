import os
import sys
from datetime import datetime, timedelta

import simpleaudio as sa

from .parse_pst import get_email

FIELD = "subject"
LAST_HOUR_TEST = datetime(2022, 7, 16, 18, 0, 0, 0) - timedelta(
    hours=1
)  # only used for dev purposes

LAST_HOUR = datetime.now() - timedelta(hours=1)  # for 'real time' use
OUTPUT_FILE = "digest.txt"
ALARM_FILE = "alarm.wav"


def _is_windows():
    """
    https://stackoverflow.com/a/1325587
    """
    return os.name == "nt"


def create_digest_of_latest_emails(pst_file):
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

    with open(OUTPUT_FILE, "w") as output:
        for message in digest:
            result = " | ".join(str(val) for val in message.values())
            output.write(f"{result}\n")


def play_alarm_sound():
    sa.WaveObject.from_wave_file(ALARM_FILE).play()


def open_digest_in_text_editor(text_file):
    open_cmd = "start" if _is_windows() else "open"
    os.system(f"{open_cmd} {text_file}")  # noqa S605


def main(pst_file):
    create_digest_of_latest_emails(pst_file)
    play_alarm_sound()
    open_digest_in_text_editor(OUTPUT_FILE)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        pst_file = sys.argv[1]
    else:
        print("Please provide a PST file")
        sys.exit(1)

    main(pst_file)
