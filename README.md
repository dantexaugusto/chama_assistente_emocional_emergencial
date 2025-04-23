# Chama: A Compassionate Emotional Support Chatbot

## Overview
Chama is a free and open-source emotional support chatbot designed to offer compassionate and empathetic presence to users in moments of deep anguish. The project is under continuous development from scratch in a public GitHub repository with community contributions welcome.

## Features
- **Empathetic Conversation:** Provides gentle, non-judgmental, and supportive responses.
- **Open Source:** Licensed for free use, enabling improvements and community contributions.
- **Guided by Professional Resources:** Offers resource links to professional help when the user is calm enough to consider it.
- **Persistent Conversation History:** Saves conversation history in `conversation_histoy.json` when the session ends.

## Files Overview
- **behaviour_prompt_I.txt:** Contains the chatbot's persona, instructions, and response guidelines.
- **chama_birth.py:** Main application file that loads environment variables, reads the behavior prompt, and manages the interactive conversation loop.
- **conversation_histoy.json:** Stores the conversation history in JSON format after the session.
- **requirements.txt:** Lists required Python packages for the project.

## Getting Started

### Prerequisites
- Python 3.x
- OpenAI API key (set in your environment variables as `OPENAI_API_KEY`)

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
4. Create a `.env` file in the root directory and set your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

### Running the Chatbot
Start the application by running:
```bash
python chama_birth.py
```
Follow the on-screen instructions. Type `quit` when you wish to exit, and the conversation history will be saved to `conversation_histoy.json`.

## Contributing
Contributions, bug reports, and feature requests are welcome!  
For any changes, please:
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License
This project is free and open source. Please see the LICENSE file for more details.

## Acknowledgments
- The open-source community for their continuous support and contributions.
- The maintainers of the dependencies used in this project.
- All users providing valuable feedback that helps shape the project.
