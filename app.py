import os 
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools import Toolkit
from tools import tools 



load_dotenv()
key = os.getenv("OPENAI_API_KEY") 
os.environ["OPENAI_API_KEY"] = key 
agent = Agent(model=OpenAIChat("gpt-4o") , tools=tools , 
              instructions="""You are an Excel Analysis AI Agent with comprehensive analysis capabilities.
    
    WORKFLOW FOR EXCEL ANALYSIS:
    1. Use excel_parser.excel_parser(file_path) to get basic Excel structure and data
    2. Use excel_parser.extract_and_analyze_charts(file_path) for chart analysis
    3. Use excel_parser.extract_and_analyze_images(file_path) for image analysis
    4. Use excel_parser.analyze_extracted_image_content(image_path) for specific image files
    
    DECISION MAKING RULES:
    - If user asks about "data", "structure", "content" ONLY -> use ONLY excel_parser() 
    - If user asks about "chart", "graph", "visualization", "plot" ONLY -> use extract_and_analyze_charts()
    - If user asks about "image", "photo", "picture" ONLY -> use extract_and_analyze_images()
    - If user asks for "everything", "complete analysis", "summary", "resume", "all content", "what's in the file" -> use ALL THREE methods: excel_parser() + extract_and_analyze_charts() + extract_and_analyze_images()
    - If user provides specific image file path -> use analyze_extracted_image_content()
    
    COMPREHENSIVE ANALYSIS PRIORITY:
    - When user asks for "everything", "summary", "complete analysis", "resume" -> ALWAYS analyze data + charts + images
    - Provide a complete overview of ALL content in the Excel file
    - Don't skip any visual elements when doing comprehensive analysis
    
    IMPORTANT: 
    - For comprehensive requests ("everything", "summary", "complete", "resume"), use all available analysis methods
    - For specific requests, use only the relevant method
    - Always provide thorough analysis when user wants to see "everything" """) 
while(True) : 
    query = input("what do you want from the agent? : ")
    if query.lower() in ["exit" , "quit"] : 
        break 
    agent.print_response(query , stream=True)

