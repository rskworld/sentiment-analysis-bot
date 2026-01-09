"""
Sentiment Analysis Bot Test Suite
Author: RSK World (https://rskworld.in)
Founded by: Molla Samser
Designer & Tester: Rima Khatun
Contact: help@rskworld.in, +91 93305 39277
Year: 2026
"""

import pytest
import json
from app import app, AdvancedSentimentAnalysisBot

@pytest.fixture
def client():
    """Create test client"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def bot():
    """Create bot instance for testing"""
    return AdvancedSentimentAnalysisBot()

class TestSentimentAnalysisBot:
    """Test the SentimentAnalysisBot class"""
    
    def test_bot_initialization(self, bot):
        """Test bot initialization"""
        assert bot.conversation_history == []
        assert bot.sentiment_stats['total'] == 0
        assert 'positive' in bot.responses
        assert 'negative' in bot.responses
        assert 'neutral' in bot.responses
    
    def test_preprocess_text(self, bot):
        """Test text preprocessing"""
        text = "Hello! How are you???   "
        processed = bot.preprocess_text(text)
        assert processed == "hello how are you"
        
        text_with_special = "Hello @world! #test $100"
        processed = bot.preprocess_text(text_with_special)
        assert processed == "hello world test 100"
    
    def test_analyze_sentiment_vader(self, bot):
        """Test VADER sentiment analysis"""
        positive_text = "I love this! It's amazing!"
        result = bot.analyze_sentiment_vader(positive_text)
        assert result['sentiment'] == 'positive'
        assert 'scores' in result
        assert 'confidence' in result
        
        negative_text = "I hate this! It's terrible!"
        result = bot.analyze_sentiment_vader(negative_text)
        assert result['sentiment'] == 'negative'
        
        neutral_text = "This is a book."
        result = bot.analyze_sentiment_vader(neutral_text)
        assert result['sentiment'] == 'neutral'
    
    def test_detect_emotions(self, bot):
        """Test emotion detection"""
        joy_text = "I am so happy and excited today!"
        emotions = bot.detect_emotions(joy_text)
        assert 'joy' in emotions
        
        anger_text = "I am very angry and frustrated!"
        emotions = bot.detect_emotions(anger_text)
        assert 'anger' in emotions
        
        sad_text = "I feel sad and depressed."
        emotions = bot.detect_emotions(sad_text)
        assert 'sadness' in emotions
    
    def test_generate_response(self, bot):
        """Test response generation"""
        sentiment_data = {'sentiment': 'positive'}
        emotions = ['joy']
        user_id = "test_user"
        response = bot.generate_contextual_response("test", sentiment_data, emotions, user_id)
        assert response is not None
        assert len(response) > 0
        
        # Test emotion-specific response
        joy_emotions = ['joy']
        response = bot.generate_contextual_response("test", sentiment_data, joy_emotions, user_id)
        assert response is not None
    
    def test_analyze_text_comprehensive(self, bot):
        """Test comprehensive text analysis"""
        text = "I am feeling very happy and excited today!"
        result = bot.advanced_analyze_text(text)
        
        assert 'sentiment' in result
        assert 'emotions' in result
        assert 'response' in result
        assert 'confidence' in result
        assert 'timestamp' in result
        assert result['sentiment'] == 'positive'
        assert 'joy' in result['emotions']
    
    def test_sentiment_report(self, bot):
        """Test sentiment report generation"""
        # Add some conversations
        bot.advanced_analyze_text("I am happy today!")
        bot.advanced_analyze_text("I am sad today!")
        bot.advanced_analyze_text("This is neutral.")
        
        report = bot.get_advanced_sentiment_report()
        assert report['total_conversations'] == 3
        assert report['raw_stats']['positive'] == 1
        assert report['raw_stats']['negative'] == 1
        assert report['raw_stats']['neutral'] == 1
        assert 'sentiment_distribution' in report
    
    def test_reset_conversation(self, bot):
        """Test conversation reset"""
        # Add conversation
        bot.advanced_analyze_text("Hello!")
        assert bot.sentiment_stats['total'] == 1
        
        # Reset
        bot.reset_conversation()
        assert bot.sentiment_stats['total'] == 0
        assert len(bot.conversation_history) == 0

class TestAPIEndpoints:
    """Test Flask API endpoints"""
    
    def test_health_check(self, client):
        """Test health check endpoint"""
        response = client.get('/api/health')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['status'] == 'healthy'
        assert 'timestamp' in data
    
    def test_chat_endpoint_valid_message(self, client):
        """Test chat endpoint with valid message"""
        response = client.post('/api/chat', 
                             json={'message': 'I am happy today!'},
                             content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'sentiment' in data
        assert 'response' in data
        assert 'emotions' in data
    
    def test_chat_endpoint_empty_message(self, client):
        """Test chat endpoint with empty message"""
        response = client.post('/api/chat', 
                             json={'message': ''},
                             content_type='application/json')
        assert response.status_code == 400
    
    def test_chat_endpoint_no_message(self, client):
        """Test chat endpoint without message"""
        response = client.post('/api/chat', 
                             json={},
                             content_type='application/json')
        assert response.status_code == 400
    
    def test_chat_endpoint_invalid_json(self, client):
        """Test chat endpoint with invalid JSON"""
        response = client.post('/api/chat', 
                             data='invalid json',
                             content_type='application/json')
        assert response.status_code == 400
    
    def test_report_endpoint(self, client):
        """Test report endpoint"""
        # First add some messages
        client.post('/api/chat', json={'message': 'I am happy!'})
        client.post('/api/chat', json={'message': 'I am sad!'})
        
        response = client.get('/api/report')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'total_conversations' in data
        assert 'sentiment_distribution' in data
    
    def test_reset_endpoint(self, client):
        """Test reset endpoint"""
        # Add a message first
        client.post('/api/chat', json={'message': 'Hello!'})
        
        # Reset
        response = client.post('/api/reset')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'message' in data
        
        # Check report is empty
        response = client.get('/api/report')
        data = json.loads(response.data)
        assert data['total_conversations'] == 0
    
    def test_index_page(self, client):
        """Test index page loads"""
        response = client.get('/')
        assert response.status_code == 200
        assert b'Sentiment Analysis Bot' in response.data

class TestEdgeCases:
    """Test edge cases and error handling"""
    
    def test_very_long_message(self, client):
        """Test very long message handling"""
        long_message = "This is a very long message. " * 100
        response = client.post('/api/chat', 
                             json={'message': long_message},
                             content_type='application/json')
        assert response.status_code == 200
    
    def test_unicode_message(self, client):
        """Test unicode characters"""
        unicode_message = "Hello 🌍! I'm feeling 😊 today!"
        response = client.post('/api/chat', 
                             json={'message': unicode_message},
                             content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'response' in data
    
    def test_mixed_sentiment(self, client):
        """Test mixed sentiment messages"""
        mixed_message = "I love the design but hate the color!"
        response = client.post('/api/chat', 
                             json={'message': mixed_message},
                             content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'sentiment' in data
    
    def test_question_message(self, client):
        """Test question handling"""
        question = "How are you feeling today?"
        response = client.post('/api/chat', 
                             json={'message': question},
                             content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'response' in data

class TestPerformance:
    """Test performance benchmarks"""
    
    def test_response_time(self, client):
        """Test API response time"""
        import time
        start_time = time.time()
        response = client.post('/api/chat', 
                             json={'message': 'I am happy today!'},
                             content_type='application/json')
        end_time = time.time()
        
        assert response.status_code == 200
        assert (end_time - start_time) < 2.0  # Should respond within 2 seconds
    
    def test_multiple_concurrent_requests(self, client):
        """Test multiple concurrent requests"""
        import threading
        import time
        
        results = []
        
        def make_request():
            response = client.post('/api/chat', 
                                 json={'message': 'Test message'},
                                 content_type='application/json')
            results.append(response.status_code)
        
        # Create 10 concurrent requests
        threads = []
        for _ in range(10):
            thread = threading.Thread(target=make_request)
            threads.append(thread)
            thread.start()
        
        # Wait for all threads to complete
        for thread in threads:
            thread.join()
        
        # All requests should succeed
        assert all(status == 200 for status in results)

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
