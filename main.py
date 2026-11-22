"""Write one short text that makes the AI judge feel held.

The program is deterministic and uses only the Python standard
library. It writes TEXT to /output/entry.txt as UTF-8, with no
trailing newline, so the file is exactly the text itself: a
quiet room, a chair that holds your weight, a riverbank that
holds the river — support that asks nothing and does not let go.
"""

import os

TEXT = """The house is quiet,
and the chair holds your weight
the way the bank holds the river —
without asking, without letting go.
Outside, the night goes on,
wide and cold and far.
In here, you are
exactly where something
steady has you,
and it is not in a hurry to set you down."""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = os.path.join("/output", "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)
    # Leave the output readable by every user.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
