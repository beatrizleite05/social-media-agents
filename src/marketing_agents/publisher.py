import json, requests, uuid
from .config import (
    INSTAGRAM_ACCESS_TOKEN, INSTAGRAM_PAGE_ID,
    LINKEDIN_ACCESS_TOKEN, LINKEDIN_ORG_ID
)

def post_on_instagram(post_text: str, img_url: str):
        if not INSTAGRAM_ACCESS_TOKEN or not INSTAGRAM_PAGE_ID:
            print("Instagram not set. skipping...")
            return

        media_ep = f"https://graph.facebook.com/v19.0/{INSTAGRAM_PAGE_ID}/media"
        publish_ep = f"https://graph.facebook.com/v19.0/{INSTAGRAM_PAGE_ID}/media_publish"
        creation = requests.post(media_ep, data={
            "image_url": img_url,
            "caption": post_text,
            "access_token": INSTAGRAM_ACCESS_TOKEN,
        }, timeout=30).json()

        cid = creation.get("id")
        
        if cid:
            requests.post(publish_ep, data={"creation_id": cid, "access_token": INSTAGRAM_ACCESS_TOKEN}, timeout=30)
            print("IG published successfully")
        else:
            print("IG error:", creation)


def post_on_linkedin(post_text: str):
    if not LINKEDIN_ACCESS_TOKEN or not LINKEDIN_ORG_ID:
        print("LinkedIn not set. skipping...")
        return

    r = requests.post(
        "https://api.linkedin.com/v2/ugcPosts",
        headers={
            "Authorization": f"Bearer {LINKEDIN_ACCESS_TOKEN}",
            "Content-Type": "application/json",
            "X-Restli-Protocol-Version": "2.0.0",
        },
        json={
            "author": f"urn:li:organization:{LINKEDIN_ORG_ID}",
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {"text": post_text},
                    "shareMediaCategory": "NONE",
                }
            },
            "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"},
        }, timeout=30,
    )
    if r.ok:
        print("LinkedIn published successfully")
    else:
        print("LinkedIn error:", r.status_code, r.text)
        
# Orchestration
def publish(json_posts: str):
    data = json.loads(json_posts)
    post_on_instagram(data["instagram"], img_url)
    post_on_linkedin(data["linkedin"])