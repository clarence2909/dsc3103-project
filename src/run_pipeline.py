
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.common.logging_setup import get_logger
from src.ingest.source_a import ingest_source_a
from src.ingest.source_b import ingest_source_b
from src.transform.clean import clean_data
from src.transform.merge import merge_data



# making object

logger = get_logger()

def run_pipe():
    logger.info("=== Ppeline run started ===")

    logger.info("Stage 1: Ingesting source a")
    source_a = ingest_source_a()
    logger.info (f"Stage 11: Source a Ingested rows out: {len(source_a)}")

    logger.info("Stage 2: Ingesting source b")
    source_b = ingest_source_b()
    logger.info (f"Stage 22: Source b Ingested rows out: {len(source_b)}")

    logger.info("stage 3: Cleaning source a...")
    clean_prices, decisions = clean_data()
    logger.info(
        f"stage 33: Source a cleaned rows in: {len(clean_prices)} | "
        f"rows out: {len(clean_prices)} | "
        f"decisions made: {len(decisions)}"
    )

    logger.info("Stage 4: Merging Price and Rainfall")
    merged = merge_data(clean_prices, source_b)
    logger.info(f"Stage 44: Merged complete : rows in: {len(merged)},rows out: {len(merged)}")

    logger.info("Stage 5: Saving merged file")
    merged.to_parquet(PATH, index= False)
    logger.info(f"Stage 55: Saving complete: Saved {len(merged)} rows")


    logger.info("=== Pipeline run completed ===")





    



if __name__ == "__main__":
    run_pipe()


