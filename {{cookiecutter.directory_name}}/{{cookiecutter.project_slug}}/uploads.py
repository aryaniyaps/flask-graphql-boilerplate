from flask_uploads import UploadSet, IMAGES


avatar_set = UploadSet(
    name="avatars", 
    extensions=IMAGES
)
