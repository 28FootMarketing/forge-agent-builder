from PIL import Image, ImageDraw, ImageFont
import io

def generate_avatar_card(agent):
    img = Image.new("RGB", (600, 300), color=(30, 30, 30))
    draw = ImageDraw.Draw(img)

    name_text = f"{agent['name']} ({agent['nickname']})"
    role_text = agent['role']
    style_text = f"Style: {agent['style']}"

    draw.text((20, 20), name_text, fill=(255, 255, 255))
    draw.text((20, 80), role_text, fill=(200, 200, 200))
    draw.text((20, 140), style_text, fill=(180, 180, 180))

    # Save to bytes
    byte_io = io.BytesIO()
    img.save(byte_io, format='PNG')
    byte_io.seek(0)

    return byte_io.read()
