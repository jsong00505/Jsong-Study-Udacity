# CREATING SCRIPT
[<- Previous](README.md) ..... [Next ->](README-3-2.md)
## BEHAVIORS

`Example`

A dog object might have:
* "bark" behavior
* "walk around" behavior
* "love humans" behavior

### What I did for the practice

* take a coconut and make it fall
1. Attach a Sphere Collider and a Rigitdbody to the coconut.
2. Create a script called "FallFromTree".
3. Double click and visual studio loaded.
4. Type "transform.Translate(0, -2.5f * Time.deltaTime, 0, Space.World);" inside Update() method.
5. Save and go back to unity.
6. Drag the script I made to Coconut Object
7. Hit "Play" button.
8. See the coconut falls right down through the ground and continues falling forever and ever.

**NEED TO STOP TO COCONUT[SOLVE]**

I just needed to remove Rigidbody and Sphere Collider. That was my problem. Feel good!


### EXPLAIN

#### transform

This is shortcut to access the transform component of whatever game object the script is attached to

#### Translate

This tells unity that we want to **move**(not rotate and not scale) an object in 3D space, and then tell unity that we want to move the object 0 units in the x-axis, -2.5 units in the y-axis and 0 units in the z-axis.

	2.5**f**: That f just tells unity we're typing a number with a decimal point. it is specifying exactly what kind of number we're using.
	2.5f * Time.deltaTime:  Pretty strange. Just for smooths out the animation.
	Space.World: Move the coconut in world space rather than local space. That means that even if we rotate the coconut it always falls towards ground.

### Update() Method

* Called every frame
* For VR, this might be called 60, 90, or even 120 times per seconds
**CAREFUL**: This speed depends on hardware and a variety of software factors.

### Time.delataTime

* Gives you smooth **framerate-independent** animation.
* Contains the amount of time it took to render the previous frame.
* Changes every frame.

#### IF Statement

1. Go to Script and modified
	```C#
	if(transform.position.y > 0.6f)
	{
		transform.Translate(0, -2.5f * Time.deltaTime, 0, Space.World);
	}
	```
2. Go back to unity and hit "Play" button
3. Coconut just hit the ground and stop
4. For fun
* Defying gravity
	```C
	transform.position = new Vector3(0, 5 + Mathf.Sin (Time.time * 5.0f), 0);
	```

[<- Previous](README.md) ..... [Next ->](README-3-2.md)
