import logging
from pathlib import Path


# Logging to file + Console
Path("logs").mkdir(exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[logging.FileHandler("logs/run.log"), logging.StreamHandler()]
)

def main():
    logging.info("Phase 0 bootstrap verified. Next: implement ingest in Phase 1.")

if __name__=="__main__":
    main()