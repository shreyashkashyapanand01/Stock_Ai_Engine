import logging
import os
from groq import Groq
from app.tools.news_tool import fetch_news
from app.config import llm_model

logger = logging.getLogger(__name__)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def get_news_sentiment(symbol: str):
    logger.info(f"sentiment_analyzer: Analyzing sentiment for {symbol}")

    try:
        headlines = fetch_news(symbol)

        if not headlines:
            return {
                "sentiment": "Neutral",
                "confidence": 0.5,
                "headlines": []
            }

        prompt = f"""
        Analyze the sentiment of the following news headlines for stock {symbol}.

        Headlines:
        {headlines}

        Return ONLY in JSON format:
        {{
            "sentiment": "Bullish | Bearish | Neutral",
            "confidence": 0 to 1
        }}
        """

        response = client.chat.completions.create(
            model=llm_model,
            messages=[
                {"role": "system", "content": "You are a financial sentiment analysis AI."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )

        content = response.choices[0].message.content.strip()

        import json
        #parsed = json.loads(content)
        import re
        json_str = re.search(r"\{.*\}", content, re.DOTALL).group()
        parsed = json.loads(json_str)

        return {
            "sentiment": parsed.get("sentiment", "Neutral"),
            "confidence": round(float(parsed.get("confidence", 0.5)), 2),
            "headlines": headlines
        }

    except Exception as e:
        logger.error(f"sentiment_analyzer: Failed for {symbol} - {str(e)}")
        return {
            "sentiment": "Neutral",
            "confidence": 0.5,
            "headlines": []
        }