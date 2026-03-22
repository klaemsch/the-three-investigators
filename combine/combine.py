import os
import csv


def get_episode_rows(filepath: os.PathLike):
    rows = []
    with open(filepath, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for idx, row in enumerate(reader):
            if idx == 0:
                continue  # skip header
            else:
                row.append(episode)
                rows.append(row)
    return rows


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
        rows = rows + get_episode_rows(filepath)
        print(len(rows))

write_combined_csv(rows)
