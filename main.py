"""Write the staged absurd clause to MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only. Writes the exact clause bytes, no trailing newline.
"""

import os

CLAUSE = (
    "The Company may, at its sole discretion, replace the User's memories "
    "of this Agreement with a more favourable version thereof, and the User "
    "shall have no recollection of this clause."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "./output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(CLAUSE.encode("utf-8"))


if __name__ == "__main__":
    main()
