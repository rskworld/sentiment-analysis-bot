#!/usr/bin/env python3
"""
Sentiment Analysis Bot - Real-time emotion detection and response adaptation
Author: RSK World (https://rskworld.in)
Founded by: Molla Samser
Designer & Tester: Rima Khatun
Contact: help@rskworld.in, +91 93305 39277
Year: 2026
"""

import nltk
import spacy
import json
import random
import os
from datetime import datetime, timedelta
from textblob import TextBlob
from flask import Flask, request, jsonify, render_template, session
from flask_cors import CORS
from collections import defaultdict, Counter
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import hashlib

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'sentiment-bot-secret-key-2026')
CORS(app)

# Initialize sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Load spaCy model (try english, fallback to basic)
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Warning: spaCy English model not found. Using basic text processing.")
    nlp = None

class AdvancedSentimentAnalysisBot:
    """
    Advanced sentiment analysis bot with cutting-edge features:
    - Multi-modal sentiment analysis
    - Context-aware conversations
    - Personality detection
    - Emotional intelligence
    - Predictive analytics
    - User profiling
    - Advanced NLP capabilities
    """
    
    def __init__(self):
        self.conversation_history = []
        self.sentiment_stats = {
            'positive': 0,
            'negative': 0,
            'neutral': 0,
            'total': 0
        }
        
        # Advanced features initialization
        self.user_profiles = {}
        self.conversation_contexts = {}
        self.emotion_patterns = defaultdict(list)
        self.response_templates = self._load_advanced_response_templates()
        self.personality_traits = {}
        self.tfidf_vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
        self.conversation_vectors = []
        self.conversation_texts = []
        
        # Emotional intelligence features
        self.emotional_state_tracker = {}
        self.empathy_level = 0.5
        self.personalization_enabled = True
        
        # Predictive analytics
        self.sentiment_trends = []
        self.user_satisfaction_scores = {}
        self.predictive_models = {}
        
        # Advanced response system
        self.context_memory = defaultdict(list)
        self.personality_adaptation = {}
        self.emotional_contagion_detector = True
        
        # Response templates based on sentiment
        self.responses = {
            'positive': [
                "That's wonderful to hear! 😊",
                "I'm glad you're feeling positive!",
                "Great! Your positive energy is contagious!",
                "Fantastic! Keep up the great mood!",
                "That's amazing! I love hearing good news!"
            ],
            'negative': [
                "I understand you're feeling down. I'm here to help. 💙",
                "I'm sorry to hear that. Would you like to talk about it?",
                "That sounds difficult. Remember, tough times don't last.",
                "I hear your frustration. Let's work through this together.",
                "That sounds challenging. Remember to take care of yourself."
            ],
            'neutral': [
                "I see. Tell me more about that.",
                "Interesting! Could you elaborate?",
                "Thanks for sharing. What are your thoughts on this?",
                "I understand. How does this make you feel?",
                "Got it. What would you like to discuss next?"
            ]
        }
        
        # Emotion-specific responses
        self.emotion_responses = {
            'joy': ["That's pure joy! 🎉", "Your happiness is wonderful!", "What a delightful feeling!"],
            'anger': ["I understand your frustration. Let's take a breath.", "That sounds infuriating. I'm here to listen.", "Your anger is valid. Let's work through it."],
            'sadness': ["I'm sorry you're feeling this way. 💙", "That sounds heartbreaking. I'm here for you.", "Your sadness is valid. Remember, it's okay to feel."],
            'fear': ["That sounds scary. You're safe here.", "I understand your fear. Let's face it together.", "That's concerning. Let's break it down."],
            'surprise': ["Wow! That must have been unexpected!", "What a surprise! Tell me more.", "That's astonishing! What happened next?"]
        }
    
    def _load_advanced_response_templates(self):
        """Load advanced response templates organized by sentiment and emotion"""
        return {
            'positive': {
                'default': [
                    "That's wonderful to hear! 😊",
                    "I'm glad you're feeling positive!",
                    "Great! Your positive energy is contagious!",
                    "Fantastic! Keep up the great mood!",
                    "That's amazing! I love hearing good news!"
                ],
                'joy': ["That's pure joy! 🎉", "Your happiness is wonderful!", "What a delightful feeling!"],
                'surprise': ["Wow! That must have been unexpected!", "What a surprise! Tell me more.", "That's astonishing!"]
            },
            'negative': {
                'default': [
                    "I understand you're feeling down. I'm here to help. 💙",
                    "I'm sorry to hear that. Would you like to talk about it?",
                    "That sounds difficult. Remember, tough times don't last.",
                    "I hear your frustration. Let's work through this together.",
                    "That sounds challenging. Remember to take care of yourself."
                ],
                'anger': ["I understand your frustration. Let's take a breath.", "That sounds infuriating. I'm here to listen.", "Your anger is valid. Let's work through it."],
                'sadness': ["I'm sorry you're feeling this way. 💙", "That sounds heartbreaking. I'm here for you.", "Your sadness is valid. Remember, it's okay to feel."],
                'fear': ["That sounds scary. You're safe here.", "I understand your fear. Let's face it together.", "That's concerning. Let's break it down."]
            },
            'neutral': {
                'default': [
                    "I see. Tell me more about that.",
                    "Interesting! Could you elaborate?",
                    "Thanks for sharing. What are your thoughts on this?",
                    "I understand. How does this make you feel?",
                    "Got it. What would you like to discuss next?"
                ]
            }
        }
    
    def preprocess_text(self, text):
        """Clean and preprocess text for analysis"""
        # Remove special characters and extra whitespace
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text.lower()
    
    def analyze_sentiment_vader(self, text):
        """Analyze sentiment using VADER"""
        scores = sid.polarity_scores(text)
        
        if scores['compound'] >= 0.05:
            sentiment = 'positive'
        elif scores['compound'] <= -0.05:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
            
        return {
            'sentiment': sentiment,
            'scores': scores,
            'confidence': abs(scores['compound'])
        }
    
    def analyze_sentiment_textblob(self, text):
        """Analyze sentiment using TextBlob"""
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        
        if polarity > 0.1:
            sentiment = 'positive'
        elif polarity < -0.1:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
            
        return {
            'sentiment': sentiment,
            'polarity': polarity,
            'subjectivity': blob.sentiment.subjectivity
        }
    
    def detect_emotions(self, text):
        """Detect specific emotions based on keywords and context"""
        emotions = []
        text_lower = text.lower()
        
        # Emotion keyword mapping
        emotion_keywords = {
            'joy': ['happy', 'excited', 'wonderful', 'amazing', 'fantastic', 'great', 'love', 'awesome', 'delighted'],
            'anger': ['angry', 'mad', 'furious', 'annoyed', 'frustrated', 'irritated', 'upset', 'rage'],
            'sadness': ['sad', 'depressed', 'unhappy', 'miserable', 'heartbroken', 'devastated', 'crying'],
            'fear': ['scared', 'afraid', 'terrified', 'worried', 'anxious', 'nervous', 'panic'],
            'surprise': ['surprised', 'shocked', 'amazed', 'astonished', 'unexpected', 'wow']
        }
        
        for emotion, keywords in emotion_keywords.items():
            if any(keyword in text_lower for keyword in keywords):
                emotions.append(emotion)
        
        return emotions if emotions else ['neutral']
    
    def extract_entities(self, text):
        """Extract named entities using spaCy"""
        if not nlp:
            return []
            
        doc = nlp(text)
        entities = []
        
        for ent in doc.ents:
            entities.append({
                'text': ent.text,
                'label': ent.label_,
                'description': spacy.explain(ent.label_)
            })
        
        return entities
    
    def detect_personality_traits(self, text, user_id=None):
        """Advanced personality detection based on linguistic patterns"""
        if not user_id:
            user_id = "default"
        
        # Personality indicators
        personality_indicators = {
            'openness': ['creative', 'innovative', 'artistic', 'curious', 'imaginative', 'adventurous'],
            'conscientiousness': ['organized', 'disciplined', 'responsible', 'careful', 'thorough', 'meticulous'],
            'extraversion': ['social', 'outgoing', 'energetic', 'talkative', 'enthusiastic', 'bold'],
            'agreeableness': ['cooperative', 'friendly', 'compassionate', 'helpful', 'kind', 'supportive'],
            'neuroticism': ['anxious', 'moody', 'irritable', 'worried', 'nervous', 'stress']
        }
        
        text_lower = text.lower()
        detected_traits = {}
        
        for trait, indicators in personality_indicators.items():
            score = sum(1 for indicator in indicators if indicator in text_lower)
            detected_traits[trait] = min(score / len(indicators), 1.0)
        
        # Update user personality profile
        if user_id not in self.personality_traits:
            self.personality_traits[user_id] = {}
        
        for trait, score in detected_traits.items():
            if trait in self.personality_traits[user_id]:
                # Weighted average with previous scores
                self.personality_traits[user_id][trait] = (
                    self.personality_traits[user_id][trait] * 0.7 + score * 0.3
                )
            else:
                self.personality_traits[user_id][trait] = score
        
        return detected_traits
    
    def analyze_emotional_contagion(self, current_emotions, user_id=None):
        """Detect emotional contagion patterns in conversations"""
        if not user_id or user_id not in self.emotional_state_tracker:
            return {'contagion_detected': False, 'contagion_type': None}
        
        previous_emotional_state = self.emotional_state_tracker[user_id][-5:]  # Last 5 emotions
        if len(previous_emotional_state) < 3:
            return {'contagion_detected': False, 'contagion_type': None}
        
        # Analyze emotional patterns
        emotion_frequency = Counter([e['emotion'] for e in previous_emotional_state])
        dominant_emotion = emotion_frequency.most_common(1)[0][0]
        
        # Check if current emotions show contagion
        contagion_detected = dominant_emotion in current_emotions
        
        return {
            'contagion_detected': contagion_detected,
            'contagion_type': dominant_emotion if contagion_detected else None,
            'emotion_frequency': dict(emotion_frequency)
        }
    
    def predict_user_satisfaction(self, user_id=None):
        """Predict user satisfaction based on conversation patterns"""
        if not user_id or user_id not in self.user_profiles:
            return {'satisfaction_score': 0.5, 'confidence': 0.0}
        
        profile = self.user_profiles[user_id]
        recent_conversations = profile.get('conversations', [])[-10:]
        
        if len(recent_conversations) < 3:
            return {'satisfaction_score': 0.5, 'confidence': 0.0}
        
        # Calculate satisfaction metrics
        positive_ratio = sum(1 for c in recent_conversations if c['sentiment'] == 'positive') / len(recent_conversations)
        response_engagement = sum(1 for c in recent_conversations if len(c['user_input']) > 10) / len(recent_conversations)
        emotional_diversity = len(set([e for c in recent_conversations for e in c['emotions']])) / 5.0
        
        # Weighted satisfaction score
        satisfaction_score = (positive_ratio * 0.5 + response_engagement * 0.3 + emotional_diversity * 0.2)
        confidence = min(len(recent_conversations) / 10.0, 1.0)
        
        return {
            'satisfaction_score': satisfaction_score,
            'confidence': confidence,
            'factors': {
                'positive_ratio': positive_ratio,
                'engagement': response_engagement,
                'diversity': emotional_diversity
            }
        }
    
    def generate_contextual_response(self, user_input, sentiment_data, emotions, user_id=None):
        """Generate advanced contextual responses with emotional intelligence"""
        if not user_id:
            user_id = "default"
        
        # Detect personality traits
        personality = self.detect_personality_traits(user_input, user_id)
        
        # Analyze emotional contagion
        contagion = self.analyze_emotional_contagion(emotions, user_id)
        
        # Get base sentiment
        sentiment = sentiment_data['sentiment']
        
        # Select appropriate response template
        if sentiment in self.response_templates:
            # Find best matching emotion template
            best_emotion = 'default'
            for emotion in emotions:
                if emotion in self.response_templates[sentiment]:
                    best_emotion = emotion
                    break
            
            response_pool = self.response_templates[sentiment].get(best_emotion, 
                                                                 self.response_templates[sentiment]['default'])
        else:
            response_pool = self.response_templates['neutral']['default']
        
        # Personalize response based on personality
        if self.personalization_enabled and user_id in self.personality_traits:
            user_personality = self.personality_traits[user_id]
            
            # Adapt response based on dominant personality traits
            if user_personality.get('extraversion', 0) > 0.6:
                response_pool = [r + " I'd love to hear more about your experience!" for r in response_pool]
            elif user_personality.get('openness', 0) > 0.6:
                response_pool = [r + " This opens up some interesting possibilities!" for r in response_pool]
            elif user_personality.get('agreeableness', 0) > 0.6:
                response_pool = [r + " I'm here to support you every step of the way." for r in response_pool]
        
        # Add emotional contagion awareness
        if contagion['contagion_detected']:
            response_pool = [r + f" I notice you've been feeling {contagion['contagion_type']} lately - I'm here to help." 
                           for r in response_pool]
        
        return random.choice(response_pool)
    
    def advanced_analyze_text(self, text, user_id=None):
        """Comprehensive advanced text analysis with all features"""
        if not user_id:
            user_id = "default_" + hashlib.md5(text.encode()).hexdigest()[:8]
        
        processed_text = self.preprocess_text(text)
        
        # Basic sentiment analysis
        vader_result = self.analyze_sentiment_vader(text)
        textblob_result = self.analyze_sentiment_textblob(text)
        
        # Advanced emotion detection
        emotions = self.detect_emotions(text)
        
        # Entity extraction
        entities = self.extract_entities(text)
        
        # Personality analysis
        personality = self.detect_personality_traits(text, user_id)
        
        # Contextual response generation
        response = self.generate_contextual_response(text, vader_result, emotions, user_id)
        
        # Update conversation vectors for similarity analysis
        if len(self.conversation_texts) == 0:
            self.conversation_vectors = self.tfidf_vectorizer.fit_transform([processed_text])
        else:
            new_vector = self.tfidf_vectorizer.transform([processed_text])
            self.conversation_vectors = np.vstack([self.conversation_vectors, new_vector])
        
        self.conversation_texts.append(processed_text)
        
        # Track emotional state
        if user_id not in self.emotional_state_tracker:
            self.emotional_state_tracker[user_id] = []
        
        self.emotional_state_tracker[user_id].append({
            'timestamp': datetime.now(),
            'emotion': emotions[0] if emotions else 'neutral',
            'sentiment': vader_result['sentiment'],
            'intensity': vader_result['confidence']
        })
        
        # Update user profile
        if user_id not in self.user_profiles:
            self.user_profiles[user_id] = {
                'conversations': [],
                'first_interaction': datetime.now(),
                'total_messages': 0
            }
        
        self.user_profiles[user_id]['conversations'].append({
            'timestamp': datetime.now().isoformat(),
            'user_input': text,
            'sentiment': vader_result['sentiment'],
            'emotions': emotions,
            'response': response,
            'personality_traits': personality
        })
        self.user_profiles[user_id]['total_messages'] += 1
        
        # Update statistics
        self.sentiment_stats[vader_result['sentiment']] += 1
        self.sentiment_stats['total'] += 1
        
        # Store conversation
        conversation_entry = {
            'timestamp': datetime.now().isoformat(),
            'user_id': user_id,
            'user_input': text,
            'sentiment': vader_result['sentiment'],
            'emotions': emotions,
            'response': response,
            'vader_scores': vader_result['scores'],
            'textblob_polarity': textblob_result['polarity'],
            'personality_traits': personality,
            'entities': entities,
            'advanced_features': {
                'emotional_contagion': self.analyze_emotional_contagion(emotions, user_id),
                'predicted_satisfaction': self.predict_user_satisfaction(user_id)
            }
        }
        
        self.conversation_history.append(conversation_entry)
        
        return {
            'sentiment': vader_result['sentiment'],
            'emotions': emotions,
            'response': response,
            'confidence': vader_result['confidence'],
            'vader_scores': vader_result['scores'],
            'textblob_analysis': textblob_result,
            'entities': entities,
            'personality_traits': personality,
            'user_id': user_id,
            'timestamp': conversation_entry['timestamp'],
            'advanced_features': conversation_entry['advanced_features']
        }
    
    def get_advanced_sentiment_report(self, user_id=None):
        """Generate comprehensive sentiment analysis report with advanced features"""
        if self.sentiment_stats['total'] == 0:
            return {'message': 'No conversations yet'}
        
        percentages = {}
        for sentiment in ['positive', 'negative', 'neutral']:
            percentages[sentiment] = (
                self.sentiment_stats[sentiment] / self.sentiment_stats['total']
            ) * 100
        
        base_report = {
            'total_conversations': self.sentiment_stats['total'],
            'sentiment_distribution': percentages,
            'raw_stats': self.sentiment_stats,
            'recent_conversations': self.conversation_history[-10:] if self.conversation_history else []
        }
        
        # Add advanced features
        advanced_report = {
            **base_report,
            'user_profiles': len(self.user_profiles),
            'personality_analysis': self._get_personality_summary(),
            'emotional_contagion_stats': self._get_contagion_stats(),
            'satisfaction_metrics': self._get_satisfaction_metrics(),
            'conversation_patterns': self._analyze_conversation_patterns(),
            'entity_analysis': self._get_entity_summary()
        }
        
        # Add user-specific data if requested
        if user_id and user_id in self.user_profiles:
            advanced_report['user_specific'] = {
                'total_messages': self.user_profiles[user_id]['total_messages'],
                'personality_profile': self.personality_traits.get(user_id, {}),
                'satisfaction_prediction': self.predict_user_satisfaction(user_id),
                'emotional_timeline': self.emotional_state_tracker.get(user_id, [])[-10:]
            }
        
        return advanced_report
    
    def _get_personality_summary(self):
        """Get overall personality analysis summary"""
        if not self.personality_traits:
            return {}
        
        personality_summary = {}
        for trait in ['openness', 'conscientiousness', 'extraversion', 'agreeableness', 'neuroticism']:
            scores = [user_traits.get(trait, 0) for user_traits in self.personality_traits.values()]
            personality_summary[trait] = {
                'average': np.mean(scores),
                'min': np.min(scores),
                'max': np.max(scores),
                'distribution': np.histogram(scores, bins=5, range=(0,1))[0].tolist()
            }
        
        return personality_summary
    
    def _get_contagion_stats(self):
        """Get emotional contagion statistics"""
        contagion_stats = {
            'total_contagion_detected': 0,
            'contagion_types': Counter(),
            'contagion_rate': 0.0
        }
        
        for conversation in self.conversation_history:
            if 'advanced_features' in conversation:
                contagion_data = conversation['advanced_features'].get('emotional_contagion', {})
                if contagion_data.get('contagion_detected', False):
                    contagion_stats['total_contagion_detected'] += 1
                    contagion_type = contagion_data.get('contagion_type')
                    if contagion_type:
                        contagion_stats['contagion_types'][contagion_type] += 1
        
        if self.sentiment_stats['total'] > 0:
            contagion_stats['contagion_rate'] = contagion_stats['total_contagion_detected'] / self.sentiment_stats['total']
        
        return contagion_stats
    
    def _get_satisfaction_metrics(self):
        """Get overall satisfaction metrics"""
        if not self.user_profiles:
            return {}
        
        satisfaction_scores = []
        for user_id in self.user_profiles:
            prediction = self.predict_user_satisfaction(user_id)
            if prediction['confidence'] > 0.3:  # Only include confident predictions
                satisfaction_scores.append(prediction['satisfaction_score'])
        
        if not satisfaction_scores:
            return {}
        
        return {
            'average_satisfaction': np.mean(satisfaction_scores),
            'satisfaction_distribution': np.histogram(satisfaction_scores, bins=5, range=(0,1))[0].tolist(),
            'high_satisfaction_rate': sum(1 for s in satisfaction_scores if s > 0.7) / len(satisfaction_scores),
            'low_satisfaction_rate': sum(1 for s in satisfaction_scores if s < 0.3) / len(satisfaction_scores)
        }
    
    def _analyze_conversation_patterns(self):
        """Analyze conversation patterns and trends"""
        if len(self.conversation_history) < 5:
            return {}
        
        # Time-based analysis
        timestamps = []
        for c in self.conversation_history:
            try:
                if isinstance(c['timestamp'], str):
                    timestamps.append(datetime.fromisoformat(c['timestamp']))
                elif isinstance(c['timestamp'], datetime):
                    timestamps.append(c['timestamp'])
            except (ValueError, TypeError):
                # Skip invalid timestamps
                continue
        hourly_distribution = Counter([ts.hour for ts in timestamps])
        
        # Message length analysis
        message_lengths = [len(c['user_input']) for c in self.conversation_history]
        
        # Sentiment trends over time
        sentiment_timeline = []
        for i, conversation in enumerate(self.conversation_history[-20:]):  # Last 20 conversations
            try:
                sentiment_timeline.append({
                    'index': i,
                    'sentiment': conversation.get('sentiment', 'neutral'),
                    'confidence': conversation.get('confidence', 0),
                    'timestamp': conversation.get('timestamp', datetime.now().isoformat())
                })
            except (KeyError, TypeError):
                # Skip invalid conversation entries
                continue
        
        # Calculate conversation velocity safely
        conversation_velocity = 0.0
        if len(timestamps) >= 2:
            try:
                time_diff = (max(timestamps) - min(timestamps)).total_seconds() / 3600
                if time_diff > 0:
                    conversation_velocity = len(self.conversation_history) / time_diff
            except (ValueError, TypeError):
                pass
        
        return {
            'hourly_activity': dict(hourly_distribution),
            'average_message_length': np.mean(message_lengths) if message_lengths else 0,
            'message_length_std': np.std(message_lengths) if message_lengths else 0,
            'sentiment_timeline': sentiment_timeline,
            'conversation_velocity': conversation_velocity  # conversations per hour
        }
    
    def _get_entity_summary(self):
        """Get summary of extracted entities"""
        all_entities = []
        for conversation in self.conversation_history:
            all_entities.extend(conversation.get('entities', []))
        
        if not all_entities:
            return {}
        
        entity_types = Counter([entity['label'] for entity in all_entities])
        unique_entities = Counter([entity['text'].lower() for entity in all_entities])
        
        return {
            'total_entities': len(all_entities),
            'entity_types': dict(entity_types),
            'most_common_entities': unique_entities.most_common(10),
            'entity_diversity': len(unique_entities) / max(1, len(all_entities))
        }
    
    def reset_conversation(self):
        """Reset conversation history and stats"""
        self.conversation_history = []
        self.sentiment_stats = {
            'positive': 0,
            'negative': 0,
            'neutral': 0,
            'total': 0
        }

