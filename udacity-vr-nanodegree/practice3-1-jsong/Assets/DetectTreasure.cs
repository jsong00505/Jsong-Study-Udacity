using UnityEngine;
using System.Collections;

public class DetectTreasure : MonoBehaviour {

    public Animator Anim;

    bool watched = false;
    void FixedUpdate()
    {
        Vector3 fwd = transform.TransformDirection(Vector3.forward);

        if (Physics.Raycast(transform.position, fwd, 10))
        {
            if(watched == false)
            {

                Anim.SetTrigger("Open");
                Anim.SetBool("OpenBool", true);
                watched = true;
                print("The chest will be open!");
            } else
            {
                print("The chest was already opened!");
            }
        }
            
    }

}
