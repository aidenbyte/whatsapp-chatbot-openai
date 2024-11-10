# 🚀 WATI Webhook Service

A beginner-friendly WhatsApp messaging service built with FastAPI and WATI API. Perfect for those learning Python web development!

## 🎯 What You'll Learn

- Building a REST API with FastAPI
- Handling webhooks (like getting WhatsApp messages)
- Working with environment variables
- Async programming in Python
- Professional logging practices
- API integration with WATI
- Testing with pytest

## 🛠️ Prerequisites

Before you start, make sure you have:
- Python 3.8 or newer installed (check with `python --version`)
- Basic Python knowledge (variables, functions, async/await)
- A WATI account (get one at [wati.io](https://wati.io))
- Your favorite code editor (VS Code recommended!)

## 📚 Quick Start Guide

### 1. Set Up Your Environment

```bash
# Clone the repository
git clone https://github.com/yourusername/wati-webhook-service.git
cd wati-webhook-service

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Create a `.env` file in the project root:

```env
WATI_API_KEY=your_api_key_here
WATI_ENDPOINT=https://your-instance.wati.io
WEBHOOK_SECRET=your_webhook_secret
```

### 3. Run the Service

```bash
uvicorn app.main:app --reload
```

Your service will be running at `http://localhost:8000`

### 4. Test the Webhook

- Use the FastAPI docs at `http://localhost:8000/docs`
- Or send a POST request to `http://localhost:8000/webhook`

## 📖 Documentation

Detailed documentation is available in the `/docs` folder:
- [API Reference](docs/api.md)
- [Configuration Guide](docs/configuration.md)
- [Testing Guide](docs/testing.md)

## 🧪 Running Tests

```bash
pytest
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to the WATI team for their excellent API
- FastAPI community for the amazing framework
- All contributors who help improve this project
```

I've added several key sections to complete the README:
1. Detailed setup instructions with code blocks
2. Environment configuration guide
3. Running instructions
4. Documentation section
5. Testing instructions
6. Contributing guidelines
7. License information
8. Acknowledgments

Each section uses emojis for visual appeal and follows markdown best practices with proper heading hierarchy and code block formatting. The instructions are clear and beginner-friendly, matching the project's stated purpose.