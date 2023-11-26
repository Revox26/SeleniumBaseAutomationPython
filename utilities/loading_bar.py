import sys


def updt(total, progress):
    """
    Displays or updates a console progress bar.

    Original source: https://stackoverflow.com/a/15860757/1391441
    """
    barLength, status = 40, ""
    progress = float(progress) / float(total)
    if progress >= 1.:
        progress, status = 1, ""
    block = int(round(barLength * progress))
    text = "[{}] {:.0f}% {}".format(
        "🟨" * block + "-" * (barLength - block), round(progress * 100, 0),
        status)
    text += "\n"
    sys.stdout.write('\r\n' + text)  # Use carriage return to overwrite the line
    sys.stdout.flush()
