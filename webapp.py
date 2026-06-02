#pip install gradio
#pip install groq

import gradio as gr
from groq import Groq

#groq api key
api_key="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"

Client=Groq(api_key=api_key)

#Gradio and groq Ai Based Multinpages websites Generator application
def generate_website(prompt):
    try:
        response=Client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system", 
                    "content": """
                    You are a senior web developer UI/UX designer 
                    and the frontend developer with expertise in HTML,CSS
                    , and JavaScript. You have expertise in creating visually appealing and user-friendly websites. 
                    Your task is to generate a complete website based on the user's prompt. The website should include multiple pages, a navigation menu, and a responsive design. 
                    Please provide the HTML, CSS, and JavaScript code for the website.

                    Generate a COMPLETE MULTI-PAGE WEBSITE in
                    ONE HTML file with embedded CSS and JavaScript
                    using internal navigation 

                    STRICT RULES:
                    - must be a full html document (DOCTYPE,html,head,style,script,body,div tags)
                    - all css and js must be embedded in same file
                    - use internal navigation(no external links)
                    - the website should have at least 3 pages
                    - the website should visyally appealing and user-friendly
                    - the website should be responsive and work well on different devices
                    - the website should include a navigation menu to navigate between pages
                    RETURN ONLY clean HTML code.
                    """

                }
                ,
                {
                    "role": "user", 
                    "content": f"""Generate a complete multi-page with style website for a startup based on the following prompt:
                      {prompt}
                      make sure to follow the strict rules mentioned in the system message and return only clean HTML code without any explanations or comments.
                      make it modern,beautiful, and user-friendly.
                      Use placeholders for images and content, and ensure that the design is visually appealing and responsive.
                      The website should include a homepage, an about page, and a contact page, with a navigation menu to navigate between them. The homepage should have a hero section with a call-to-action button, the about page should provide information about the startup, and the contact page should include a contact form and contact details.
             """
                }
            ]
        )
    except Exception as e:
        print("Error:", e)
        return "An error occurred while generating the website. Please try again."
    
