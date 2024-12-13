import json
import csv
import os
from prettytable import PrettyTable


def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def clean_domain_for_filename(domain):
    return domain.replace("http://", "").replace("https://", "")


def save_json_report(domain, analysis_result, folder):
    cleaned_domain = clean_domain_for_filename(domain)
    filepath = os.path.join(folder, f"{cleaned_domain}.json")
    with open(filepath, "w") as file:
        json.dump(analysis_result, file, indent=4)
    return filepath


def save_csv_report(domain, analysis_result, folder):
    cleaned_domain = clean_domain_for_filename(domain)
    filepath = os.path.join(folder, f"{cleaned_domain}.csv")
    with open(filepath, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Header", "Status", "Details"])
        for header in analysis_result["headers"]:
            writer.writerow([header["header"], header["status"], header["details"]])
    return filepath


def wrap_text(text, width=50):
    lines = []
    while len(text) > width:
        space_index = text.rfind(" ", 0, width)
        if space_index == -1:
            lines.append(text[:width])
            text = text[width:]
        else:
            lines.append(text[:space_index])
            text = text[space_index + 1:]
    lines.append(text)
    return "\n".join(lines)


def save_table_report(domain, analysis_result, folder):
    cleaned_domain = clean_domain_for_filename(domain)
    filepath = os.path.join(folder, f"{cleaned_domain}.txt")
    
    table = PrettyTable()
    table.field_names = ["Header", "Status", "Details"]
    table.max_width = 50

    for header in analysis_result["headers"]:
        details = header["details"]
        if isinstance(details, dict):
            details = str(details)

        wrapped_details = wrap_text(details, width=50)

        table.add_row([header["header"], header["status"], wrapped_details])

    with open(filepath, "w") as file:
        file.write(str(table))
    return filepath


def save_report(domain, analysis_result):
    folder = os.path.join("reports", clean_domain_for_filename(domain))
    ensure_directory_exists(folder)

    json_path = save_json_report(domain, analysis_result, folder)
    csv_path = save_csv_report(domain, analysis_result, folder)
    table_path = save_table_report(domain, analysis_result, folder)

    return {"json": json_path, "csv": csv_path, "table": table_path}