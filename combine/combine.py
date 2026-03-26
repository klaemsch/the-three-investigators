import os
import csv

def combine_rows(row1, row2):
    # "Speaker","Text","Page","speaker_id","Episode"
    if (
        row1[0] == row2[0]  # speaker equal
        and row1[2] == row2[2]  # page equal
        and row1[3] == row2[3]  # speaker_id equal
        and row1[4] == row2[4]  # episode equal
    ):
        return [
            row1[0],
            row1[1].rstrip() + ' ' + row2[1].lstrip(),
            row1[2],
            row1[3],
            row1[4]
        ]
    else:
        return []

def get_episode_rows(filepath: os.PathLike, episode: int):
    saved_rows = []
    with open(filepath, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for idx, row in enumerate(reader):
            row.append(episode)  # add episode to row
            if idx == 0:
                continue  # skip header and already saved rows
            elif len(saved_rows) == 0:
                # there is no row we can compare to
                saved_rows.append(row)
            else:
                current_row = row
                previous_row = saved_rows[-1]

                combined_row = combine_rows(previous_row, current_row)
                if len(combined_row) == 0:
                    # case 1: rows cant be combined -> add current row to saved_rows, leave previous untouched
                    saved_rows.append(current_row)
                else:
                    # case 2: rows can be combined -> replace previous row, with the combined entry
                    saved_rows[-1] = combined_row

    return saved_rows


def write_combined_csv(data):
    with open("combine.csv", "w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh, quoting=csv.QUOTE_ALL)
        writer.writerow(["Speaker", "Text", "Page", "speaker_id", "Episode"])
        writer.writerows(data)


CSV_DIR = "../csv"
rows = []

for filename in os.listdir(CSV_DIR):
    print(filename)
    if filename.endswith(".csv"):
        episode = int(filename.removesuffix(".csv"))
        print(episode)
        filepath = os.path.join(CSV_DIR, filename)
        rows = rows + get_episode_rows(filepath, episode)
        print(len(rows))

write_combined_csv(rows)
