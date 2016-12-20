# Physics & Audio
[<- Previous](README-3-4.md) ..... [Next ->](README-3-6.md)
## 1. Unity Physics

For anythin of Physics engine, we need to assign a `Collider` component whatever `GameObject`

4 Main types
* Box Collider
* Capsule Collider
* Mesh Collider
* Sphere Collider

If you make `GameObject` -> `3D Object` -> `Cube`, `Sphere` or `Capsule`, those will already have the corresponding `Collider`

We've appropriately defined collision area for an object, and then we need to assign a `Rigidbody` component to it.

`Rigidbody` is a component to enable a `GameObject` to interface with the Unity physics simulation.

### Practice1
1. Create a really simple scene first
2. Create a `Plane` at the origin
3. Create a `Sphere` called `Ball`
4. Create a `Cube` will act as `Land` for the ball to slide down
5. Set up by positioning and scaling the `Ball` and `Land`
6. Add `Rigidbody` to `Ball`
7. Just hit the 'Play'

## 2. Playing with Rays

### Practice2
1. Open up the `Island` scene
2. `Raycast` casting is for detecting what someone in VR is looking at
3. `Position`, it's located at and the `Direction`, it's traveling in
4. Add a `Collider` to all objects we want to detect in VR
5. Select `Chest` for the practice
6. Create new `C# Script` called `DetectTreasure`
7. Just copy the code [here](https://docs.unity3d.com/ScriptReference/Physics.Raycast.html)
8. Paste it in `DetectTreasure`
9. Add the component in `MainCamera`
10. Press 'Play'
11. See the `TreasureChest`, you can see the message `There is something in front of the object`

## 3. Using Audio in VR

### Practice3
1. Just go to `Audio` folder called `waves.wav`
2. Create `Audio Source` component
3. Drag-and-drop `waves.wav` onto the `AudioClip` in the component we created
4. `Audio Listener` component makes us how far the `Audio` is from the camera

## 4. Creating a List

### Practice4
1. Create new `C# Script` called `AudioPicker`
2. Type `public AudioClip[] soundFiles;`
3. Type `public AudioSource soundSource;`
4. Go back to Unity and select `AudioSource`
5. Choose size of array
6. Set the clips on the `Elements` box
7. Drag-and-drop the `AudioSource` in `Sound Source`

## 5. Picking a Song

### Practice5
1. Jump back to the script
2. Type `int index = Random.Range(0, soundFiles.Length);` in `Start()` method
3. Type `soundSource.clip = soundFiles[index];`
4. Type `soundSource.Play ();` to play the random song

[<- Previous](README-3-4.md) ..... [Next ->](README-3-6.md)
