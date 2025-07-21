
# 🐾 Pet Store Agent

A sophisticated AI-powered chatbot built with LangChain and Gradio that intelligently interacts with the Swagger Pet Store API. This agent can perform various pet store operations through natural language conversations, making API interactions intuitive and user-friendly.

## 🌟 Features

- **Intelligent Conversation**: Natural language interface powered by OpenAI's GPT-4o
- **Pet Store Operations**: Complete CRUD operations for pet management
- **Interactive Web UI**: Clean and responsive Gradio interface
- **Tool Integration**: Multi-tool agent with Wikipedia integration
- **Real-time Processing**: See intermediate steps and tool usage
- **Memory Persistence**: Conversation history maintained across interactions

## 🛠️ Tech Stack

- **Framework**: LangChain for agent orchestration
- **LLM**: OpenAI GPT-4o
- **UI**: Gradio for web interface
- **API**: Swagger Pet Store API (v2)
- **Tools**: Custom pet store tools + Wikipedia integration
- **Language**: Python 3.12+

## 📋 Prerequisites

- Python 3.12 or higher
- OpenAI API key
- Internet connection for API calls

## 🚀 Quick Start

### 1. Environment Setup

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 2. Installation

All dependencies are automatically managed by Replit. The project uses:

- `gradio` - Web interface
- `langchain` - Agent framework
- `langchain-openai` - OpenAI integration
- `requests` - HTTP client
- `python-dotenv` - Environment management

### 3. Running the Application

Click the **Run** button in Replit, or execute:

```bash
python app.py
```

The application will start on port 7860 and provide both local and public URLs.

## 💬 Usage Examples

### Basic Pet Operations

```
User: "Find all available pets"
Agent: Uses find_pets_by_status tool to retrieve available pets

User: "Add a new dog named Max"
Agent: Uses add_pet tool to create a new pet entry

User: "Get details for pet ID 12345"
Agent: Uses get_pet_by_id tool to fetch specific pet information

User: "Delete pet with ID 99999"
Agent: Uses delete_pet tool to remove the pet
```

### Advanced Queries

```
User: "What pets are currently pending adoption?"
Agent: Searches for pets with "pending" status

User: "Tell me about Golden Retrievers and then find any Golden Retriever pets in the store"
Agent: Uses Wikipedia for breed information, then searches the pet store
```

## 🔧 Project Structure

```
├── app.py              # Main Gradio application
├── agents.py           # Agent creation and configuration
├── tools.py           # Pet store API tools and schemas
├── requirements.txt   # Python dependencies
├── pyproject.toml     # Project configuration
└── README.md          # This file
```

### Core Components

#### `app.py`
- Main application entry point
- Gradio ChatInterface setup
- Response formatting with intermediate steps
- Environment configuration

#### `agents.py`
- Agent factory function
- OpenAI Tools Agent configuration
- Memory management setup
- Error handling and iteration limits

#### `tools.py`
- Pet Store API integration tools:
  - `add_pet` - Create new pets
  - `update_pet` - Modify existing pets
  - `get_pet_by_id` - Retrieve pet details
  - `delete_pet` - Remove pets
  - `find_pets_by_status` - Search by status
- Wikipedia integration for general queries
- Pydantic schemas for type safety

## 🔌 API Integration

The agent integrates with the Swagger Pet Store API v2:
- **Base URL**: `https://petstore.swagger.io/v2`
- **Supported Operations**: CRUD operations for pets
- **Data Format**: JSON with structured schemas
- **Error Handling**: Robust retry mechanisms and validation

## 🎛️ Configuration

### Agent Settings
- **Model**: GPT-4o for optimal performance
- **Temperature**: 0 for consistent responses
- **Max Iterations**: 5 to prevent infinite loops
- **Memory**: Conversation buffer for context retention

### Tool Configuration
- All tools use Pydantic schemas for input validation
- Comprehensive error handling for API failures
- Automatic retry mechanisms for reliability

## 🐛 Troubleshooting

### Common Issues

1. **OpenAI API Key Error**
   - Ensure your API key is set in the `.env` file
   - Verify the key has sufficient credits

2. **Pet Store API Errors**
   - Check internet connectivity
   - API may occasionally return 404 for non-existent pets

3. **Tool Execution Failures**
   - Review intermediate steps in the UI
   - Check console output for detailed error messages

### Debug Mode

The application runs with `debug=True` enabled, providing:
- Detailed console logging
- Automatic reloading on code changes
- Enhanced error messages

## 📈 Performance Considerations

- **Response Time**: Typically 2-5 seconds depending on query complexity
- **Concurrent Users**: Gradio handles multiple simultaneous conversations
- **Rate Limits**: Respects OpenAI API rate limits
- **Memory Usage**: Conversation history is maintained in memory

## 🔮 Future Enhancements

- [ ] Add pet image upload capabilities
- [ ] Implement advanced search filters
- [ ] Add user authentication
- [ ] Create pet adoption workflow
- [ ] Integrate with more pet-related APIs
- [ ] Add voice interaction capabilities

## 📄 License

This project is for educational and demonstration purposes. Please respect the terms of service for:
- OpenAI API
- Swagger Pet Store API
- Wikipedia API

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For issues and questions:
- Check the troubleshooting section above
- Review console output for error details
- Ensure all dependencies are properly installed

---

**Built with ❤️ using LangChain, OpenAI, and Gradio**
