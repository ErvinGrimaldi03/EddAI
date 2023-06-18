from transformers import pipeline

# Initialize the summarizer
summarizer = pipeline("summarization")

def chunk_text(text, chunk_size):

    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def summarize_text(text, min_length=30, max_length=150):
    print("RUNNING SUMMARIZE. . .")
    # Break the text into chunks
    chunks = chunk_text(text, 1000)  # Adjust as needed

    # Initialize an empty string for the summary
    summary = ""

    # Process each chunk
    for chunk in chunks:
        # Generate the summary for this chunk
        chunk_summary = summarizer(chunk, max_length=max_length, min_length=min_length, do_sample=False)
        # Add this summary to the overall summary
        summary += chunk_summary[0]['summary_text']
    print(summary)
    # Return the overall summary
    return summary
