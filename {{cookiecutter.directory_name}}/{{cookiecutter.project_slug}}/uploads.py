from flask_uploads import UploadSet, IMAGES


media_set = UploadSet(
    name="media", 
    extensions=IMAGES
)
