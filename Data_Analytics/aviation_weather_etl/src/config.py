from dotenv import load_dotenv
import os


load_dotenv()

STATION = os.getenv("STATION", "KNHK")
HOURS_BACK = int(os.getenv("HOURS_BACK", "24"))
DB_URL = os.getenv("DB_URL", "sqlite:///db/aviation.db")
