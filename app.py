import streamlit as st
import os
import sys

# Add utils directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), "utils"))

from builder import build_agent_profile
from templates import agent_templates
from visual_generator import generate_avatar_card

st.set_page_config(page_title="Forge - Agent Builder", layout="wide")

st.title("🧠 Forge: Your AI Agent Builder")

st.markdown("Build new agents with a few clicks. Select their purpose, style, and generate a ready-to-use profile, prompt, and automation blocks.")

with st.form("agent_form"):
    name = st.text_input("Agent Name", placeholder="e.g., Zion")
    nickname = st.text_input("Agent Nickname", placeholder="e.g., The Tracker")
    role = st.text_area("Role / Description", placeholder="What does this agent do?")
    style = st.text_input("Communication Style", placeholder="e.g., Calm, Data-driven, Inspirational")
    quote = st.text_input("Agent Quote (optional)")
    output_gpt = st.checkbox("Include Custom GPT Prompt")
    output_workflow = st.checkbox("Include GoHighLevel Workflow Blocks")
    output_visual = st.checkbox("Include Visual Profile Card")

    submitted = st.form_submit_button("🛠 Build Agent")

if submitted:
    agent_data = {
        "name": name,
        "nickname": nickname,
        "role": role,
        "style": style,
        "quote": quote,
        "include_prompt": output_gpt,
        "include_workflow": output_workflow,
        "include_visual": output_visual
    }

    results = build_agent_profile(agent_data)

    st.success(f"✅ Agent '{name}' built successfully!")

    if output_gpt:
        st.subheader("🧾 Custom GPT Prompt")
        st.code(results["gpt_prompt"], language="markdown")

    if output_workflow:
        st.subheader("🔁 Workflow Automation Script")
        st.code(results["workflow_script"], language="text")

    if output_visual and results["visual_card"]:
        st.subheader("🎨 Agent Visual Card")
        st.image(results["visual_card"])

    st.download_button("Download Agent Files (ZIP)", data=results["zip_data"], file_name=f"{name}_Agent_Package.zip")
