# NeuraCET

NeuraCET is a terminal-based AI assistant built in Python using Google's Gemini API. It combines conversational AI with tool calling, allowing Gemini to access real-time information from external services such as NewsAPI when needed.

## Features

* AI-powered chat using Gemini 2.5 Flash
* Rich terminal UI with markdown rendering
* Function/tool calling support
* Real-time news retrieval via NewsAPI
* Dynamic topic-based news search
* Environment variable support using `.env`
* Clean and lightweight Python implementation

## Demo

```bash
You>> latest gaming news

Gemini:
• Xbox announces ...
• PlayStation reveals ...
• Steam introduces ...
```

## Tech Stack

* Python
* Google Gemini API
* NewsAPI
* Rich
* Requests
* Python Dotenv

## Project Structure

```text
gemini_neuracet/
├── main.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env
```

## Installation

### Clone the repository

```bash
git clone https://github.com/NandhuRamesh143/gemini_neuracet.git
cd gemini_neuracet
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the environment

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
newsapi=your_newsapi_key
```

## Running the Project

```bash
python main.py
```

## How It Works

1. User enters a prompt.
2. Gemini determines whether a tool is needed.
3. If news is requested, Gemini calls the `get_news` tool.
4. Python fetches relevant headlines from NewsAPI.
5. Headlines are returned to Gemini.
6. Gemini generates a final response using the retrieved information.

## Example Queries

```text
latest AI news
```

```text
gaming news
```

```text
OpenAI news
```

```text
Formula 1 news
```

```text
Bitcoin news
```

## Future Plans

* Weather tool integration
* Reddit integration
* YouTube search tool
* Desktop GUI using PySide6
* Conversation history
* Multi-tool orchestration
* Local file interaction

## Author

Nandhu Ramesh

GitHub: https://github.com/NandhuRamesh143

## License

This project is licensed under the MIT License.
