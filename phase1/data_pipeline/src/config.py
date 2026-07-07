from dotenv import load_dotenv
import os

load_dotenv()

# API Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = "gemini-2.5-flash"
GEMINI_EMBEDDING_MODEL = "gemini-embedding-001"
# File Paths
INPUT_CSV = "data/input.csv"
CLEANED_CSV = "data/cleaned.csv"
OUTPUT_FILE = "data/embeddings.json"
CHECKPOINT_FILE = "data/checkpoint.json"

# Pipeline Configuration
BATCH_SIZE = 20
MAX_RETRIES = 3
REQUEST_TIMEOUT = 30