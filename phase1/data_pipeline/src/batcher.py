def batch_data(df, batch_size):
    batches = []
    for start in range(0, len(df), batch_size):
        end = start + batch_size
        batch = df.iloc[start:end]
        batches.append(batch)
    return batches