using UnityEngine;
using System.Collections;

public class RotateLight : MonoBehaviour {

    public GameObject directionalLight;

	// Use this for initialization
	void Start () {
	
	}
	
	// Update is called once per frame
	void Update () {
        directionalLight.transform.Rotate(0f, Time.deltaTime, 0f);

        //Quaternion startRotation = Quaternion.Euler(50f, 30f, 0f);
        //Quaternion endRoatation = startRotation * Quaternion.Euler(0, 180f, 0f);

        //directionalLight.transform.rotation = Quaternion.Slerp(startRotation, endRoatation, Time.time);

    }
}
