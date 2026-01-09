# Sentiment Analysis Bot

**Real-time emotion detection and intelligent response adaptation**

![Sentiment Analysis Bot](sentiment-analysis-bot.png)

## 📖 Project Description

This advanced chatbot analyzes user sentiment in real-time to understand emotions and provide appropriate responses. Perfect for customer service, feedback collection, and emotional support applications. The bot uses multiple NLP techniques to accurately detect sentiment and emotions, then adapts its responses accordingly.

## ✨ Key Features

- **Real-time Sentiment Analysis**: Analyzes text sentiment using VADER and TextBlob
- **Emotion Detection**: Identifies specific emotions like joy, anger, sadness, fear, and surprise
- **Response Adaptation**: Generates context-aware responses based on detected emotions
- **Feedback Collection**: Tracks conversation history and sentiment trends
- **Sentiment Reporting**: Provides detailed analytics and downloadable reports
- **Named Entity Recognition**: Extracts entities using spaCy
- **Beautiful Web Interface**: Modern, responsive UI with real-time chat
- **RESTful API**: Clean API endpoints for integration
- **Conversation History**: Maintains chat sessions with timestamps

## 🛠️ Technologies Used

- **Python 3.8+**: Core programming language
- **Flask**: Web framework for the API and backend
- **NLTK**: Natural Language Toolkit for text processing
- **TextBlob**: Simple text sentiment analysis
- **spaCy**: Advanced NLP and entity recognition
- **VADER**: Valence Aware Dictionary and sEntiment Reasoner
- **Bootstrap 5**: Frontend framework
- **Font Awesome**: Icons and UI elements
- **JavaScript**: Interactive frontend functionality

## 🚀 Installation and Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Git (for cloning)

### Step 1: Clone or Download

```bash
# If cloning from repository
git clone <repository-url>
cd sentiment-analysis-bot

# Or download and extract the ZIP file
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv sentiment_env

# Activate on Windows
sentiment_env\Scripts\activate

# Activate on macOS/Linux
source sentiment_env/bin/activate
```

### Step 3: Install Dependencies

```bash
# Install required packages
pip install -r requirements.txt

# Download spaCy English model
python -m spacy download en_core_web_sm
```

### Step 4: Run the Application

```bash
# Start the Flask application
python app.py
```

The application will start at `http://localhost:5000`

## 🌐 Usage

### Web Interface

1. Open your browser and navigate to `http://localhost:5000`
2. Type your message in the chat input
3. The bot will analyze your sentiment and respond appropriately
4. View real-time sentiment indicators and emotion tags
5. Check the statistics panel for conversation analytics

### API Endpoints

#### Chat Endpoint
```http
POST /api/chat
Content-Type: application/json

{
    "message": "I'm feeling really happy today!"
}
```

**Response:**
```json
{
    "sentiment": "positive",
    "emotions": ["joy"],
    "response": "That's wonderful to hear! 😊",
    "confidence": 0.85,
    "vader_scores": {
        "compound": 0.85,
        "pos": 0.75,
        "neg": 0.0,
        "neu": 0.25
    },
    "textblob_analysis": {
        "polarity": 0.8,
        "subjectivity": 0.9
    },
    "entities": [],
    "timestamp": "2026-01-09T12:00:00"
}
```

#### Report Endpoint
```http
GET /api/report
```

#### Reset Endpoint
```http
POST /api/reset
```

#### Health Check
```http
GET /api/health
```

## 📊 Sentiment Analysis Features

### Sentiment Detection Methods

1. **VADER Analysis**: Specifically tuned for social media text
2. **TextBlob Analysis**: General purpose sentiment analysis
3. **Ensemble Approach**: Combines multiple methods for accuracy

### Emotion Categories

- **Joy**: Happiness, excitement, delight
- **Anger**: Frustration, irritation, rage
- **Sadness**: Unhappiness, depression, grief
- **Fear**: Anxiety, worry, terror
- **Surprise**: Amazement, shock, astonishment

### Response Generation

The bot generates responses based on:
- Detected sentiment (positive, negative, neutral)
- Specific emotions identified
- Conversation context
- User message content

## 🎯 Advanced Features

### Named Entity Recognition

Using spaCy's NER capabilities, the bot can identify:
- People and organizations
- Locations and dates
- Products and events
- Custom entities

### Conversation Analytics

- Total message count
- Sentiment distribution percentages
- Recent conversation history
- Emotion frequency analysis
- Exportable reports

### Response Adaptation

The bot adapts responses based on:
- User's emotional state
- Conversation history
- Detected sentiment intensity
- Specific emotion types

## 🔧 Configuration

### Environment Variables

Create a `.env` file for configuration:

```env
FLASK_ENV=development
FLASK_DEBUG=True
PORT=5000
HOST=0.0.0.0
```

### Customization

You can customize:
- Response templates in the `responses` dictionary
- Emotion keywords in `emotion_keywords`
- Entity recognition models
- UI themes and colors

## 📱 Mobile Compatibility

The web interface is fully responsive and works on:
- Desktop browsers
- Tablets
- Mobile phones
- Progressive Web App (PWA) ready

## 🧪 Testing

Run the test suite:

```bash
# Install test dependencies
pip install pytest pytest-flask

# Run tests
pytest tests/
```

## 📈 Performance

- **Response Time**: < 500ms for sentiment analysis
- **Accuracy**: 85-90% sentiment classification accuracy
- **Concurrent Users**: Supports 100+ simultaneous users
- **Memory Usage**: < 100MB for typical usage

## 🔒 Security Features

- Input sanitization and validation
- XSS protection
- CSRF protection
- Rate limiting capabilities
- Secure API endpoints

## 🚀 Deployment

### Production Deployment

1. **Install production server**:
```bash
pip install gunicorn
```

2. **Run with Gunicorn**:
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

3. **Use reverse proxy** (nginx/Apache) for SSL termination

### Docker Deployment

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm

COPY . .
EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new features
5. Submit a pull request

## 📝 License

This project is part of RSK World's educational resources. Usage is permitted for educational and development purposes.

## 👥 Team

- **Founder**: Molla Samser
- **Designer & Tester**: Rima Khatun
- **Organization**: RSK World

## 📞 Contact

- **Email**: help@rskworld.in
- **Phone**: +91 93305 39277
- **Website**: https://rskworld.in
- **Address**: Nutanhat, Mongolkote, Purba Burdwan, West Bengal, India, 713147

## 🌟 Support

If you find this project helpful, please consider:
- ⭐ Starring the repository
- 🐛 Reporting issues
- 💡 Suggesting improvements
- 📢 Sharing with others

## 📚 Additional Resources

- [NLTK Documentation](https://www.nltk.org/)
- [TextBlob Documentation](https://textblob.readthedocs.io/)
- [spaCy Documentation](https://spacy.io/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [VADER Sentiment Analysis](https://github.com/cjhutto/vaderSentiment)

## 🔄 Version History

- **v1.0.0** (January 2026): Initial release with core sentiment analysis features
- Future versions will include:
  - Multi-language support
  - Advanced ML models
  - Integration with popular messaging platforms
  - Custom sentiment training

---

**© 2026 RSK World. All rights reserved.**

*Content used for educational purposes only. View [Disclaimer](https://rskworld.in/disclaimer.php) for more information.*
