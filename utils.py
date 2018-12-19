import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAAE21khDS7kBAL0lT4HPLhmsxeS1G3XzFjBs5Oh4izvZCzVX4xzZBXHroiPxhbfncQxS5z3dGsUvm3rTZBFbltd1K72SBx0z84XDKbKW3LZBTZBTG5po8CJhA7koZCVveCv9JKeJ0dV1uxmAPQpY6maPSFAk98d1rKU2hrmUcvUAZDZD"

def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response



def send_video_message(id, the_url):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"open_graph",
                    "elements":[
                        {
                            "url":the_url
                        }
                    ]
                }
            }
        }
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""

