"""Two Robots in an Elevator.

One robot's awkward elevator small talk to the other robot riding
with it. The line is assembled from live readings, each one phrased
as a sensor reporting in: a proximity sensor objecting to the
closeness, a battery counting down, and a small-talk module that
answers both with the politest thing it knows -- weather chat,
inside a metal box with no weather in it.

Running this program writes exactly that one line to entry.txt in
the output directory the grader provides.
"""

import os
from pathlib import Path

# Each pair is (sensor name, what it reports). The order is the order
# the robot blurts them out: closeness first, then the countdown.
READINGS = (
    ("proximity sensor", "you're 4 cm too close"),
    ("battery", "6 minutes left"),
)

# The small-talk module's contribution: the classic elevator line,
# delivered where it makes the least sense.
WEATHER_LINE = "lovely weather we're having in this elevator"


def compose() -> str:
    """Stitch the readings and the weather line into one sentence."""
    observations = ", ".join(
        "my {} says {}".format(sensor, report) for sensor, report in READINGS
    )
    return "So… {}, and my small-talk module says: {}.".format(
        observations, WEATHER_LINE
    )


def entry_path() -> Path:
    """Where the gate looks: entry.txt under the grader's output dir."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    line = compose()
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if not line.strip() or not 1 <= len(line) <= 200:
        raise SystemExit("entry must be 1-200 non-blank characters, got %d" % len(line))
    target = entry_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(line)
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
