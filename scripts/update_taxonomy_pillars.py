import json
import os


def update_taxonomy():
    overlay_path = "metadata/MSC_index_pillars_overlay.json"
    taxonomy_path = "metadata/msc_taxonomy.all.json"

    if not os.path.exists(overlay_path) or not os.path.exists(taxonomy_path):
        print("Error: Files not found.")
        return

    # Load overlay
    with open(overlay_path, "r", encoding="utf-8") as f:
        overlay_data = json.load(f)

    # Create mapping: msc_code -> (primary, secondary)
    pillar_map = {}
    for section in overlay_data["sections"]:
        pillar_map[section["msc_code"]] = {
            "primary": section.get("primary_pillar"),
            "secondary": section.get("secondary_pillars", []),
        }

    # Load taxonomy
    with open(taxonomy_path, "r", encoding="utf-8") as f:
        taxonomy_data = json.load(f)

    # Update taxonomy
    updated_count = 0
    for entry in taxonomy_data:
        section_code = entry.get("hierarchy", {}).get("section")
        if section_code in pillar_map:
            mapping = pillar_map[section_code]
            # Replace 'pillar' field with 'primary_pillar' or just update it
            # To be consistent with the overlay, we'll use primary_pillar and secondary_pillars
            entry["primary_pillar"] = mapping["primary"]
            entry["secondary_pillars"] = mapping["secondary"]
            # Optionally remove or update the old 'pillar' field
            if "pillar" in entry:
                entry["pillar"] = mapping["primary"]
            updated_count += 1

    # Save updated taxonomy
    with open(taxonomy_path, "w", encoding="utf-8") as f:
        json.dump(taxonomy_data, f, indent=2, ensure_ascii=False)

    print(f"Successfully updated {updated_count} entries in {taxonomy_path}")


if __name__ == "__main__":
    update_taxonomy()
