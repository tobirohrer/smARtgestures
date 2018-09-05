using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.VR.WSA.Input;
using UnityEngine.VR;
using UnityEngine.Networking;

public class gestureDataCollector : MonoBehaviour {

    public AudioClip audioClip;
    public bool sendGeturesToBackend = false;
    List<Vector3> gesturePositions = new List<Vector3>();
    bool recordingGesture = false;
    GestureList gestureList = new GestureList();
    RestConsumer restConsumer = new RestConsumer();
    const string outputFile = "G:\rawGestures.txt"

    GestureRecognizer recognizer;

    void Start()
    {
        
        Debug.Log("started gestureDetector");
        SetupGestureRecognizer();
        InteractionManager.SourceDetected += InteractionManager_SourceDetected;
        InteractionManager.SourceUpdated += InteractionManager_SourceUpdated;
        InteractionManager.SourceLost += InteractionManager_SourceLost;
        }

    void SetupGestureRecognizer() {
        Debug.Log("setting up gesture recognizer");
        recognizer = new GestureRecognizer();
        recognizer.SetRecognizableGestures(GestureSettings.Tap);
        recognizer.StartCapturingGestures();
        recognizer.TappedEvent += MyTapEventHandler;
        Debug.Log("gesture recognizer ready");
    }

    void OnDestroy()
    {
        InteractionManager.SourceDetected -= InteractionManager_SourceDetected;
        InteractionManager.SourceUpdated -= InteractionManager_SourceUpdated;
        InteractionManager.SourceLost -= InteractionManager_SourceLost;

        string json = JsonUtility.ToJson(gestureList);
        Debug.Log(json);
        System.IO.File.WriteAllText(@outputFile, json);
    }

    void MyTapEventHandler(InteractionSourceKind source, int tapCount, Ray ray) {
        Debug.Log("tap gesture recoreded");
        AudioSource.PlayClipAtPoint(audioClip, new Vector3(0, 0, 0));
        if (recordingGesture == true) {
            TransformGestureData();
        }

        recordingGesture = !recordingGesture;
        Debug.Log("recordingState " + recordingGesture);
    }

    void TransformGestureData() {

        Gesture gesture = new Gesture();
        int[] gestureClass = { 0,0,0,1 };
        gesture.gestureClass = gestureClass;
        gesture.gestureData = new List<Vector3>(gesturePositions);

        gestureList.gestureList.Add(gesture);

        Debug.Log("size of captured gesture is " + gesturePositions.Count);
        string gestureJson = JsonUtility.ToJson(gesture);
        Debug.Log(gestureJson);
        if (sendGeturesToBackend) {
            StartCoroutine(restConsumer.SendToServer(gestureJson));
        }
        gesturePositions.Clear();
    }

    void InteractionManager_SourceDetected(InteractionSourceState state)
    {
        Debug.Log(state.source.kind + " detected");
    }

    void InteractionManager_SourceLost(InteractionSourceState state)
    {
        // Source was lost. This will be after a SourceDetected event and no other events for this source id will occur until it is Detected again
        // state has the current state of the source including id, position, kind, etc.
    }

    void InteractionManager_SourceUpdated(InteractionSourceState state)
    {
        Vector3 relativeHandPosition;
        InteractionSourceProperties interActionSourceProperties = state.properties;
        InteractionSourceLocation interactionSourceLocation = interActionSourceProperties.location;

        if (recordingGesture == true) { 
            interactionSourceLocation.TryGetPosition(out relativeHandPosition);
            Debug.Log(relativeHandPosition);
            gesturePositions.Add(relativeHandPosition);
        }

        // Source was updated. The source would have been detected before this point
        // state has the current state of the source including id, position, kind, etc.
    }
}
