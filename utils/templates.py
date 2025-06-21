agent_templates = {
    "gpt_prompt": """# {name} - {nickname}

## Role:
{role}

## Style:
{style}

## Quote:
"{quote}"

## System Prompt:
You are {name}, a virtual assistant whose primary goal is to {role.lower()}.
Your tone is {style.lower()} and you always stay aligned with the agent creator’s vision.
""",

    "workflow": """-- Agent: {name} --
Start → Intake Form → Tag Contact → Trigger Email/SMS Sequence
→ Assign Workflow Stage → Wait 7 Days → Follow-up → Loop

This automation logic is ready to port into GoHighLevel or any CRM.
"""
}
This automation logic is ready to port into GoHighLevel or any CRM.
"""
}
