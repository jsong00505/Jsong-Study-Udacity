# Programming Animations
[<- Previous](README-3-3.md) ..... [Next ->](README-3-5.md)
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
1. Select `GoogleVR->Scripts->GvrViewer`
2. Just look around the script
3. Go bact to `RotateLight`
4. Type `public void ActivateRotation() {}`
5. Type `GvrViewer.Instance.OnTrigger += ActivateRotation;` in `Start()` method
6. Define two variables `float startTime=0f` and `bool isPressed=false;`
7. Type `isPressed=true;` into `ActivateRotation`
8. Type `if(isPressed == true) {}` after `Quaternion endRotation = ...` in `Update()` method
9. Put `directionalList.transform...` inside the if statement
10. Change `Time.time` to `startTime / 10f`
11. Last thing make sure to update `startTime += Time.deltaTime`
12. Press 'Play'

## 3. What are Variables
 Variables are `float`, `bool` or `string`

## 4. Scripting with Unity's Animator
1. Apply the animator to our Sun and go back to the script editor
2. Define a variable `public Animator sunRotationAnimation;`
3. Type `sunRotationAnimation.StopPlayback;` inside if statement and comment `directionalLight...` out
4. Type `sunRotationAnimation.StartPlayback;` after `GvrViewer` into `Start()` method
5. Type `sunRotationAnimation.SetBool("ChangeColor", true);` in `ActiveRotation()` method
6. Go back to Unity and click on the `Sun` and apply the animator component
7. Press 'Play' and see to turn the color red


[<- Previous](README-3-3.md) ..... [Next ->](README-3-5.md)
