from typing import Dict, Optional


def find_image(post: Dict) -> Optional[str]:
    """Finds an image url in the post"""

    image_formats = [".png", ".jpg", ".jpeg", ".gif"]

    url = post.get("url")
    if url and any(url.endswith(x) for x in image_formats):
        return url
