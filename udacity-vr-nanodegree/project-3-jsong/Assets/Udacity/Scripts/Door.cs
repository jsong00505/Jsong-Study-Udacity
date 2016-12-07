using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Door : MonoBehaviour 
{
    // Create a boolean value called "locked" that can be checked in Update() 
    bool locked = true;

    void Update() {
        // If the door is unlocked and it is not fully raised
        if(!locked)
        {
            // Animate the door raising up
            gameObject.transform.Translate(0, 2*Time.deltaTime, 0, Space.World);
            if(gameObject.transform.position.y > 25)
            {
                locked = true;
                Debug.Log("The door is opened comletely");
            } else
            {
                Debug.Log("Running" + Time.deltaTime);
            }
            
        }
    }

    public void Unlock()
    {
        // You'll need to set "locked" to true here
        locked = false;
    }
}
