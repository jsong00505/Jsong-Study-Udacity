# VR Interaction
[<- Previous](README-3-2.md) ..... [Next ->](README-3-4.md)
## 1. Basic UI in Unity

### Practice1
1. open up the starter project, and if you don't have the project, [download](https://d17h27t6h515a5.cloudfront.net/topher/2016/October/58178819_vrnd-course3-course-assets-000/vrnd-course3-course-assets-000.zip)
2. Open up the `TakeAVacation` scene
3. Search for a model called `VacationBox`
4. Drag-and-drop it into the hierarchy
5. Raise up a little bit, and try to position it on that pedestal
6. Create some instructions
7. Right-click on the hierarchy, and then go to `UI`, and then `Text`
8. **PROBLEMS**: huge, blurry and created GameObject. One is `Canvas`, and other is `Text`
9. Click on the `Text` in the hierarchy
10. Go down, scroll down over on the inspector
11. See under `Paragraph`, and it says `alignment`
12. Click the horizontal center and vertical center alignment button
13. Fix position (0, 0, 0)
14. Change color you like
15. Click on the `Canvas` in the hierarchy, and change the `Render Mode` to `World Space`
16. Scale way down
17. Move to (0, 0, 0)
18. Press `F` key
19. Zoom a little bit, and place the `Text` in front of the `VacationBox`
20. Click the `Canvas` in hierarchy, and then go over to `Dynamic Pixels Per Unit`
21. Change the value higher, and it looks more clear. **CAREFUL: Performance Penalty**
22. **TIP**: Hold `control` or `command`, and rotate the object 15 degrees
23. Drag it down to the ground
24. Make some instructions we want to say
25. `Click here to (Enter) go on vacation`
26. Go to `Vertical Overflow`
27. Switch from `Truncate` to `Overflow`
28. Save the Scene
29. Press "Play"

**RESET: Gear button -> Reset**

#### Canvas
* Unity defaults to rendering the UI Canvas on the entire screen which is called screen space

## 2. Event System and Inputs

### Practice2
1. Create `UI` and `EventSystem`
2. Remove `Standalone Input Module`
3. Go to `Add Component`
4. Search `gaze input module`
5. Press Enter
6. Click `VacationBox`
7. Go to `Add Component`
8. Search for `box collider`
9. Go to `Add Component`
10. Add a component called an `Event Trigger`
11. See a new button appear called `Add New Event Type`, and click on that
12. Select `PointerClick`
13. Click that little plus on the left bottom

## 3. Methods and Debugging

### Practice3
1. Select `VacationBox`, and go to the inspector
2. Go to `Add Component`
3. Type `ChangeScene`, and have only option `New Script`. Click
4. Click `Create and Add`
5. Double click the script and open it up
6. Delete both `Start()` and `Update()` method
7. Type `public void GoToScene() {}`
8. Type `Debug.Log("My method was called!");` inside `GoToScene()` method
9. Go back to Unity
10. Select `VacationBox`
11. Scroll down to the `Event Trigger`
12. Drag `VacationBox` all the way over to that little slot for an object in the `Event Trigger`
13. Click drop-down box that says `No Function`, and then `ChangeScene`, and then `GoToScene ()`
14. Let's test it

## 4. Scene Changing Via Script

### Practice4
1. Go `File` -> `Build Settings`
2. See `Scenes In Build`
3. Drag-and-drop `TakeAVacation` and `FallingCoconut`
4. `TakeAVacation` should be on top, so Unity automatically load the first scene in the `Build Settings`
5. Close the window
6. Go back to the script `ChangeScene` and loaded up
7. Type `SceneManager.LoadScene("name of scene to load");` below the debugging code
8. See the problem because there is no idea what to do with `SceneManager`
9. Add `using UnityEngine.SceneManagement;` on top of the script
10. Go back to Unity and find island scene
11. Click once and select the name of the scene called `FallingCoconut`
12. Press `ctrl-c` to copy the name and then back to the script. Replace the name of `name of scene to load` to `00-FallingCoconut`
13. Also, I could use what's called an index which is the name or the number of the scene
14. Sava and then go back to Unity
15. Press `Play`

## 5. The Power of Variables

### Practice5
1. Go to the script and instead of the name `00-FallingCoconut`
2. Change to variable named `sceneName`
3. Put it as parameter to this method like `public void GoToScene(string sceneName)`
4. Go back to Unity and select `VacationBox`
5. Scroll down and can't find GoToScene method anymore
6. Scroll down and find that method called `ChangeScene.GoToScene(string)`
7. See a `TextBox` and type the name of the scene
8. Copy and Paste like before
9. Press `ctrl-s` to save
10. Try one more time

[<- Previous](README-3-2.md) ..... [Next ->](README-3-4.md)
