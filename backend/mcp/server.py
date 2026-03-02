import os
import json
from mcp.server.fastmcp import FastMCP
from openai import AsyncOpenAI
from backend.app.llm.prompt import SYSTEM_PROMPT

# Initialize FastMCP server
mcp = FastMCP("Analytics Query Generator")

# Initialize OpenAI Client (Requires OPENAI_API_KEY in .env)
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@mcp.tool()
async def generate_mongo_pipeline(user_query: str) -> str:
    """
    Translates a natural language query into a MongoDB aggregation pipeline.
    
    Args:
        user_query: The natural language question from the user.
    """
    try:
        response = await client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_query}
            ],
            response_format={"type": "json_object"}
        )
        
        return response.choices[0].message.content
    except Exception as e:
        return json.dumps({"error": str(e)})

if __name__ == "__main__":
    mcp.run()