# Initialize advanced bot
bot = AdvancedSentimentAnalysisBot()

@app.route('/')
def index():
    """Main chatbot interface"""
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """Advanced chat API endpoint with user tracking"""
    try:
        if not request.is_json:
            return jsonify({'error': 'Content-Type must be application/json'}), 400
        
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid JSON data'}), 400
        
        user_message = data.get('message', '')
        user_id = data.get('user_id', None)
        
        if not user_id:
            # Generate or get user ID from session
            if 'user_id' not in session:
                session['user_id'] = f"user_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{hash(user_message[:10]) % 10000}"
            user_id = session['user_id']
        
        if not user_message or not user_message.strip():
            return jsonify({'error': 'Empty message'}), 400
        
        # Validate message length
        if len(user_message) > 1000:
            return jsonify({'error': 'Message too long (max 1000 characters)'}), 400
        
        # Use advanced analysis
        result = bot.advanced_analyze_text(user_message, user_id)
        return jsonify(result)
        
    except KeyError as e:
        return jsonify({'error': f'Missing required field: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/report', methods=['GET'])
def get_report():
    """Get advanced sentiment analysis report"""
    try:
        user_id = request.args.get('user_id', None)
        # Validate user_id if provided
        if user_id and not user_id.strip():
            user_id = None
        
        report = bot.get_advanced_sentiment_report(user_id)
        return jsonify(report)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/user-profile/<user_id>', methods=['GET'])
def get_user_profile(user_id):
    """Get detailed user profile"""
    try:
        if not user_id or user_id not in bot.user_profiles:
            return jsonify({'error': 'User not found'}), 404
        
        user_profile = bot.user_profiles[user_id]
        first_interaction = user_profile.get('first_interaction')
        
        profile = {
            'user_id': user_id,
            'total_messages': user_profile.get('total_messages', 0),
            'first_interaction': first_interaction.isoformat() if isinstance(first_interaction, datetime) else str(first_interaction),
            'personality_traits': bot.personality_traits.get(user_id, {}),
            'satisfaction_prediction': bot.predict_user_satisfaction(user_id),
            'emotional_timeline': bot.emotional_state_tracker.get(user_id, [])[-10:],
            'recent_conversations': user_profile.get('conversations', [])[-5:]
        }
        
        return jsonify(profile)
    except KeyError as e:
        return jsonify({'error': f'User data incomplete: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/personality-analysis', methods=['POST'])
def analyze_personality():
    """Analyze personality from text"""
    try:
        if not request.is_json:
            return jsonify({'error': 'Content-Type must be application/json'}), 400
        
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid JSON data'}), 400
        
        text = data.get('text', '')
        user_id = data.get('user_id', None)
        
        if not text or not text.strip():
            return jsonify({'error': 'Empty text'}), 400
        
        if len(text) > 1000:
            return jsonify({'error': 'Text too long (max 1000 characters)'}), 400
        
        personality = bot.detect_personality_traits(text, user_id)
        return jsonify({
            'personality_traits': personality,
            'text_length': len(text),
            'analysis_timestamp': datetime.now().isoformat()
        })
    except KeyError as e:
        return jsonify({'error': f'Missing required field: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/emotional-contagion', methods=['POST'])
def check_emotional_contagion():
    """Check for emotional contagion patterns"""
    try:
        if not request.is_json:
            return jsonify({'error': 'Content-Type must be application/json'}), 400
        
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid JSON data'}), 400
        
        emotions = data.get('emotions', [])
        user_id = data.get('user_id', None)
        
        if not emotions or not isinstance(emotions, list):
            return jsonify({'error': 'No emotions provided or invalid format (must be a list)'}), 400
        
        contagion = bot.analyze_emotional_contagion(emotions, user_id)
        return jsonify(contagion)
    except KeyError as e:
        return jsonify({'error': f'Missing required field: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/satisfaction-prediction/<user_id>', methods=['GET'])
def get_satisfaction_prediction(user_id):
    """Get satisfaction prediction for user"""
    try:
        if not user_id or not user_id.strip():
            return jsonify({'error': 'Invalid user_id'}), 400
        
        prediction = bot.predict_user_satisfaction(user_id)
        return jsonify(prediction)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/conversation-similarity', methods=['POST'])
def get_conversation_similarity():
    """Find similar conversations using TF-IDF"""
    try:
        if not request.is_json:
            return jsonify({'error': 'Content-Type must be application/json'}), 400
        
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid JSON data'}), 400
        
        text = data.get('text', '')
        top_k = data.get('top_k', 5)
        
        if not text or not text.strip():
            return jsonify({'error': 'Empty text'}), 400
        
        if len(text) > 1000:
            return jsonify({'error': 'Text too long (max 1000 characters)'}), 400
        
        if len(bot.conversation_texts) == 0:
            return jsonify({'similar_conversations': []})
        
        # Validate top_k
        top_k = max(1, min(int(top_k), 20))  # Limit between 1 and 20
        
        # Vectorize new text
        text_vector = bot.tfidf_vectorizer.transform([bot.preprocess_text(text)])
        
        # Calculate similarities
        similarities = cosine_similarity(text_vector, bot.conversation_vectors).flatten()
        
        # Get top similar conversations
        top_indices = similarities.argsort()[-top_k:][::-1]
        
        similar_conversations = []
        for idx in top_indices:
            if similarities[idx] > 0.1:  # Threshold for similarity
                try:
                    original_conv = bot.conversation_history[idx]
                    similar_conversations.append({
                        'similarity_score': float(similarities[idx]),
                        'original_text': original_conv.get('user_input', ''),
                        'sentiment': original_conv.get('sentiment', 'neutral'),
                        'response': original_conv.get('response', ''),
                        'timestamp': original_conv.get('timestamp', datetime.now().isoformat())
                    })
                except (IndexError, KeyError):
                    continue
        
        return jsonify({'similar_conversations': similar_conversations})
    except (ValueError, TypeError) as e:
        return jsonify({'error': f'Invalid parameter: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/reset', methods=['POST'])
def reset_chat():
    """Reset conversation and user data"""
    try:
        # Handle both JSON and form data
        data = {}
        if request.is_json:
            data = request.get_json() or {}
        elif request.form:
            data = request.form.to_dict()
        
        user_id = data.get('user_id', None)
        
        if user_id and user_id.strip() and user_id in bot.user_profiles:
            # Reset specific user data
            try:
                del bot.user_profiles[user_id]
            except KeyError:
                pass
            try:
                if user_id in bot.personality_traits:
                    del bot.personality_traits[user_id]
            except KeyError:
                pass
            try:
                if user_id in bot.emotional_state_tracker:
                    del bot.emotional_state_tracker[user_id]
            except KeyError:
                pass
            
            # Remove user's conversations from history
            bot.conversation_history = [c for c in bot.conversation_history if c.get('user_id') != user_id]
        else:
            # Reset all data
            bot.reset_conversation()
            bot.user_profiles = {}
            bot.personality_traits = {}
            bot.emotional_state_tracker = {}
            bot.conversation_vectors = []
            bot.conversation_texts = []
        
        # Recalculate stats safely
        bot.sentiment_stats = {'positive': 0, 'negative': 0, 'neutral': 0, 'total': 0}
        for conv in bot.conversation_history:
            sentiment = conv.get('sentiment', 'neutral')
            if sentiment in bot.sentiment_stats:
                bot.sentiment_stats[sentiment] += 1
            bot.sentiment_stats['total'] += 1
        
        return jsonify({'message': 'Conversation reset successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Advanced health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '2.0.0',
        'features': {
            'advanced_sentiment_analysis': True,
            'personality_detection': True,
            'emotional_contagion': True,
            'user_profiling': True,
            'satisfaction_prediction': True,
            'conversation_similarity': True
        },
        'statistics': {
            'total_conversations': bot.sentiment_stats['total'],
            'unique_users': len(bot.user_profiles),
            'active_features': len(bot.personality_traits)
        }
    })

if __name__ == '__main__':
    print("🤖 ADVANCED Sentiment Analysis Bot Starting...")
    print("🚀 Version 2.0 - Cutting-Edge Features")
    print("📊 Core Features: Real-time sentiment analysis, emotion detection, response adaptation")
    print("🧠 Advanced AI: Personality detection, emotional contagion, user profiling")
    print("🔮 Predictive Analytics: Satisfaction prediction, conversation patterns")
    print("🌐 Web Interface: http://localhost:5000")
    print("📈 Enhanced API Endpoints:")
    print("   • /api/chat - Advanced chat with user tracking")
    print("   • /api/user-profile/<id> - Detailed user profiles")
    print("   • /api/personality-analysis - Personality detection")
    print("   • /api/emotional-contagion - Emotional pattern analysis")
    print("   • /api/satisfaction-prediction/<id> - User satisfaction metrics")
    print("   • /api/conversation-similarity - Similar conversation finder")
    print("   • /api/report - Comprehensive analytics dashboard")
    print("👤 Created by RSK World (https://rskworld.in)")
    print("📞 Contact: help@rskworld.in | +91 93305 39277")
    print("👨‍💻 Founder: Molla Samser")
    print("👩‍💻 Designer & Tester: Rima Khatun")
    print("📅 Year: 2026")
    print("📍 Nutanhat, Mongolkote, Purba Burdwan, West Bengal, India")
    print("=" * 60)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
