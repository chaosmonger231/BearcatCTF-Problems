
import os
import time
from PIL import Image

def cut_image_into_sections(image_path, section_width, section_height, save_folder):
    try:
        img = Image.open(image_path)
        img_width, img_height = img.size
        print(f"Image Size: {img_width}x{img_height}")
           
        os.makedirs(save_folder, exist_ok=True)
        
        sections = []
        for top in range(0, img_height, section_height):
            for left in range(0, img_width, section_width):
                box = (left, top, left + section_width, top + section_height)
                section = img.crop(box)
                sections.append(section)
                
                section_file_path = os.path.join(save_folder, f"section_{top // section_height}_{left // section_width}.png")
                section.save(section_file_path)
                
                time.sleep(1)

        print(f"Total Sections: {len(sections)} saved to '{save_folder}'")
        return sections
    except Exception as e:
        print(f"Error: {e}")
    
image_path = "/Users/kramc/Desktop/bearcatCTF25_problems/Cropped_Image/target.png"
section_width = 322
section_height = 246
save_folder = "/Users/kramc/Desktop/bearcatCTF25_problems/Cropped_Image/images"

cropped_sections = cut_image_into_sections(image_path, section_width, section_height, save_folder)

#for index, section in enumerate(cropped_sections):
    #section.show()
    #section.save(f"section_{index}.png")