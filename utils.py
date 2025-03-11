from PIL import Image, ImageDraw, ImageFont
import os
import yaml


def add_sufix_for_output_file(path: str) -> str:
    """"""
    root, ext = os.path.splitext(path)
    return f"{root}_output{ext}"


def draw_img_with_bb(path: str, data):
    """"""
    # Ouvrir une image existante
    image = Image.open(path)

    # Initialiser le module de dessin
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("arial.ttf", 14)

    # Dessiner un rectangle (x0, y0, x1, y1)
    for row in data:
        # coords
        x0, y0, x1, y1 = row["bounding_box"]

        # Dessiner le rectangle
        draw.rectangle([(x0, y0), (x1, y1)], fill="red" if row.get("clickable", False) else "black")
        
        # Calculer les dimensions et l'emplacement du texte
        text_bbox = draw.textbbox((0, 0), row["text"], font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        
        center_x = (x0 + x1) / 2
        center_y = (y0 + y1) / 2
        text_x = center_x - text_width / 2
        text_y = center_y - text_height / 2
        
        # Dessiner le texte centré
        draw.text((text_x, text_y), row["text"], fill="white", font=font)
        
    return image
    

def np_to_python(nb):
    """"""
    try:
        return nb.item()
    except:
        return nb


def perform_OCR(reader, input_path: str):
    """"""
    result = reader.readtext(input_path)

    return [
        {
            "text": text.lower(),
            "conf_level": round(np_to_python(confident_level), 2),
            "bounding_box":
                (
                    np_to_python(bounding_box[0][0]),
                    np_to_python(bounding_box[0][1]),
                    np_to_python(bounding_box[2][0]),
                    np_to_python(bounding_box[2][1])
                )
         } for bounding_box, text, confident_level in result
    ]


def load_yaml(path: str):
    """"""
    with open(path, "r", encoding="utf-8") as fichier:
        return yaml.safe_load(fichier)
