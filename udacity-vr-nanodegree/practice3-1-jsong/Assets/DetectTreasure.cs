using UnityEngine;
using System.Collections;

public class DetectTreasure : MonoBehaviour {

    [SerializeField]
    private Animator Anim;

    private bool watched = false;

    void Start()
    {
        print("--> Start() <--");

        print(Anim.GetBool("OpenBool"));
    }
    private void FixedUpdate()
    {
        print("--> FixedUpdate() <--");
        Vector3 fwd = transform.TransformDirection(Vector3.forward);
        print("BOOL->>" + Anim.GetBool("OpenBool"));
        if (Physics.Raycast(transform.position, fwd, 10))
        {
            if(!watched)
            {
                Anim.SetBool("OpenBool", true);
                watched = true;
                print("The chest will be open!");
            }

        }
            
    }

}
