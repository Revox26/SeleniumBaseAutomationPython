import random


def generate_random_icon_list(num_icons=1):
    icon_list = [
        "yin-yang", "yen-sign", "x-ray", "wrench", "won-sign", "wine-glass-alt",
        "wine-glass", "wine-bottle", "window-restore", "window-minimize",
        "window-maximize", "window-close", "wind", "wifi", "wheelchair",
        "weight-hanging", "weight", "wave-square", "water", "warehouse", "wallet",
        "walking", "vr-cardboard", "vote-yea", "volume-up", "volume-off",
        "volume-mute", "volume-down", "volleyball-ball", "voicemail", "viruses",
        "virus-slash", "virus", "vihara", "video-slash", "video", "vials", "vial",
        "vest-patches", "vest", "venus-mars", "venus-double", "venus",
        "vector-square", "utensils", "utensil-spoon", "users-slash", "users-cog",
        "users", "user-times", "user-tie", "user-tag", "user-slash", "user-shield",
        "user-secret", "user-plus", "user-nurse", "user-ninja", "user-minus",
        "user-md", "user-lock", "user-injured", "user-graduate", "user-friends",
        "user-edit", "user-cog", "user-clock", "user-circle", "user-check",
        "user-astronaut", "user-alt-slash", "user-alt", "user", "upload",
        "unlock-alt", "unlock", "unlink", "university", "universal-access",
        "undo-alt", "undo", "underline", "umbrella-beach", "umbrella", "tv",
        "tty", "tshirt", "truck-pickup", "truck-moving", "truck-monster", "truck",
        "trophy", "tree", "trash-restore-alt", "trash-restore", "trash-alt",
        "trash", "transgender-alt", "transgender", "tram", "train", "trailer",
        "traffic-light", "trademark", "tractor", "torii-gate", "torah", "tooth",
        "tools", "toolbox", "toilet-paper-slash", "toilet-paper", "toilet",
        "toggle-on", "toggle-off", "tired", "tint-slash", "tint", "times-circle",
        "times", "ticket-alt", "thumbtack", "thumbs-up", "thumbs-down",
        "thermometer-three-quarters", "thermometer-quarter", "thermometer-half",
        "thermometer-full", "thermometer-empty", "thermometer", "theater-masks",
        "th-list", "th-large", "th", "text-width", "text-height", "terminal",
        "tenge", "temperature-low", "temperature-high", "teeth-open", "teeth",
        "taxi", "tasks", "tape", "tags", "tag", "tachometer-alt", "tablets",
        "tablet-alt", "tablet", "table-tennis", "table", "syringe", "sync-alt",
        "sync", "synagogue", "swimming-pool", "swimmer", "swatchbook", "surprise",
        "superscript", "sun", "suitcase-rolling", "suitcase", "subway",
        "subscript", "stroopwafel", "strikethrough", "street-view", "stream",
        "store-slash", "store-alt-slash", "store-alt", "store", "stopwatch-20",
        "stopwatch", "stop-circle", "stop"
    ]

    num_of_icons = min(num_icons, len(icon_list))

    select_random_icons = random.sample(icon_list, num_of_icons)

    # Convert the list to a string
    icons_string = ", ".join(select_random_icons)

    return icons_string



