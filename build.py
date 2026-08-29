#!/usr/bin/env python3
import json
import os
import zipfile
import sys

def build_addon():
    print("Building and packaging Reverse Mob Spawning Add-on...")

    # 1. Package Behavior Pack into .mcpack
    bp_filename = "Reverse_Mob_Spawning_BP.mcpack"
    with zipfile.ZipFile(bp_filename, "w", zipfile.ZIP_DEFLATED) as zip_bp:
        for root, dirs, files in os.walk("behavior_pack"):
            for file in files:
                filepath = os.path.join(root, file)
                arcname = os.path.relpath(filepath, "behavior_pack")
                zip_bp.write(filepath, arcname)
    print(f"Created {bp_filename}")

    # 2. Package Resource Pack into .mcpack
    rp_filename = "Reverse_Mob_Spawning_RP.mcpack"
    with zipfile.ZipFile(rp_filename, "w", zipfile.ZIP_DEFLATED) as zip_rp:
        for root, dirs, files in os.walk("resource_pack"):
            for file in files:
                filepath = os.path.join(root, file)
                arcname = os.path.relpath(filepath, "resource_pack")
                zip_rp.write(filepath, arcname)
    print(f"Created {rp_filename}")

    # 3. Package combined .mcaddon
    addon_filename = "Reverse_Mob_Spawning.mcaddon"
    with zipfile.ZipFile(addon_filename, "w", zipfile.ZIP_DEFLATED) as zip_addon:
        for root, dirs, files in os.walk("behavior_pack"):
            for file in files:
                filepath = os.path.join(root, file)
                arcname = os.path.join("behavior_pack", os.path.relpath(filepath, "behavior_pack"))
                zip_addon.write(filepath, arcname)
        for root, dirs, files in os.walk("resource_pack"):
            for file in files:
                filepath = os.path.join(root, file)
                arcname = os.path.join("resource_pack", os.path.relpath(filepath, "resource_pack"))
                zip_addon.write(filepath, arcname)
    print(f"Created {addon_filename}")

if __name__ == "__main__":
    build_addon()
