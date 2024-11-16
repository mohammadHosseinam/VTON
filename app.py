import gradio as gr
from PIL import Image
#import keras

def process_images(person, cloth):
    #model = keras.models.load_model('./model/model name')
    #output = model.predict(person , cloth)
    output = Image.blend(person, cloth, alpha=0.5)
    return output


examples = [
    ["images/000004_0.jpg", "images/019592_1.jpg"],
    ["images/000013_0.jpg", "images/019593_1.jpg"]
]


iface = gr.Interface(
    fn=process_images,  
    inputs=[
        gr.Image(type="pil", label="person Image"),
        gr.Image(type="pil", label="cloth Image")
    ],
    outputs=gr.Image(type="pil", label="Output Image"),
    title="Virtual Try On",  
    description="Upload person and cloth images and get one dressed image as output.",
    examples=examples  
)

iface.launch()
