# Programming Animations
[<- Previous](README-3-4.md) ..... [Next ->](README-3-5.md)
## 1. Scripting A Simple Rotation

### Practice1
**GOAL**: Rotate the Sun in my scene
1. Open up the `ProgrammingAnimations`
2. Play around with Sun Rotation
3. Create new script file called `RotateLight`
4. Open it up
5. Type ` public GameObject directionalLight;` to add `GameObject`
6. Check the documentation of `Transform.Rotate`
7. In update(), type `directionalLight.transform.Rotate(0, Time.deltaTime, 0);`
8. Go back to Unity
9. Assign the script to the Sun
10. Hit `Play` and see the directionalLight changing

#### 1) [LERP](https://docs.unity3d.com/ScriptReference/Vector3.Lerp.html)
* Linearly interpolates between two vectors

#### 2) [SLERP](https://docs.unity3d.com/ScriptReference/Quaternion.Slerp.html)
* Spherically interpolates between two vectors

## 2. Scripting SLERP

### Practice2
1. Hop back into `RotateLight` script
2. Use `SLERP` and `Quaternion`
3. Type `Quaternion startRotation = Quaternion.Euler(50f, 30f, 0f);`
4. Type `Quaternion endRoatation = startRotation * Quaternion.Euler(0, 180f, 0f);`
5. Type `directionalLight.transform.rotation = Quaternion.Slerp(startRotation, endRoatation, Time.time);`
6. Go back and hit `Play`
7. If you feel the rotation is too fast, just edit `Time.time` by multiplying or dividing

## 3. C# Event

[<- Previous](README-3-4.md) ..... [Next ->](README-3-5.md)
