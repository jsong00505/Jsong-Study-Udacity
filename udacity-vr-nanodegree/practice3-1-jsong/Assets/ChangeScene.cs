using UnityEngine;
using System.Collections;
using UnityEngine.SceneManagement;

public class ChangeScene : MonoBehaviour {
    public void GoToScene(string sceneName)
    {
        Debug.Log("My method was called!");
        // SceneManager.LoadScene("00-FallingCoconut");
        SceneManager.LoadScene(sceneName);
    }

}
