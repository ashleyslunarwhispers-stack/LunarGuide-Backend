import gradio as gr

def lunar_guide(prompt):
    # Simulated response logic for now
    if "moon" in prompt.lower():
        return "🌕 The moon is currently in her waxing phase. Set intentions, light a candle, and speak your truth."
    elif "shadow" in prompt.lower():
        return "🌑 Shadow work prompt: What part of yourself feels unseen, and what would it say if it had a voice?"
    elif "tarot" in prompt.lower():
        return "🔮 Tarot pull: The High Priestess. Trust your intuition and honor the mystery."
    elif "energy" in prompt.lower():
        return "✨ Energy scan: Your aura feels tender. Ground with breath and surround yourself with lavender light."
    else:
        return "🌙 Welcome, seeker. Ask about moon phases, shadow work, tarot, or energy scans."

iface = gr.Interface(
    fn=lunar_guide,
    inputs=gr.Textbox(lines=2, placeholder="Ask Lunar Guide for a ritual, tarot reading, or energy scan..."),
    outputs="text",
    title="Lunar Guide",
    description="A mystical AI companion for moon-aligned rituals, tarot, and emotional healing."
)

iface.launch()
