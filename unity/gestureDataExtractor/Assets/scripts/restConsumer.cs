using UnityEngine;
using System.Collections;
using UnityEngine.Networking;
using System.Text;
using System.Collections.Generic;

public class RestConsumer {
    public string url = "http://192.168.178.154:5000/gesture/classify";

    public IEnumerator SendToServer(string data)  
    {
        Dictionary<string,string> headers = new Dictionary<string, string>();
        headers.Add("Content-Type", "application/json");
            
        byte[] pData = Encoding.ASCII.GetBytes(data.ToCharArray());

        Debug.Log("starting gesture Upload");
        // Start a download of the given URL
        WWW www = new WWW(url, pData, headers);
 
        // Wait for download to complete
        yield return www;
    }
}
