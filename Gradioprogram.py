#Gradio
#pip install gradio
import gradio as gr
with gr.Blocks() as demo:
    gr.Markdown("## Hello, Gradio!")
    input_text=gr.Textbox(label="Enter your name")
    output_text=gr.Textbox(label="Output")
    btn=gr.Button("Submit")
    btn.click(
        fn=lambda x:x.upper(),
        inputs=input_text,
        outputs=output_text
    )
demo.launch(share=True)