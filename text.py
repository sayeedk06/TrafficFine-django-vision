import io
from google.cloud import vision


# file_name = 'Outline-of-the-Bangladesh-license-plates_Q320.jpg'

# client = vision.ImageAnnotatorClient()

# with io.open(file_name, 'rb') as image_file:
# 	content = image_file.read()

# image = vision.types.Image(content=content)

# response = client.text_detection(image=image)
# texts = response.text_annotations
# print('Texts:')

# for text in texts:
# 	print('\n"{}"'.format(text.description))

# 	vertices = (['({},{})'.format(vertex.x, vertex.y)
# # for vertex in text.bounding_poly.vertices])

# 	print('bounds: {}'.format(','.join(vertices)))



def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)
    image_context = vision.types.ImageContext(language_hints=["bn"])
	# image_context = types.ImageContext(language_hints =['bn'])
    response = client.text_detection(image=image,image_context=image_context)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))


detect_text('Outline-of-the-Bangladesh-license-plates_Q320.jpg')