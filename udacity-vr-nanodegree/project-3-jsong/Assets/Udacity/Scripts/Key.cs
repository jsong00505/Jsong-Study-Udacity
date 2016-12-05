﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class Key : MonoBehaviour 
{
    //Create a reference to the KeyPoofPrefab and Door
    public GameObject KeyPoofPrefab;
    public GameObject KeyPrefab;
    public Door door;

	void Update()
	{
		//Bonus: Key Animation
	}

	public void OnKeyClicked()
	{
        // Instatiate the KeyPoof Prefab where this key is located
        // Make sure the poof animates vertically
        // Call the Unlock() method on the Door
        // Destroy the key. Check the Unity documentation on how to use Destroy
        Debug.Log("Get the key to open the door!!!");
        
        door.Unlock();

    }
}
