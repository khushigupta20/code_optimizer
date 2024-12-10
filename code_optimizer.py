from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

def optimizeCode(original_code):

    # Optionally, you can set the token as an environment variable to avoid hardcoding it
    openai_api_key = os.getenv("OPENAI_API_KEY")

    # Set up OpenAI model with LangChain
    llm = OpenAI(
        openai_api_key=openai_api_key,  # Pass your OpenAI API key
        model="gpt-3.5-turbo-instruct",        # Choose the OpenAI model (e.g., text-davinci-003 or gpt-3.5-turbo)
        temperature=0.5                  # Adjust temperature for response randomness
    )

    # Define a prompt template for optimizing code
    template = """
    You are an expert Software developer. Your task is to identify language of the code given below, optimize the code, improving efficiency and readability while maintaining its original functionality.

    Here is the code to optimize:
    {code}

    ---------------------------------------------------------------------------
    Please provide the optimized version of the code along with detailed reasons.
    """

    # Create a prompt template
    prompt = PromptTemplate(input_variables=["code"], template=template)

    # Set up the LLMChain with the model and prompt
    chain = LLMChain(llm=llm, prompt=prompt)

    # Run the chain to get optimized code
    optimized_code = chain.run({"code": original_code})

    # Print the optimized code
    print(optimized_code)

    return optimized_code

