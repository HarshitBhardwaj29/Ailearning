import asyncio

from tqdm import tqdm

from csv_reader import read_csv
from cleaner import clean_data
from batcher import batch_data
from embedding_service import get_embeddings
from writer import save_embeddings
from retry import retry_with_backoff
from checkpoint import (
    load_checkpoint,
    save_checkpoint,
    reset_checkpoint,
)

from config import (
    INPUT_CSV,
    BATCH_SIZE,
)


async def run_pipeline():
    # Read CSV
    df = read_csv(INPUT_CSV)

    print("===== Before Cleaning =====")
    print(df)

    # Clean Data
    df = clean_data(df)

    print("\n===== After Cleaning =====")
    print(df)

    # Create batches
    batches = batch_data(df, BATCH_SIZE)
    print(f"\nTotal Batches: {len(batches)}")
    # Load checkpoint
    last_completed_batch = load_checkpoint()

    print(f"Resuming from batch {last_completed_batch + 1}")

    # Skip completed batches
    remaining_batches = batches[last_completed_batch:]

    # Create async tasks
    tasks = [
        retry_with_backoff(get_embeddings, batch)
        for batch in remaining_batches
    ]

    all_embeddings = []

    with tqdm(total=len(tasks), desc="Generating Embeddings") as progress:

        current_batch = last_completed_batch
        for response in asyncio.as_completed(tasks):
            result = await response
            all_embeddings.extend(result)
            current_batch += 1
            # Save checkpoint
            save_checkpoint(current_batch)
            progress.update(1)

    # Save embeddings
    save_embeddings(all_embeddings)

    # Reset checkpoint
    reset_checkpoint()

    print(f"\nSaved {len(all_embeddings)} embeddings successfully!")