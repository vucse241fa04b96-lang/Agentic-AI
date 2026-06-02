from groq import Groq
class AIGROQAGENT:
    def __init__(self,api_key,model_name="llama-3.3-70b-versatile"):
        self.client=Groq(api_key=api_key)
        self.model_name=model_name
    def generate(self,prompt):
        response=self.client.chat.completions.create(
            model=self.model_name,
            messages=[{"role":"user","content":prompt}],
            max_tokens=1024,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    #Agent task execution process
    def execute_task(self,task_details):
        task_prompt=f"""
        you are an autonomous AI Agent.
        Task
        {task_details}
        provide the solve this task step-by-step.
        """
        return self.generate(task_prompt)
    #Learning/Reflection process
    def learn_from_experience(self,experience_details):
        learning_prompt=f"""
        you are an autonomous AI Agent.
        Analyze the following experience
        and provide insights for improvement.
        Experience
        {experience_details}
        reflect on this experience and provide insights for improvement.
        """
        return self.generate(learning_prompt)

if __name__=="__main__":
    API_KEY="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"
    while True:
        agent=AIGROQAGENT(API_KEY)
    agent=AIGROQAGENT(API_KEY)
    # prompt=input("Enter your prompt: ")
    # response=agent.generate(prompt)
    # print("AI Response:",response)
    # prompt1="provide the top 3  bike companies list with details"
    # response1=agent.execute_task(prompt1)
    # print("AI Task Response:",response1)
    # prompt2="I had a conversation with a customer where I failed to address their concerns effectively. The customer was upset about a delayed delivery and expressed their frustration. I struggled to provide a satisfactory solution and ended up escalating the issue to my supervisor. Reflecting on this experience, I realize that I could have handled the situation better by actively listening to the customer's concerns, empathizing with their frustration, and offering alternative solutions such as expedited shipping or a discount on their next purchase. Additionally, I should have remained calm and composed throughout the conversation instead of becoming defensive. Moving forward, I will focus on improving my communication skills and finding ways to de-escalate tense situations with customers."
    # response2=agent.learn_from_experience(prompt2)
    # print("AI Learning Response:",response2)
    PROMPT2=INPUT("enter the prompt")

