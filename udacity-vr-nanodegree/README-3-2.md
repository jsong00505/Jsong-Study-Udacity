# CONTROLLING OBJECTS USING CODE
[<- Previous](README-3-1.md) ..... [Next ->](README-3-3.md)
## 1. Documentation

### Unity Documentation
You can find the Unity docs [here](https://docs.unity3d.com/Manual/index.html)
#### 1) Manual
- Design and components

#### 2) Scripting API
* Programming
* Divided into **namespaces**
* Namespaces establish a groupings between related objects
* UnityEngine: all about stuff that happens when VR app is running
* UnityEditor: all about extending the unity editor

#### 3) UnityEngine
* Almost all scripts start with **using UnityEngine;**
* This gives you access to all the objects in the UnityEngine namespace

## 2. Creating Objects using Code
* This is called **Instantiating**.
* You are creating a new instance of something.

### Practice1
1. Create a new script called `ObjectMaker`
2. Open the script
3. Put some code in `Start()` method
4. **References**
5. Type `public GameObject objectToCreate;`
6. Save and go back to Unity
7. Create an empty GameObject called `MyObjectMaker`
8. Drag-and-drop `ObjectMaker` script onto `MyObjectMaker`
9. Notice the little field called `Object To Create` in `ObjectMaker`
10. Create new cube called `MyCube`
11. Drag-and-drop that cube into the object to create field

#### References
* Allow me to pass objects and components into a script and control them
* Allow me to drag-and-drop objects into code using the Unity Editor
* Easy and fast

#### Break down the code1
```C#
public GameObject objectToCreate;
```
* `public`
* `GameObject`: data type
* `objectToCreate`: name of reference using Camel case
* `;` (semicolon): Tells unity that I am done

### Practice2
1. Use the script I wrote in Practice1
2. Go to `Start()` method
3. Type `Object.Instantiate(objectToCreate, new Vector3(2,4,6), Quaternion.identity);`
4. Save and go back to Unity
5. Press "Play"
6. See that a new cube appeared with a position of (2, 4, 6)
7. The code is creating a copy whatever object I dragged into the object create slot and placing that copy at position (2, 4, 6)

#### Break down the code1
```C#
Object.Instantiate(objectToCreate, new Vector3(2,4,6), Quaternion.identity);
```
* `Object.Instantiate`: Call Instantiate method on the object class. Clones an object
* `objectToCreate`: The name of the reference I created
* `new Vector3(2,4,6)`: How I code positions in 3D space. Place the new object position (2, 4, 6)
* `Quaternion.identity`: Tell Unity how to rotate the new object. No rotation at all

#### 1) new Vector3(2,4,6)
* This is how you specify positions in 3D space
* Creates a new Vector3 object
* First number is the **x coordinate**
* Second number is the **y coordinate**
* Third number is the **z coordinate**

#### 2) Quaternions
* How Unity handles 3D rotations
* Better for simulations than Euler angles
* Unity handles all the complicated math for me

## 3. For Loops

### Practice3
1. Create new script called `MiniObjectMaker`
2. Add 2 lines of code to create an object using a reference
3. Write some code to create a long line of 1000 cubes.
4. Coment out the line that starts with `Object.Instantiate`
5. Type `for(int i = 0; i < 1000; i++) {}`
6. Add some new code. `Object.Instantiate(objectToCreate, new Vector3(i,4,6), Quaternion.identity)`
7. Go back to Unity
8. Create new object called `MyMiniObjectMaker`
9. Drag-and-drop the script to it
10. Press "Play"
11. See that new 1000 cubes

#### 1) Comments
* Great wayto write programming notes to yourself and others.
* Also useful for saving code for later reference


#### 2) For Loops
```C#
for(int i = 0; i < 1000; i++) {
  // do stuff
}
// finished
```
* `int i`: Creates a variable called `i`, and it sets its value to 0
* `i < 1000`: Checks to see if `i` is less than 1000
* `// do stuff`:
* `i++`: When Unity hits the closing brace, it jumps back to the top, and adds 1 to `i`
* Runs until i is equal to 1000, and Unity exits the loop.

## 4. Prefabs
* Allo you to store a **GameObject**, all of its components, and settings in a file on your hard disk.
* Think of prefabs as a "plan" that Unity follows to create certain GameObjects.

### Practice4
1. Take `MyCube` object, and scale it vertically a little bit
2. Drag-and-drop `MyCube` into the project pane
3. Just created a prefab, and notice it has a little blue icon. That's what prefabs look like inside of Unity
4. Save the scene and create new one.
5. Drag-and-drop the prefab into the new scene
6. Go back to the previous scene and use a prefab
7. Locate the GameObject that has the `MyMiniObjectMaker` script attached
8. Drag-and-drop the prefab into that slot
9. Press "Play"

**Most assets I get from the Unity asset store will be prefabs**

### Practice5
1. [Download](https://d17h27t6h515a5.cloudfront.net/topher/2016/November/5818d15d_vrnd-course3-course-assets-001/vrnd-course3-course-assets-001.zip) this asset first
2. Install
3. Search for a prefab called `seagull`
4. Drag-and-drop it into the object to create slot
5. Press "Play"
6. Created 1000 seagulls

### Practice6

1. Go back to the script, the `MiniObjectMaker`
2. change 1000 to 50
3. Coment out the line that starts with `Object.Instantiate`
4. Add the code below `Break down the code2`
5. Save and then turn back to Unity
6. Run
7. See everyone of those seagulls have a slightly different color of grey

#### Break down the code2
```C#
GameObject newSeagull = (GameObject)Object.Instantiate(objectToCreate, new Vector3(i, 0, 0), Quaternion.identity);
Renderer objectRenderer = newSeagull.GetComponentInChildren<Renderer>();
objectRenderer.material.color = Color.white * Random.value;
```

> GameObject newSeagull = (GameObject)Object.Instantiate(objectToCreate, new Vector3(i, 0, 0), Quaternion.identity);

This is the same as before, but storing the seagull we created into a variable

> Renderer objectRenderer = newSeagull.GetComponentInChildren<Renderer>();
>objectRenderer.material.color = Color.white * Random.value;

Talking to the new seagull that we created and finding out a way to change its color and the way I do that is through `Renderer` inside of Unity

### Practice7
1. Go back to Unity, and find seagull
2. Drag-and-drop into the scene
3. Roll down the seagull and look at how it's made
4. See eventually there's a `Skinned Mesh Renderer` which one type of renderer


#### How code works
1. Find the first renderer inside of seagull which happened to be `Skinned Mesh Renderer`
2. Find the material associated that renderer
3. Change the color

[<- Previous](README-3-1.md) ..... [Next ->](README-3-3.md)
