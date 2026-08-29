# Reverse Mob Spawning Add-on

A Minecraft Bedrock Edition add-on that completely reverses hostile mob spawning mechanics!

## 🌟 Features

- **Reverse Natural Spawning**: Hostile mobs (Creepers, Zombies, Skeletons, Spiders, Cave Spiders, Witches, Endermen, Drowned, Husks, Strays, Phantoms, Slimes) **no longer spawn in darkness**. Instead, they spawn exclusively in maximum light levels (**Light Level 15**)!
- **Jumpscare Light Source Placement**: Placing light sources (Torches, Soul Torches, Glowstone, Lanterns, Sea Lanterns, Campfires, End Rods, etc.) immediately spawns a Creeper right where you placed the light!
- **Glowing & Bright Textures**: Custom bright solar-infused creeper textures with glowing eyes and fiery mouth.
- **Works In-Game**: Fully compatible with Minecraft Bedrock Edition 1.20+.

## 📦 File Structures

- `behavior_pack/`: Contains entity spawn rules for light level 15 natural spawning and `@minecraft/server` scripts for block placement events.
- `resource_pack/`: Contains entity definitions, custom textures, and pack icons.
- `Reverse_Mob_Spawning.mcaddon`: Combined installer package for Bedrock.
- `Reverse_Mob_Spawning_BP.mcpack`: Behavior Pack package.
- `Reverse_Mob_Spawning_RP.mcpack`: Resource Pack package.

## 🚀 How to Install

1. Double-click or open `Reverse_Mob_Spawning.mcaddon` with Minecraft Bedrock Edition.
2. In world settings:
   - Enable **Reverse Mob Spawning BP** under Behavior Packs.
   - Enable **Reverse Mob Spawning RP** under Resource Packs.
   - Ensure **Beta APIs** (or Experiments if using scripts) are toggled ON in world settings.
3. Enjoy your brightly lit, Creeper-infested home!

## 🛠️ Development & Building

To validate and rebuild the add-on packages:
```bash
python3 test_addon.py
python3 build.py
```
