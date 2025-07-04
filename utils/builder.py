
import zipfile
import io
import visual_generator
import templates

def build_agent_profile(agent):
    files = {}

    if agent["include_prompt"]:
        prompt = templates.agent_templates["gpt_prompt"].format(**agent)
        files["gpt_prompt.md"] = prompt

    if agent["include_workflow"]:
        workflow = templates.agent_templates["workflow"].format(**agent)
        files["workflow.txt"] = workflow

    if agent["include_visual"]:
        image = visual_generator.generate_avatar_card(agent)
        files["visual_card.png"] = image

    # Bundle into zip
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w") as zip_file:
        for filename, content in files.items():
            if isinstance(content, bytes):
                zip_file.writestr(filename, content)
            else:
                zip_file.writestr(filename, content.encode('utf-8'))
    zip_buffer.seek(0)

    return {
        "gpt_prompt": files.get("gpt_prompt.md", ""),
        "workflow_script": files.get("workflow.txt", ""),
        "visual_card": files.get("visual_card.png", None),
        "zip_data": zip_buffer
    }
