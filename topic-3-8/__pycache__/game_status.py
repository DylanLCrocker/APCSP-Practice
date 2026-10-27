"""Game Status: refactor render_status without changing its behavior."""

def bind_type(type, max) :
    shown_type = type
    if shown_type < 0 :           
        shown_type = 0
    elif shown_type > max :
         shown_type = max
    return shown_type

def create_bar(type, shown_type, max) :
    type_filled = shown_type * 10 // max
    type_bar = "["
    for position in range(10):
        if position < type_filled:
            type_bar = type_bar + "#"
        else:
            type_bar = type_bar + "-"
    type_bar = type_bar + "]"
    return type_bar

def format_duration(total_seconds) :

    total_minutes = total_seconds // 60
    total_remainder = total_seconds % 60
    total_text = str(total_minutes) + ":"
    if total_remainder < 10:
        total_text = total_text + "0"
    total_text = total_text + str(total_remainder)

    return total_text

def render_status(name, health, energy, elapsed_seconds, best_seconds, scores):
    # Keep this function's name, parameters, and returned report.
    # Add your own helper functions above it.

    # Bound the two meters.
    
    shown_health = bind_type(health, 100)
    shown_energy = bind_type(energy, 60)

    # Build two bars. // keeps the whole-number part of the division.

    health_bar = create_bar(health, shown_health, 100)
    energy_bar = create_bar(energy,shown_energy, 60)

    # Format two durations.

    elapsed_text = format_duration(elapsed_seconds)
    best_text = format_duration(best_seconds)

    # Summarize the recent scores.
    total = 0
    highest = scores[0]
    strong_count = 0
    
    for score in scores:
        total = total + score
        if score > highest:
            highest = score
        if score >= 80:
            strong_count = strong_count + 1

    # Choose a level from the total.
    if total < 100:
        level = "Rookie"
    elif total < 250:
        level = "Skilled"
    else:
        level = "Expert"

    # Return one report. \n separates its lines; there is no final \n.
    report = "PLAYER: " + name
    report = report + "\nHealth  " + health_bar + " " + str(shown_health) + "/100"
    report = report + "\nEnergy  " + energy_bar + " " + str(shown_energy) + "/60"
    report = report + "\nLevel:  " + level
    report = report + "\nTime:   " + elapsed_text
    report = report + "\nBest:   " + best_text
    report = report + "\nRecent: total=" + str(total)
    report = report + ", best=" + str(highest) + ", 80+=" + str(strong_count)
    return report


# Supplied demo. This guard keeps the demo from running when tests import the file.
if __name__ == "__main__":
    print(render_status("Nova", 75, 18, 125, 119, [40, 50, 90]))
    print()
    print(render_status("Orion", 110, -4, 61, 60, [80, 80, 90]))
