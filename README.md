# 📱 Auto-Reply System for Selected Telegram Users using LLMs 🤖

This project sets up an auto-reply system for selected Telegram users using Large Language Models (LLMs). It utilizes Ollama to manage local LLMs and OpenWebUI to create a single interface for connecting both local and OpenAI models. Additionally, TDLib binaries are employed for Telegram integration.

## Prerequisites ✅

- **Ollama** (optional): A platform for managing local LLMs. [🌐 Website](https://ollama.com) 
- **OpenWebUI**: A tool for creating a unified LLM interface. [🌐 Website](https://openwebui.com)
- **TDLib Binaries**: Precompiled binaries to avoid building from source, available [👉 here](https://github.com/ForNeVeR/tdlib.native/releases).
- **Python 3.7+**: Ensure you have Python installed. [📥 Download Python](https://www.python.org/downloads/)
- **Telegram Account**: To use the Telegram API.

## Installation ⚙️

Follow these steps to set up the project:

### 1. Install OpenWebUI 🛠️

- **With Ollama Support**: If you don't have Ollama installed, download OpenWebUI with bundled Ollama support. [📝 Installation Guide](https://docs.openwebui.com/#installing-open-webui-with-bundled-ollama-support)
  
- **API-Only**: If you only plan to use OpenAI models and do not need local models, use the API-only image. [📝 Installation Guide](https://docs.openwebui.com/#installation-for-openai-api-usage-only)

### 2. Generate OpenWebUI Token 🔑

- Obtain your API key from OpenWebUI by navigating to `Settings > Account`.
- Alternatively, create a JWT (JSON Web Token) for authentication.

### 3. Download TDLib Binaries 💾

- Go to the [TDLib releases page](https://github.com/ForNeVeR/tdlib.native/releases).
- Download the appropriate binary for your operating system and extract it to the root folder of your project.

### 4. Register Telegram Application 📄

- Register your application on Telegram to obtain `app_id` and `app_hash`.
- Refer to the Telegram documentation for detailed instructions: [📑 Obtaining API ID](https://core.telegram.org/api/obtaining_api_id)


### 5. Configuration File 🗂️

The configuration file is a JSON object that contains settings for both the Telegram integration and OpenWebUI model interaction. Below is a detailed explanation of each field within the configuration file:

```json
{
  "telegram": {
    "self": 382881513,
    "other": 236242192,
    "phone": "+38012345678",
    "api_id": 812346,
    "api_hash": "8667ab539ca5139dccc23142"
  },
  "openwebui": {
    "host": "http://localhost:3000",
    "token": "sk-0023123e21ba4015812f49b7ca2438f5",
    "model": "gpt-4o-mini",
    "prompt": "твоя задача вести бесіду з людиною, так щоб ніхто не зрозумів що ти не людина. уяви що спілкуєшся в мессенджері. не используй форматування тексту."
  }
}
```

### Telegram Settings 📲

- **self**: (Integer) Your own Telegram user ID. Messages you send will be treated by the LLM as assistant responses.
  
- **other**: (Integer) The Telegram user ID of the individual for whom this auto-reply system is designed. Messages from this ID will be treated as user inputs to the LLM.
  
- **phone**: (String) Your Telegram phone number, which is required for connection and verification.
  
- **api_id**: (Integer) The API ID provided by Telegram when you register your application.
  
- **api_hash**: (String) The API hash provided by Telegram during application registration. Used for authentication purposes.

### OpenWebUI Settings 🌐

- **host**: (String) The base URL where your OpenWebUI instance is hosted. Ensure this is correctly set to match the environment where OpenWebUI is running, typically `http://localhost:3000` for local setups.
  
- **token**: (String) The API token or JWT for authenticating requests to the OpenWebUI. Keep this secure and confidential.
  
- **model**: (String) The identifier for the LLM to be used, e.g., `"gpt-4o-mini"`. Make sure this corresponds to a model available and configured in OpenWebUI.
  
- **prompt**: (String) The initial prompt given to the LLM to define its behavior during conversations. This prompt is designed to instruct the model on maintaining human-like conversation characteristics while avoiding specific conversational topics or behaviors.


### 6. Setup Python Virtual Environment 🐍

- Create a Python virtual environment:
  ```bash
  python -m venv venv
  ```
- Activate the virtual environment:
  - On Windows: `.\venv\Scripts\activate`
  - On macOS/Linux: `source venv/bin/activate`
  
- Install required dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### 7. Start the Application 🚀

Run the main script to start the application:

```bash
python main.py
```

- On first execution, the application will prompt you for a Telegram confirmation number and password (if cloud passwords are enabled).

