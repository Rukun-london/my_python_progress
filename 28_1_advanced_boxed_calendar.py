import calendar

def build_boxed_month(year: int, month: int) -> str:
    """
    Return a string representing the given month in a boxed ASCII calendar.
    Week starts on Monday by default.
    """
    # Ensure weeks start on Monday (0 = Monday)
    calendar.setfirstweekday(calendar.MONDAY)

    # Get matrix of weeks: each week is [Mon, Tue, Wed, Thu, Fri, Sat, Sun]
    weeks = calendar.monthcalendar(year, month)

    # Box-drawing characters
    h = "─"
    v = "│"
    tl = "┌"
    tr = "┐"
    bl = "└"
    br = "┘"
    tj = "┬"
    bj = "┴"
    lj = "├"
    rj = "┤"
    cj = "┼"

    # Column width for each day cell (including padding)
    cell_width = 4  # e.g. "  1 " (2 digits + 2 spaces)

    # Helper to build a horizontal border line
    def build_border(left: str, mid: str, junction: str, right: str) -> str:
        parts = [left]
        for i in range(7):
            parts.append(h * cell_width)
            parts.append(junction if i < 6 else right)
        return "".join(parts)

    # Top, middle, and bottom borders
    top_border = build_border(tl, h, tj, tr)
    mid_border = build_border(lj, h, cj, rj)
    bottom_border = build_border(bl, h, bj, br)

    # Weekday header labels
    headers = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    # Build header row
    header_cells = []
    for name in headers:
        # Center the 3-letter name in the cell width
        header_cells.append(f"{name:^{cell_width}}")

    header_row = v + v.join(header_cells) + v

    # Build each week row
    week_rows = []
    for week in weeks:
        cells = []
        for day in week:
            if day == 0:
                # Empty cell for days outside the month
                cells.append(" " * cell_width)
            else:
                # Right-align the day number within the cell
                cells.append(f"{day:>{cell_width - 1}} ")
        week_rows.append(v + v.join(cells) + v)

    # Assemble full calendar
    lines = []
    # Title line (month name + year)
    month_name = calendar.month_name[month]
    title = f"{month_name} {year}"
    # Width of the inside area (7 cells + 6 verticals)
    inner_width = 7 * cell_width + 6
    lines.append(title.center(inner_width + 2))  # +2 for side borders

    lines.append(top_border)
    lines.append(header_row)
    lines.append(mid_border)

    for i, row in enumerate(week_rows):
        lines.append(row)
        if i < len(week_rows) - 1:
            lines.append(mid_border)
    lines.append(bottom_border)

    return "\n".join(lines)


if __name__ == "__main__":
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))

    print()
    print(build_boxed_month(year, month))
