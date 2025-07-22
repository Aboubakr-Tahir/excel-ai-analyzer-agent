# 🤖 Excel AI Analyzer Agent

An intelligent Excel analysis system that extracts and analyzes data, charts, and images from Excel files using GPT-4 Vision API.

## ✨ Features

- 📊 **Smart Chart Analysis** - Extract charts using Spire.XLS and analyze with GPT-4V
- 🖼️ **Image Understanding** - Extract and analyze embedded images with AI
- 📈 **Complete Data Analysis** - Full Excel structure and content analysis
- 🧠 **AI-Powered Insights** - Uses GPT-4 Vision for visual content understanding
- 🔄 **Multi-Modal Processing** - Handles data, charts, and images in one workflow

## 🛠️ Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Aboubakr-Tahir/excel-ai-analyzer-agent.git
   cd excel-ai-analyzer-agent
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Install Spire.XLS:**

   ```bash
   pip install Spire.XLS
   ```

4. **Set up environment:**
   ```bash
   cp .env.example .env
   # Add your OpenAI API key to .env file
   ```

## 🚀 Usage

### Basic Commands:

- **Complete Analysis:** `"give me a summary of file.xlsx"`
- **Chart Analysis:** `"explain the chart in file.xlsx"`
- **Image Analysis:** `"what's in the image in file.xlsx"`
- **Data Only:** `"show me the data structure in file.xlsx"`

### Example:

```python
python app.py
# What do you want from the agent?: give me a summary of clients_fictifs.xlsx
```

## 📋 Requirements

- Python 3.8+
- OpenAI API key
- Spire.XLS library
- See `requirements.txt` for full dependencies

## 🏗️ Project Structure

```
excel-ai-analyzer-agent/
├── app.py              # Main application
├── tools.py            # Excel analysis tools
├── test.py             # Chart extraction example
├── requirements.txt    # Dependencies
├── .env.example        # Environment template
└── README.md          # This file
```

## 🔧 How It Works

1. **Data Extraction** - Analyzes Excel structure and content with Pandas
2. **Chart Processing** - Uses Spire.XLS to extract charts as images
3. **Image Analysis** - Leverages GPT-4V to understand visual content
4. **Comprehensive Reporting** - Combines all analyses into detailed insights

## 📝 License

MIT License - see LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ⚠️ Security Note

Never commit your `.env` file with API keys. Use `.env.example` as a template.
