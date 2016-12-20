# How to Use Git and GitHub

## What we'll cover

* Lesson 1: why version control?
	* install `git` + read-only usage

* Lesson 2: read + write `git`

* Lesson 3: share + collaborate `GitHub`

## Asteroids Game

* [Doug's website](http://www.dougmcinnes.com/html-5-asteroids/)
* Using space to fire the engine might be more intuitive to usage

	Changing Control Keys
	Fire the engine: up arrow -> space
	Shoot: space -> enter

* game.js

```javascript
...
KEY_CODES = {
  32: 'space',
  37: 'left',
  38: 'up',
  39: 'right',
  40: 'down',
  70: 'f',
  71: 'g',
  72: 'h',
  77: 'm',
  80: 'p'
}
...
```

** Too long to find differences between old and new!! **

## Automatically Compare Files

* Windows - FC (file compare)
* Max - Diff (difference)
* Linux - Diff (difference)

## CMD

	// Windows
	// move to the folder where the files in
	uda> FC favorite-app-old.html favorite-app.html

	// Mac or Linux
	uda> diff - u favorite-app-old.html favorite-app.html

## Reflections

**How did viewing a diff between two versions help you spot the bug?**

### Why should I?

* This really helps!
* you'll use this content for vc prectice

### How?

* One file per lesson
* plain-text, Not rich-text

## Setup

[References](https://classroom.udacity.com/courses/ud775/lessons/2980038599/concepts/29975186190923#)
