from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate

def optimizeCode(original_code):

    # Load the smaller model and tokenizer
    model_name = "Salesforce/codegen-350M-multi"  # Using a smaller model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    # Create a Hugging Face pipeline
    hf_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer, max_length=256)

    # Wrap the pipeline with LangChain's HuggingFacePipeline
    llm = HuggingFacePipeline(pipeline=hf_pipeline)

    # Define the prompt template
    prompt_template = PromptTemplate(
        input_variables=["task", "constraints", "code"],
        template="""
        You are an expert software developer. Your task is to optimize and clean provided code.
        Task: {task}
        Constraints: {constraints}

        Provide code that adheres to best practices, is efficient, and easy to maintain. Please provide details of changes made and reasons.

        Provided Code:
        {code}
        """
    )

    # Specify task and constraints
    task = "Optimize the given code below."
    constraints = "The code should have minimal time complexity and minimal auxiliary space."

    # Format the prompt
    formatted_prompt = prompt_template.format(task=task, constraints=constraints, code=original_code)

    # Generate a response from the model
    response = llm(formatted_prompt)
    print(response)

    return response

