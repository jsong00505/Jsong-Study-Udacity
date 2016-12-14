# A Maze
Completion: 16/16
## Main Functionality
- [x] The student assembles a Maze scene using Unity primitives. - Starting with the project starter kit, the student has created a maze scene using Unity primitives.
- [x] The student populates their maze environment with waypoints, collectables, the key, a gate, and a completion UI. - The maze environment contains collectables, waypoints, a key, a gate, and the completion UI.

## Waypoint Functionality
- [x] The student uses provided waypoints and arranges them in the scene such that it can be traveled from the start to the key, the key to the door and final UI. - The maze may be traversed using the waypoints from start to finish.

## Gate Functionality
- [x] A gate prefab blocks the user's path. - The maze cannot be completed without opening the gate.
- [x] The gate is locked, and will not open until the key is collected. - The gate will not open when interacted with until the key is collected. Once collected the gate opens and animates.
- [x] Once the key is found, the gate opens.
- [x] A sound effect is played when the gate opens. - A sound effect plays when the gate is unlocked with the key and opened.

## Key Functionality
- [x] The key exists in the scene away from the gate. - The student positions the key in the scene, separate from the door.
- [x] The key can be collected by looking at it and clicking it. - The student creates a means for the key to be collected and stores the status of whether the user has the key or not.
- [x] The key has sound effects when it is collected. - The student plays a sound via script when the key is clicked.
- [x] This gate can be interacted with, selected, and clicked. - The gate will not open when interacted with until the key is collected. Once collected the gate opens and animates.
- [x] Each of these demonstrates a visual response.

## Collectable Functionality
- [x] Collectables exist scattered throughout the scene. - The student positions collectables in the scene.
- [x] Collectables are gathered when in clicked - The student creates a means for these items to be collected via clicking
- [x] Sound effect. - The student triggers a sound effect via script when the item is collected.

## Completion Functionality
- [x] The scene is reloaded when the UI is clicked. - The student allows the scene to be reset to its initial state such that it can be run again by scripting this functionality into the UI.
