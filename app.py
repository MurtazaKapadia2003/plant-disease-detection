import gradio as gr

def predict(image):
    return "🌱 Plant is healthy!"

demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs=gr.Textbox(),
    title="Plant Disease Detection",
    description="Upload a plant leaf image to detect diseases"
)

demo.launch()
