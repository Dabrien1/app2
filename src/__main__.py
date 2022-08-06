from pathlib import Path
import sys
from .parse_pst import get_email


def email_digest(pst_file): 
    '''function to scan target pst every hour and output a digest of recent activity'''
    test = get_email(pst_file)
    print(test)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        pst_file = Path(sys.argv[1])
    else:
        raise ValueError("no pst file provided")

    email_digest(pst_file)