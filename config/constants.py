from config.paths import OUTPUT_DIR
from pathlib import Path

OPENROUTER_API_KEY = "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"

OPENROUTER_MODEL= "meta-llama/llama-4-scout:free"   
OPENROUTER_URL = "https://openrouter.ai/api/v1"
# openrouter

outputfile = Path(OUTPUT_DIR / 'a.out')

PROG_LANG = {
    "python", "java", "javascript", "c", "cpp", "c#", "ruby", "go", "kotlin", "swift", "php",
    "typescript", "scala", "perl", "rust", "r", "haskell", "matlab", "dart", "lua", "sql"
}
LANG_EXT = {
    "python": ".py",
    "java": ".java",
    "javascript": ".js",
    "c": ".c",
    "cpp": ".cpp",
    "c#": ".cs",
    "ruby": ".rb",
    "go": ".go",
    "kotlin": ".kt",
    "swift": ".swift",
    "php": ".php",
    "typescript": ".ts",
    "scala": ".scala",
    "perl": ".pl",
    "rust": ".rs",
    "r": ".r",
    "haskell": ".hs",
    "matlab": ".m",
    "dart": ".dart",
    "lua": ".lua",
    "sql": ".sql"
}


LANG_COM = {
    ".py": ["python", "{filename}"],
    ".java": ["javac", "{filename}"], 
    ".js": ["node", "{filename}"],
    ".c": ["gcc", "{filename}", "-o", str(outputfile)], 
    ".cpp": ["g++", "{filename}", "-o", str(outputfile)],
    ".rb": ["ruby", "{filename}"],
    ".go": ["go", "run", "{filename}"],
    ".ts": ["ts-node", "{filename}"],
    ".rs": ["rustc", "{filename}"], 
    ".php": ["php", "{filename}"],
    ".sh": ["bash", "{filename}"],
    ".pl": ["perl", "{filename}"],
}

OPEN_QUES = [
    "Please enter the task.",
    "What task would you like me to perform?",
    "Enter the task you'd like help with.",
    "Hi there! What task can I help you with today?",
    "Just let me know the task you'd like me to handle.",
    "What would you like me to do?",
    "Add a new task—what do you want to get done?",
    "What's the next task on your to-do list?",
    "Describe the task you'd like to create or work on."
]

FEED_QUES = [
    "Is the output as expected after running the code?",
    "Was the result of the code execution as anticipated?",
    "Were there any exceptions or issues in the code execution?",
    "Did the code run successfully?",
    "Was the execution of the code successful?",
    "Were there any errors during the code execution?",
    "Can you confirm if the code executed without any issues?",
    "Did the code complete successfully, or did it encounter any problems?"
]