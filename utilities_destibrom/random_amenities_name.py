import random

def generate_random_amenities(num_amenities=1):
    amenities_list = [
        "Zen garden",
        "Virtual reality arcade",
        "Rock climbing wall",
        "Petting zoo",
        "Rooftop bar",
        "Outdoor yoga space",
        "Hydroponic farm",
        "Hammock lounge",
        "Artisanal coffee shop",
        "Skydiving simulator",
        "Butterfly conservatory",
        "Trampoline park",
        "Meditation room",
        "Glass-bottomed swimming pool",
        "Outdoor movie theater",
        "Mini golf course",
        "Segway rental",
        "Community book exchange",
        "Ice cream truck",
        "Public sauna",
        "Urban farm",
        "Karaoke bar",
        "Batting cages",
        "Roller skating rink",
        "Board game cafe",
        "Tide pool exhibit",
        "Zip line course",
        "Electric scooter rental",
        "Disc golf course",
        "Archery range",
        "Hot air balloon rides",
        "VR escape room",
        "Labyrinth maze",
        "Outdoor trapeze",
        "Food truck park",
        "Psychic reading booth",
        "Glassblowing studio",
        "Parkour gym",
        "Bungee jumping platform",
        "Art installation gallery",
        "Snow cone stand",
        "Oxygen bar",
        "Community garden",
        "Outdoor chess boards",
        "Street food market",
        "Wildlife observation deck",
        "Stand-up paddleboard rental",
        "Geocaching trail",
        "Ping pong tables",
        "Aerial silk performance space",
        "Tarot card readings",
        "Model train exhibit",
        "Segway tour",
        "Bird watching tower",
        "Synchronized swimming pool",
        "Fishing pond",
        "Indoor trampoline park",
        "Floating restaurant",
        "Pottery studio",
        "Paddleboat rental",
        "Psychic fair",
        "Virtual petting zoo",
        "Outdoor bocce ball court",
        "Reptile sanctuary",
        "Indoor climbing gym",
        "Puzzle room",
        "Wildlife rescue center",
        "Arcade museum",
        "Outdoor laser tag arena",
        "Electric bike rental",
        "Wine tasting room",
        "Miniature golf course",
        "Slackline park",
        "Eclectic music venue",
        "Butterfly release garden",
        "Helicopter tours",
        "Archery tag arena",
        "Community theater",
        "Psychic healing sessions",
        "Skywalk observation deck",
        "Edible garden",
        "Kayak rental",
        "Virtual reality roller coaster",
        "Alpaca farm",
        "Graffiti art wall",
        "Aromatherapy spa",
        "Insect zoo",
        "Telescope observatory",
        "Segway obstacle course",
        "Kite flying field",
        "Scuba diving pool",
        "Aquaponics farm",
        "Holographic art gallery",
        "Psychic pet communicator",
        "Indoor surfing simulator",
        "Rooftop garden",
        "Aerial tramway",
        "Recycled art exhibit",
        "Cider tasting room",
        "Unicycle rental",
        "Exotic fruit orchard",
        "Potbelly pig petting area",
        "Truffle hunting experience",
        "Gondola rides",
        "Virtual reality painting studio",
        "Indoor go-kart track",
        "Bonsai garden",
        "Wine and paint studio",
        "Street magic performances",
        "Bat house",
        "Kombucha bar",
        "Interactive light installation",
        "Sandcastle building workshop",
        "Coworking space with a slide",
        "Virtual reality dance club",
        "Urban beekeeping station",
        "Psychic fitness classes",
        "Slackline forest trail",
        "Bubble tea lab",
        "Aquatic acrobatics show",
        "Forest bathing trail",
        "Rodeo arena",
        "Hot air balloon glow festival",
        "3D printing studio",
        "Floating market",
        "Tarot-themed escape room",
        "Electric skateboard rental",
        "Glow-in-the-dark mini golf",
        "Robot petting zoo",
        "Mermaid swimming lessons",
        "Pop-up roller disco",
        "Psychic comedy club",
        "Cactus garden",
        "Virtual reality cooking classes",
        "Drone racing track",
        "Outdoor astronomy lessons",
        "Hiking trail with hidden sculptures",
        "Moonlight kayaking tours",
        "Food foraging workshops",
        "Electric scooter obstacle course",
        "Indoor kite flying arena",
        "Mobile pet adoption center",
        "Psychic improv theater",
        "Glassblowing demonstration",
        "Unusual plant nursery",
        "Virtual reality wine tasting",
        "Ice sculpture exhibit",
        "Psychic speed dating events",
        "Interactive sound garden",
        "Geodesic dome greenhouse",
        "Juggling workshop",
        "Floating obstacle course",
        "Psychic trivia night",
        "Aquatic puppet show",
        "Solar-powered phone charging station",
        "Virtual reality fashion show",
        "Bioluminescent kayak tours",
        "Archery biathlon",
        "Drone light show",
        "Indoor kiteboarding facility",
        "Psychic escape room",
        "Virtual reality escape safari",
        "Fire spinning performances",
        "Trampoline dodgeball arena",
        "Aquatic robot racing",
        "Psychic drum circle",
        "Recycled fashion runway",
        "Virtual reality language immersion",
        "Underwater sculpture garden",
        "Firefly watching tours",
        "Psychic board game night",
        "Holographic petting zoo",
        "Electric unicycle rental",
        "Recycled material art workshops",
        "Bubble soccer field",
        "Virtual reality gardening class",
        "Glow-in-the-dark paintball",
        "Biodegradable art installations",
        "Psychic movie night",
        "Aromatherapy painting class",
        "Drone yoga classes",
        "Virtual reality wildlife safari",
        "Recycled paper-making workshop",
        "Fire dancer workshop",
        "Psychic karaoke night",
        "Electric scooter racing track",
        "Virtual reality ice sculpting",
        "Drone painting performance",
        "Psychic stand-up comedy",
        "Aquatic acrobatics workshop",
        "Virtual reality wildlife photography",
        "Recycled sculpture park",
        "Psychic improv dance party",
        "Electric skateboard parkour",
        "Virtual reality glassblowing",
        "Bioluminescent art installations",
        "Holographic pottery class",
        "Psychic improv music jam",
        "Recycled fashion design classes",
        "Virtual reality circus workshop"
    ]

    # Ensure the number of requested amenities is not greater than the total number of amenities available
    num_amenities = min(num_amenities, len(amenities_list))

    # Randomly select amenities
    random_amenities = random.sample(amenities_list, num_amenities)

    # Convert the list to a string
    amenities_string = ", ".join(random_amenities)

    return amenities_string




