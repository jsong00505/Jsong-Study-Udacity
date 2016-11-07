using UnityEngine;
using System.Collections;

public class ObjectMaker : MonoBehaviour {

    public GameObject objectToCreate;

    // Use this for initialization
    void Start () {
        Object.Instantiate(objectToCreate, new Vector3(2, 4, 6), Quaternion.identity);
    }
	
	// Update is called once per frame
	void Update () {
	
	}
}
