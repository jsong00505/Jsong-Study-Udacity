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

[<- Previous](README-3-4.md) ..... [Next ->](README-3-6.md)
