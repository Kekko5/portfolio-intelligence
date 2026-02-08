"""
Client per l'API Claude di Anthropic.
"""
import os
from anthropic import Anthropic
from dotenv import load_dotenv

# Carica variabili da .env
load_dotenv()


class AIClient:
    """
    Client wrapper per Claude API.
    """
    
    def __init__(self, model: str = "claude-sonnet-4-20250514"):
        """
        Args:
            model: Modello Claude da usare
        """
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY non trovata. Crea un file .env con la key.")
        
        self.client = Anthropic(api_key=api_key)
        self.model = model
    
    def ask(self, prompt: str, system_prompt: str = None, max_tokens: int = 1024) -> str:
        """
        Invia una richiesta a Claude.
        
        Args:
            prompt: Il messaggio da inviare
            system_prompt: Istruzioni di sistema (opzionale)
            max_tokens: Massimo numero di token nella risposta
        
        Returns:
            La risposta di Claude come stringa
        """
        messages = [{"role": "user", "content": prompt}]
        
        kwargs = {
            "model": self.model,
            "max_tokens": max_tokens,
            "messages": messages,
        }
        
        if system_prompt:
            kwargs["system"] = system_prompt
        
        response = self.client.messages.create(**kwargs)
        
        return response.content[0].text