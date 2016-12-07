using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class Key : MonoBehaviour 
{
    //Create a reference to the KeyPoofPrefab and Door
    public GameObject KeyPoofPrefab;
    public Door door;
    int directionFlag = 2;
	void Update()
	{
        // Bonus: Key Animation
        // Make the object go up and down or rotate
        if (gameObject.transform.position.y > 5)
        {
            directionFlag = -2;
        } else if (gameObject.transform.position.y < 3)
        {
            directionFlag = 2;
        }
        gameObject.transform.Translate(0, directionFlag * Time.deltaTime, 0, Space.World);

    }

	public void OnKeyClicked()
	{
        // Instatiate the KeyPoof Prefab where this key is located
        // Make sure the poof animates vertically
        // Call the Unlock() method on the Door
        // Destroy the key. Check the Unity documentation on how to use Destroy

        // Animation
        GameObject.CreatePrimitive(PrimitiveType.Cube);
        Instantiate(KeyPoofPrefab);

        Debug.Log("Get the key to open the door!!!");
        
        door.Unlock();
        Destroy(gameObject);

    }
}
