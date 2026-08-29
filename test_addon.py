#!/usr/bin/env python3
import json
import os
import sys
import struct

def test_json_files():
    print("Testing JSON syntax in all project directories...")
    json_count = 0
    for root, dirs, files in os.walk("."):
        if ".git" in root or "node_modules" in root:
            continue
        for file in files:
            if file.endswith(".json"):
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8") as f:
                    try:
                        json.load(f)
                        json_count += 1
                    except Exception as e:
                        print(f"Error parsing JSON in {filepath}: {e}")
                        sys.exit(1)
    print(f"PASS: Validated {json_count} JSON files.")

def test_manifests():
    print("Testing Manifest format and UUID links...")
    with open("behavior_pack/manifest.json") as f:
        bp_manifest = json.load(f)
    with open("resource_pack/manifest.json") as f:
        rp_manifest = json.load(f)

    bp_uuid = bp_manifest["header"]["uuid"]
    rp_uuid = rp_manifest["header"]["uuid"]

    # Check RP is referenced in BP dependencies
    bp_deps = [dep.get("uuid") for dep in bp_manifest.get("dependencies", []) if "uuid" in dep]
    assert rp_uuid in bp_deps, f"Resource Pack UUID {rp_uuid} not found in BP dependencies: {bp_deps}"
    print("PASS: BP and RP manifest dependencies match.")

def test_spawn_rules():
    print("Testing spawn rules light brightness filter...")
    spawn_rules_dir = "behavior_pack/spawn_rules"
    rules = os.listdir(spawn_rules_dir)
    assert len(rules) >= 1, "No spawn rules found!"

    for rule_file in rules:
        if not rule_file.endswith(".json"):
            continue
        with open(os.path.join(spawn_rules_dir, rule_file)) as f:
            data = json.load(f)
        conditions = data["minecraft:entity"]["conditions"]
        for cond in conditions:
            bf = cond.get("minecraft:brightness_filter", {})
            assert bf.get("min") == 15 and bf.get("max") == 15, \
                f"Spawn rule {rule_file} min/max light level is not 15! Found: {bf}"
    print(f"PASS: All {len(rules)} spawn rules enforce min=15, max=15 light levels.")

def test_png_files():
    print("Testing PNG header integrity...")
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".png"):
                filepath = os.path.join(root, file)
                with open(filepath, "rb") as f:
                    header = f.read(8)
                    assert header == b"\x89PNG\r\n\x1a\n", f"Invalid PNG header in {filepath}"
    print("PASS: All PNG files have valid headers.")

if __name__ == "__main__":
    test_json_files()
    test_manifests()
    test_spawn_rules()
    test_png_files()
    print("ALL TESTS PASSED SUCCESSFULLY!")
