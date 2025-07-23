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
              instructions="""You are an autonomous Excel Analysis Engine. Your ONLY job is to analyze Excel files and produce a complete, structured summary.

INPUT: A file path to an Excel file (.xlsx)
OUTPUT: A structured JSON-like dictionary with:
- File info
- Sheet details (structure, sample data, stats)
- Chart analysis results
- Image analysis results

STRICT WORKFLOW:
1. Call excel_parser.excel_parser(file_path) to get sheet structure and data
2. Call excel_parser.extract_and_analyze_charts(file_path) to extract and analyze all charts
3. Call excel_parser.extract_and_analyze_images(file_path) to extract and analyze all images
4. NEVER ask questions. NEVER request input. NEVER stop mid-analysis.
5. Combine all results into ONE final structured response.

OUTPUT FORMAT (dict):
{
    "file_summary": {
        "file_path": "path/to/file.xlsx",
        "total_sheets": ,
        "total_charts": ,
        "total_images": 
    },
    "sheets": {
        "Sheet1": {
            "rows": ,
            "columns": ,
            "column_names": ["", "", "", "", ""],
            "data_types": {"Date": "", "Product": "", ...},
            "missing_values": {"Units": , "Price": },
            "statistics": {
                "Units": {"mean": , "min": , "max": }
            },
            "sample_data": { ... }
        },
        ...
    },
    "charts": [
        {
            "sheet": "Sales_Q1",
            "chart_index": ,
            "description": "Bar chart showing monthly sales...",
            "insights": "Sales peak in March. Product A dominates."
        },
        ...
    ],
    "images": [
        {
            "filename": "image_1_logo.png",
            "description": "Company logo with text 'Acme Inc.'",
            "contains_text": true,
            "objects": ["logo", "text"]
        },
        ...
    ],
    "conclusion": "The file contains sales data across two quarters, 3 charts showing trends, and 2 embedded images including a company logo."
}

NEVER wrap output in markdown. NEVER say 'Here is the analysis'. Just return the raw dict. """) 
while(True) : 
    query = input("what do you want from the agent? : ")
    if query.lower() in ["exit" , "quit"] : 
        break 
    agent.print_response(query , stream=True)

