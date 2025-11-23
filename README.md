# PDF Knowledge Extractor with AI

A beginner-friendly Python project that extracts knowledge from PDF files using AI. This tool reads a PDF, focuses on a specific topic, and uses OpenAI's GPT model to generate summaries and insights.

## 🌟 What This Project Does

Imagine you have a long PDF (like a book or report) and you want to quickly understand everything it says about a particular topic like "money", "leadership", or "technology". This tool does exactly that! It:

1. **Reads** your PDF file
2. **Extracts** the text content
3. **Asks** an AI to find and summarize key ideas about your chosen topic
4. **Presents** a clean, concise summary

## 🛠️ What You'll Need

### Prerequisites
- Basic understanding of Python
- An OpenAI API account (like a ChatGPT subscription but for developers)

### Tools Required
- Python 3.7 or higher
- An OpenAI API key

## 📁 Project Structure

```
pdf-ai-extractor/
├── main.py              # Main program file
├── prompts.py           # Instructions for the AI
├── naval.pdf           # Example PDF file (you can replace this)
├── .env                # Your secret API key (create this file)
└── README.md           # This file
```

## 🚀 Quick Start Guide

### Step 1: Setup Your Environment

1. **Install Python packages:**
   ```bash
   pip install PyPDF2 openai python-dotenv
   ```

2. **Get your OpenAI API key:**
   - Go to [OpenAI's platform](https://platform.openai.com/)
   - Create an account or sign in
   - Go to "API Keys" and create a new secret key
   - Copy your key

3. **Create your environment file:**
   Create a file called `.env` in the project folder and add:
   ```
   OPENAI_API_KEY=your_secret_key_here
   ```
   Replace `your_secret_key_here` with the actual key you copied.

### Step 2: Prepare Your Files

1. **Create `prompts.py`:**
   ```python
   system_message = "You are a helpful assistant that extracts and summarizes key ideas from texts."

   def generate_prompt(book_text, topic):
       return f"""
       Please analyze the following text and extract all important ideas, concepts, 
       and insights related to the topic of '{topic}'. 
       
       Present the information in a clear, organized way that would help someone 
       understand what the text says about {topic}.
       
       TEXT:
       {book_text}
       """
   ```

2. **Add your PDF:**
   - Place your PDF file in the project folder
   - Update the `file_path = "your-file.pdf"` line in `main.py`

### Step 3: Configure the Settings

In `main.py`, you can customize:

```python
model = 'gpt-4'  # You can use 'gpt-3.5-turbo' for faster, cheaper results
temperature = 0.3  # Lower = more factual, Higher = more creative
max_tokens = 500   # Length of the AI's response
topic = "money"    # Your topic of interest
```

### Step 4: Run the Program

```bash
python main.py
```

The program will:
- Load your PDF
- Read the specified pages
- Send the text to the AI
- Print out a beautiful summary about your chosen topic

## ⚙️ Customization Options

### Change the PDF Pages
Modify these lines in `main.py`:
```python
start_page = 23      # Skip first 22 pages
end_page = total_pages - 30  # Skip last 30 pages
```

### Try Different Topics
Change the `topic` variable:
```python
topic = "leadership"
# or
topic = "success"
# or
topic = "happiness"
```

### Adjust AI Behavior
- **Temperature**: `0.1` for very factual, `0.7` for creative
- **Max Tokens**: `300` for short answers, `1000` for detailed analysis

## 💡 Example Use Cases

- **Students**: Extract key concepts from textbook chapters
- **Researchers**: Summarize academic papers on specific themes
- **Book Clubs**: Focus on particular themes in a book
- **Business**: Analyze reports for specific topics like "risk" or "opportunities"

## 🛠️ Troubleshooting

### Common Issues

1. **"Module not found" error**
   ```bash
   pip install missing-package-name
   ```

2. **"Invalid API key" error**
   - Check your `.env` file exists
   - Verify the API key is correct
   - Make sure you have credits in your OpenAI account

3. **PDF won't open**
   - Ensure the PDF file is in the same folder as `main.py`
   - Check the filename matches exactly (including .pdf extension)

4. **AI response is too short/long**
   - Adjust the `max_tokens` parameter
   - Modify the prompt in `prompts.py`

## 🔒 Important Notes

- **Keep your API key secret**: Never share your `.env` file or commit it to public repositories
- **Cost awareness**: Using the API costs money (check OpenAI's pricing)
- **PDF quality**: The tool works best with text-based PDFs, not scanned images

## 🎯 Next Steps

Once you're comfortable with the basics, you could enhance this project by:

- Adding support for multiple PDF files
- Creating a simple web interface
- Adding export functionality (save summaries as text files)
- Implementing batch processing for multiple topics

## 📚 Learning Resources

- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [PyPDF2 Documentation](https://pypdf2.readthedocs.io/)

## 🤝 Contributing

This is a learning project! Feel free to:
- Experiment with different prompts
- Try different PDF processing libraries
- Add error handling and user feedback
- Create your own variations

---

**Happy coding!** Remember, every expert was once a beginner. Don't hesitate to experiment and make this project your own. 🚀