import exifread

def extract_metadata(image_path):
    with open(image_path, 'rb') as f:
        tags = exifread.prcs_file(f)

    cleaned_tags = {tag: str(value) for tag, value in tags.items()}

    return cleaned_tags

