using UnityEngine;
using System.Collections;

public class DetectTreasure : MonoBehaviour {

    [SerializeField]
    private Animator Anim;

    private bool watched = false;
    private void FixedUpdate()
    {
        Vector3 fwd = transform.TransformDirection(Vector3.forward);

        if (Physics.Raycast(transform.position, fwd, 10))
        {
            if(!watched)
            {
                Anim.SetBool("OpenBool", true);
                //Anim.SetBool("OpenBool", false);
                watched = true;
                print("The chest will be opened!");
            }
        }
            
    }

}
