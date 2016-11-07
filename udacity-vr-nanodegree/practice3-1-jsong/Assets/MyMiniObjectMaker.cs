using UnityEngine;
using System.Collections;

public class MyMiniObjectMaker : MonoBehaviour {

    public GameObject objectToCreate;

    // Use this for initialization
    void Start () {
        //Object.Instantiate(objectToCreate, new Vector3(2, 4, 6), Quaternion.identity);
        for(int i = 0; i < 50; i++)
        {
            //Object.Instantiate(objectToCreate, new Vector3(i, 4, 6), Quaternion.identity);
            GameObject newSeagull = (GameObject)Object.Instantiate(objectToCreate, new Vector3(i, 0, 0), Quaternion.identity);
            Renderer objectRenderer = newSeagull.GetComponentInChildren<Renderer>();
            objectRenderer.material.color = Color.white * Random.value;
        }
    }
	
	// Update is called once per frame
	void Update () {
	
	}
}
