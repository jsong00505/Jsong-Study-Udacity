# Advanced VR Scripting
[<- Previous](README-3-5.md) ..... [Next ->](README.md)
## 1. Waypoints
** GOAL **
- Add additional Waypoints
- Change the way they look
- Change how quickly we move to a new waypoint when we click it

### Practice1
1. Go to `island` scene
2. Go to `Art` -> `Prefabs` -> `Systems`
3. Drag-and-drop `Waypoints` into the scene
4. Reset the position
5. Move toward to island
6. See 2 scripts called `Waypoint` and `Navigate` on the root node
7. Modify the scripts and let's start with `Waypoint` first
8. Chage `animation_scale` to `3.0f` and see what happens
9. Nothing changed because Unity allows us to change public variables in the inspector and override those values in scripts so need to set them in the inspector itself.
10. See animator a lot of quicker
11. Change `Animation_speed` 2 by adjusting speed
12. See pulsating is bigger and slower
13. Go to `Navigation` script and look around
14. Drag-and-drop `Waypoint` into the scene to add new waypoint
15. Position it and need to set the waypoint neighbors
16. Drag one `Waypoint` property to Element of Neighborhood

## 2. Ocean Shader

### Practice2
1. Modify the way the ocean looks
2. Select `Scene` component and click `Ocean_material` and then you will able to see the materials
3. Go to `Shader` folder and double click `Line` to open
4. Go back to Unity and select `Scene` component
5. Press `Play` and you can see `Ocean` component created in sudden
6. Pause to spend a few minutes playing with shading to get a stormy appearance


## 3. Modifying a Flocking Algorithm

### Practice3
1. Go to `Script` -> `Examples` and create a `GameObject` in the scene
2. Assign the flocking script to the objet
3. Reset
4. Press `Play` and see what it happened
5. Open `ExampleFlocking` script
6. See comments to help to guide us
7. Make a public variable called `flockObject` like this `public GameObject flockObject;`
8. Insted of the line to create primitive, let's delete `GameObject.CreatePrimitive(PrimitiveType.Cube);`
9. Add `Instantiate(flockObject);`
10. Go to `Prefabs` folder and there's a seagull that we can use for flocking script
11. Assign the seagull to flocking script by draging that onto the flock object property
12. You will get an error is telling us that there's no mesh renderer, so we know we should remove all references to mesh renderers in our example flocking script
13. Go back to script and comment the line included `MeshRenderer` inside out

[<- Previous](README-3-4.md) ..... [Next ->](README-3-6.md)
