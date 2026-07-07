import json
import os
from config import CHECKPOINT_FILE
def load_checkpoint():
    """
    Load the last completed batch from checkpoint.json.
    Returns 0 if checkpoint doesn't exist.
    """
    if not os.path.exists(CHECKPOINT_FILE):
        return 0
    with open(CHECKPOINT_FILE, "r") as file:
        data = json.load(file)
    return data.get("last_completed_batch", 0)

def save_checkpoint(batch_number):
    """
    Save the last successfully completed batch.
    """
    data = {
        "last_completed_batch": batch_number
    }
    with open(CHECKPOINT_FILE, "w") as file:
        json.dump(data, file, indent=4)


def reset_checkpoint():
    """
    Reset checkpoint after successful pipeline completion.
    """
    data = {
        "last_completed_batch": 0
    }

    with open(CHECKPOINT_FILE, "w") as file:
        json.dump(data, file, indent=4)