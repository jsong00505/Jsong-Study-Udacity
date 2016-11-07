# VR Interaction
[<- Previous](README-3-3.md) ..... [Next ->](README-3-4.md)
## Basic UI in Unity

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

[<- Previous](README-3-3.md) ..... [Next ->](README-3-4.md)
