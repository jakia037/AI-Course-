from google import genai

# ==========================
# Gemini Client (API Key)
# ==========================
api_key ="your_API_key"  # <-- put your Gemini API key 
client = genai.Client(api_key=api_key)

# ==========================
# Memory Module
# ==========================
class Memory:
    def __init__(self):
        self.history = []

    def add(self, role, content):
        self.history.append({"role": role, "content": content})

    def get(self, limit=8):
        return self.history[-limit:]

# ==========================
# Sample Tool: Calculator
# ==========================
class Calculator:
    name = "calculator"
    description = "Do basic math operations."

    def run(self, expr: str):
        try:
            return f"Result / ফলাফল: {eval(expr)}"
        except Exception as e:
            return f"Error: {e}"

TOOLS = {
    "calculator": Calculator(),
}

# ==========================
# Agent Logic
# ==========================
class Agent:
    def __init__(self):
        self.memory = Memory()

    # Detect tool call: use:tool{payload}
    def detect_tool(self, text: str):
        if text.startswith("use:"):
            try:
                name, payload = text[4:].split("{", 1)
                payload = payload.rstrip("}")
                return name, payload
            except:
                return None
        return None

    # Ask Gemini LLM
    def ask_llm(self, user_msg: str):
        self.memory.add("user", user_msg)

        system_prompt = (
            "You are a helpful AI assistant. Detect the language of the user's input "
            "and reply in the same language. Always respond clearly and avoid confusing or reversed answers."
        )

        # Combine memory + system prompt
        prompt = f"{system_prompt}\n"
        for msg in self.memory.get():
            role = msg["role"]
            content = msg["content"]
            prompt += f"{role}: {content}\n"
        prompt += f"user: {user_msg}\nassistant:"

        # Gemini API call
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        text = response.text
        self.memory.add("assistant", text)
        return text

    # Main run
    def run(self, user_input: str):
        tool = self.detect_tool(user_input)
        if tool:
            name, payload = tool
            if name in TOOLS:
                return TOOLS[name].run(payload)
            return "Unknown tool / অজানা টুল।"

        return self.ask_llm(user_input)

# ==========================
# CLI loop
# ==========================
if __name__ == "__main__":
    agent = Agent()
    print("Gemini Multi-language AI Agent Ready!")

    while True:
        user = input("You: ")
        reply = agent.run(user)
        print("Agent:", reply)

