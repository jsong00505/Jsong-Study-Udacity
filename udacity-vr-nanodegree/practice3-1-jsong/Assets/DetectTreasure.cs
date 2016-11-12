using UnityEngine;
using System.Collections;

public class DetectTreasure : MonoBehaviour {

    public Animator Anim;

    bool watched = false;
    void FixedUpdate()
    {
        Vector3 fwd = transform.TransformDirection(Vector3.forward);

        if (Physics.Raycast(transform.position, fwd, 10) && !watched)
        {
            if(watched == false)
            {
                print("The chest will be open!");
                Anim.SetTrigger("Open");
                watched = true;
            } else
            {
                print("The chest was already opened!");
            }
        }
            
    }

}
