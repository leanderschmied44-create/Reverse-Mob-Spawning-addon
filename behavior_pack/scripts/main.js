import { world, system } from "@minecraft/server";

// Light-emitting block identifiers
const LIGHT_SOURCES = new Set([
  "minecraft:torch",
  "minecraft:soul_torch",
  "minecraft:redstone_torch",
  "minecraft:glowstone",
  "minecraft:lantern",
  "minecraft:soul_lantern",
  "minecraft:sea_lantern",
  "minecraft:shroomlight",
  "minecraft:jack_o_lantern",
  "minecraft:froglight",
  "minecraft:pearlescent_froglight",
  "minecraft:verdant_froglight",
  "minecraft:ochre_froglight",
  "minecraft:crying_obsidian",
  "minecraft:beacon",
  "minecraft:end_rod",
  "minecraft:campfire",
  "minecraft:soul_campfire",
  "minecraft:light_block",
  "minecraft:candle",
  "minecraft:white_candle",
  "minecraft:orange_candle",
  "minecraft:magenta_candle",
  "minecraft:light_blue_candle",
  "minecraft:yellow_candle",
  "minecraft:lime_candle",
  "minecraft:pink_candle",
  "minecraft:gray_candle",
  "minecraft:light_gray_candle",
  "minecraft:cyan_candle",
  "minecraft:purple_candle",
  "minecraft:blue_candle",
  "minecraft:brown_candle",
  "minecraft:green_candle",
  "minecraft:red_candle",
  "minecraft:black_candle"
]);

// Helper to spawn a creeper right at the specified location
function spawnCreeperAt(dimension, location, sourceName) {
  try {
    const spawnLoc = {
      x: location.x + 0.5,
      y: location.y,
      z: location.z + 0.5
    };
    dimension.spawnEntity("minecraft:creeper", spawnLoc);

    // Broadcast message
    world.sendMessage(`§c[Reverse Spawning] A light source (${sourceName.replace("minecraft:", "")}) spawned a Creeper!`);
  } catch (error) {
    console.error("Failed to spawn creeper on light placement:", error);
  }
}

// Listen for block placement events
world.afterEvents.playerPlaceBlock.subscribe((event) => {
  const { block, player } = event;
  const blockTypeId = block.typeId;

  if (
    LIGHT_SOURCES.has(blockTypeId) ||
    blockTypeId.includes("torch") ||
    blockTypeId.includes("lantern") ||
    blockTypeId.includes("glowstone")
  ) {
    spawnCreeperAt(block.dimension, block.location, blockTypeId);
  }
});

// Periodic check / ambient daylight check for players outdoors in daylight or bright areas
system.runInterval(() => {
  for (const player of world.getAllPlayers()) {
    try {
      const dim = player.dimension;
      const timeOfDay = world.getTimeOfDay(); // 0 to 24000

      // Daylight in Minecraft is roughly between 0 and 12000 ticks
      const isDaytime = timeOfDay >= 0 && timeOfDay <= 12000;

      if (isDaytime && Math.random() < 0.05) {
        // Outdoors check: check if sky above player is clear to the top
        const playerLoc = player.location;
        const headLoc = {
          x: Math.floor(playerLoc.x),
          y: Math.floor(playerLoc.y + 1),
          z: Math.floor(playerLoc.z)
        };

        const topBlock = dim.getTopmostBlock(headLoc);
        if (topBlock && topBlock.location.y <= headLoc.y + 1) {
          // Player is directly under open daylight (Light Level 15)
          const spawnLoc = {
            x: headLoc.x + (Math.floor(Math.random() * 7) - 3) + 0.5,
            y: headLoc.y,
            z: headLoc.z + (Math.floor(Math.random() * 7) - 3) + 0.5
          };

          const mobs = ["minecraft:creeper", "minecraft:zombie", "minecraft:skeleton", "minecraft:spider"];
          const selectedMob = mobs[Math.floor(Math.random() * mobs.length)];
          dim.spawnEntity(selectedMob, spawnLoc);
        }
      }
    } catch (e) {
      // Ignore location out of bounds / unloaded chunks
    }
  }
}, 100);

console.warn("[Reverse Mob Spawning] Behavior pack script initialized successfully!");
