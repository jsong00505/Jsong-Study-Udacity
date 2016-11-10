using UnityEngine;
using System.Collections;

public class AudioPicker : MonoBehaviour {

    public AudioClip[] soundFiles;

    public AudioSource soundSource;

	// Use this for initialization
	void Start () {
        int index = Random.Range(0, soundFiles.Length);
        soundSource.clip = soundFiles[index];
        soundSource.Play ();
	}
	
	// Update is called once per frame
	void Update () {
	
	}
}
