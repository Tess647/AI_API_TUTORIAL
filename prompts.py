# prompts.py
system_message = "You are a helpful AI assistant that analyzes books and provides insights."

def generate_prompt(book, topic):
    prompt = f"""
    Book: {book}
    Analysis Topic: {topic}
    
    Please provide:
    1. Key insights about {topic} from this book
    2. Important quotes or passages related to {topic}
    3. How this book contributes to understanding {topic}
    
    Be thorough and analytical in your response.
    """