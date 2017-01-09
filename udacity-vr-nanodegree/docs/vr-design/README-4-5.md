# Let's get moving!
[<- Previous](README-4-4.md) ..... [Next ->](README-4-6.md)

## Simulator Sickness

* Use linear acceleration
* Move forwards
* Remain stationary when possible
* Give users controlKeep movement time short
* Keep a high frame rate

**REF: Oculus Best Practice**

[Here is the link](https://developer3.oculus.com/documentation/intro-vr/latest/concepts/bp_app_simulator_sickness/)

## Mobile VR limitations

* Movement mechanics are still being explored

## 3rd party library

* iTween

```C#
public void startPuzzle() { //Begin the puzzle sequence
    toggleUI();
    iTween.MoveTo (player,
        iTween.Hash (
            "position", playPoint.transform.position,
            "time", 2,
            "easetype", "linear"
        )
    );
}
```  

## Let's get moving!

* This is primary practice in this chapter

## Considerations for user testing movement

* The user is not like you!(they probably get sick easier)
* Make sure your user is well informed about the test
* Teach them how to mitigate VR sickness ahead of time

[<- Previous](README-4-4.md) ..... [Next ->](README-4-6.md)
