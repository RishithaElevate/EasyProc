def analyze_logs():
    with open("violations.csv", "r") as f:
        lines = f.readlines()
    return f"Total violations: {len(lines)}\n\n" + "".join(lines)
