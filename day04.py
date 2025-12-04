with open("input-04.txt") as f:
    rows = f.readlines()

rows = [row.strip() for row in rows]

accessible_count = 0
for y, row in enumerate(rows):
    for x, entry in enumerate(row):
        if entry == "@":
            roll_count = 0
            for x_check in range(max(x-1, 0), min(x+2, len(row))):
                for y_check in range(max(y-1, 0), min(y+2, len(rows))):
                    if rows[y_check][x_check] == "@":
                        roll_count += 1
            if roll_count < 5:
                accessible_count += 1
print(accessible_count)
#---------
def remove_accessible(rows):
    accessible_count = 0
    new_rows = []
    for y, row in enumerate(rows):
        new_row = []
        for x, entry in enumerate(row):
            if entry == "@":
                roll_count = 0
                for x_check in range(max(x-1, 0), min(x+2, len(row))):
                    for y_check in range(max(y-1, 0), min(y+2, len(rows))):
                        if rows[y_check][x_check] == "@":
                            roll_count += 1
                if roll_count < 5:
                    accessible_count += 1
                    new_row.append(".")
                else:
                    new_row.append("@")
            else:
                new_row.append(".")
        new_rows.append(new_row)
    return new_rows, accessible_count

removed = -1
removed_total = 0
while removed != 0:
    rows, removed = remove_accessible(rows)
    removed_total += removed

print(removed_total)
