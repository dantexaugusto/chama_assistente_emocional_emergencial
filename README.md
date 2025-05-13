# Chama: A Compassionate Emotional Support Chatbot

## Overview
Chama is a free and open-source emotional support chatbot designed to offer compassionate and empathetic presence to users in moments of deep emotional distress. Focused on suicide prevention and emotional crisis support, Chama provides a safe space for users to express their feelings without judgment.

## Features
- **Empathetic Conversation:** Provides gentle, non-judgmental, and supportive responses
- **Telegram Integration:** Accessible through Telegram at [t.me/assistente_chama_bot](https://t.me/assistente_chama_bot)
- **Persistent Conversation History:** Maintains conversation context across sessions
- **Multi-user Support:** Handles multiple users simultaneously with individual conversation tracking
- **Professional Resources:** Offers resource links to professional help when appropriate

## Files Overview
- **behaviour_prompt.txt & behaviour_prompt_I.txt:** Define the chatbot's persona, instructions, and response guidelines
- **chama_birth.py:** Core module that manages the conversational AI integration and conversation history
- **main_app_telegramAPI_module.py:** Telegram bot integration for message handling
- **usrids_conversation_state.json:** Stores user conversation histories across sessions
- **requirements.txt:** Lists required Python packages for the project

## Getting Started

### Prerequisites
- Python 3.x
- OpenAI API key (set in your environment variables as `OPENAI_API_KEY`)
- Telegram Bot Token (set in your environment variables as `BOT_TOKEN`)

### Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate into the project directory:
   ```bash
   cd <project_directory>
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the root directory and set your API keys:
   ```
   OPENAI_API_KEY=your_api_key_here
   BOT_TOKEN=your_telegram_bot_token_here
   ```

### Running the Chatbot
#### Console Mode
Start the application in console mode by running:
```bash
python chama_birth.py
```

#### Telegram Bot Mode
Start the Telegram bot by running:
```bash
python main_app_telegramAPI_module.py
```
Or use the deployed version at [t.me/assistente_chama_bot](https://t.me/assistente_chama_bot)

## Contributing
Contributions, bug reports, and feature requests are welcome!  
For any changes, please:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a pull request

## License
This project is free and open source. Please see the LICENSE file for more details.

## Acknowledgments
- Created by Dante Augusto (@dantexaugusto on Telegram)
- The open-source community for their continuous support
- All users providing valuable feedback that helps shape the project