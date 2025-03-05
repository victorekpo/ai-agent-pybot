import os
from openai import OpenAI
import requests
from dotenv import load_dotenv
from datetime import datetime
import time
import re
import random

load_dotenv()

# Initialize the OpenAI client
client = OpenAI(
    api_key=os.getenv('API_KEY'),
)

# Function to generate image
def openai_generate(prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,  # Number of images to generate
        size="1024x1024"  # You can use "256x256", "512x512", or "1024x1024"
    )

    # Get the image URL from the response
    image_url = response.data[0].url

    return image_url

# Function to save the image
def save_image(image_url, save_path):
    # Send GET request to download the image
    image_response = requests.get(image_url)

    if image_response.status_code == 200:
        # Save the image to the specified path
        with open(save_path, 'wb') as f:
            f.write(image_response.content)
        print(f"Image saved to {save_path}")
    else:
        print("Failed to download image.")

def clean_filename(prompt):
    # Define a list of stop words to remove
    stop_words = ['a', 'an', 'the', 'of', 'and', 'or', 'in', 'at', 'to', 'with', 'on', 'for', 'by', 'is', 'it', 'this', 'that', 'these', 'those']
    # Convert prompt to lowercase
    prompt = prompt.lower()
    # Remove stop words and unwanted characters
    cleaned_prompt = re.sub(r'\b(?:' + '|'.join(stop_words) + r')\b', '', prompt)
    cleaned_prompt = re.sub(r'[^\w\s]', '', cleaned_prompt)  # Remove punctuation
    cleaned_prompt = re.sub(r'\s+', '_', cleaned_prompt.strip())  # Replace spaces with underscores
    return cleaned_prompt

# Function to generate and save an image based on a prompt
def generate_image(prompt):
    # Generate image based on the prompt
    image_url = openai_generate(prompt)

    # Get the image filename from the prompt
    filename = clean_filename(prompt)

    # Get the current timestamp
    timestamp = datetime.now().strftime("%m-%d-%Y-%H-%M-%S")

    # Set the save path
    save_path = os.path.join(os.getcwd(), "generated", f"{filename}-{timestamp}.png")

    # Save the image to your computer
    save_image(image_url, save_path)

def run_generate_image():
    prompts = [
        "A beautiful Nigerian woman dressed in traditional attire",
        "A beautiful Nigerian woman dressed in city attire",
        "A beautiful Nigerian woman dressed in traditional wedding attire",
        "A beautiful Nigerian woman dressed in Igbo traditional wedding attire",
        "A beautiful Nigerian woman dressed in Akwa Ibom traditional wedding attire",
        "A beautiful Nigerian woman dressed in Edo traditional wedding attire",
        "A beautiful Nigerian woman dressed in Yoruba traditional wedding attire",

        "Beautiful Nigerian woman gasping after seeing beautiful flowers from her handsome Nigerian man.",
        "Beautiful Nigerian woman and handsome Nigerian man dancing joyfully at their traditional wedding.",
        "Beautiful Nigerian woman and handsome Nigerian man exchanging vows under a decorated arch.",
        "Beautiful Nigerian woman smiling while holding a bouquet of flowers.",
        "Handsome Nigerian man placing a ring on the beautiful Nigerian woman's finger.",
        "Beautiful Nigerian woman and handsome Nigerian man sharing a romantic kiss.",
        "Beautiful Nigerian woman and handsome Nigerian man cutting their wedding cake together.",
        "Beautiful Nigerian woman and handsome Nigerian man walking hand in hand down the aisle.",
        "Beautiful Nigerian woman and handsome Nigerian man laughing with their wedding party.",
        "Beautiful Nigerian woman and handsome Nigerian man sharing a tender moment under the stars.",
        "Beautiful Nigerian woman and handsome Nigerian man posing for a traditional wedding photo.",
        "Beautiful Nigerian woman and handsome Nigerian man holding hands during the ceremony.",
        "Beautiful Nigerian woman and handsome Nigerian man exchanging loving glances.",
        "Beautiful Nigerian woman and handsome Nigerian man dancing under a canopy of lights.",
        "Beautiful Nigerian woman and handsome Nigerian man sharing a toast with their guests.",
        "Beautiful Nigerian woman and handsome Nigerian man embracing after the ceremony.",
        "Beautiful Nigerian woman and handsome Nigerian man enjoying a traditional wedding feast.",
        "Beautiful Nigerian woman and handsome Nigerian man surrounded by family and friends.",
        "Beautiful Nigerian woman and handsome Nigerian man sharing a quiet moment by a lake.",
        "Beautiful Nigerian woman and handsome Nigerian man walking through a flower-filled garden.",
        "Beautiful Nigerian woman and handsome Nigerian man holding hands during a traditional dance.",
        "Beautiful Nigerian woman and handsome Nigerian man sharing a laugh during the reception.",
        "Beautiful Nigerian woman and handsome Nigerian man posing with their parents.",
        "Beautiful Nigerian woman and handsome Nigerian man sharing a romantic dance.",
        "Beautiful Nigerian woman and handsome Nigerian man exchanging gifts during the ceremony.",
        "Beautiful Nigerian woman and handsome Nigerian man sharing a kiss under a floral arch.",
        "Beautiful Nigerian woman and handsome Nigerian man walking through a field of wildflowers.",
        "Beautiful Nigerian woman and handsome Nigerian man sharing a moment of prayer.",
        "Beautiful Nigerian woman and handsome Nigerian man dancing with their guests.",
        "Beautiful Nigerian woman and handsome Nigerian man sharing a kiss at sunset.",
        "Beautiful Nigerian woman and handsome Nigerian man posing with their wedding party.",
        "Beautiful Nigerian woman and handsome Nigerian man sharing a kiss in front of a waterfall.",
        "Beautiful Nigerian woman and handsome Nigerian man holding hands during a traditional ceremony.",
        "Beautiful Nigerian woman and handsome Nigerian man sharing a kiss under a tree.",
        "Beautiful Nigerian woman and handsome Nigerian man walking through a forest.",
        "Beautiful Nigerian woman and handsome Nigerian man sharing a kiss in a meadow.",
        "Beautiful Nigerian woman and handsome Nigerian man posing for a photo in front of a historic building.",
        "Beautiful Nigerian woman and handsome Nigerian man sharing a kiss on a bridge.",
        "Beautiful Nigerian woman and handsome Nigerian man walking through a vineyard.",
        "Beautiful Nigerian woman and handsome Nigerian man sharing a kiss in a garden.",
        "Beautiful Nigerian woman and handsome Nigerian man posing for a photo in front of a castle.",
        "Beautiful Nigerian woman and handsome Nigerian man sharing a kiss on a beach.",
        "Beautiful Nigerian woman and handsome Nigerian man walking through a park.",
        "Beautiful Nigerian woman and handsome Nigerian man sharing a kiss in a field.",
        "Beautiful Nigerian woman and handsome Nigerian man posing for a photo in front of a mountain.",
        "Beautiful Nigerian woman and handsome Nigerian man sharing a kiss in a cityscape.",
        "Beautiful Nigerian woman and handsome Nigerian man walking through a market.",
        "Beautiful Nigerian woman and handsome Nigerian man sharing a kiss in a courtyard.",
        "Beautiful Nigerian woman and handsome Nigerian man posing for a photo in front of a lake.",
        "Beautiful Nigerian woman and handsome Nigerian man sharing a kiss in a forest clearing."

        "handsome Nigerian man, the tech bro, wearing a stylish suit, standing at the airport terminal, looking excited to return to Nigeria to see beautiful Nigerian woman",
        "beautiful Nigerian woman, looking radiant in her traditional attire, walking through a lively Nigerian market, with a vibrant smile on her face",
        "handsome Nigerian man and beautiful Nigerian woman reunited at the airport, embracing each other with joy, amidst a backdrop of Nigerian airport excitement",
        "handsome Nigerian man and beautiful Nigerian woman laughing together under a tree in a traditional Nigerian village, surrounded by family members",
        "handsome Nigerian man and beautiful Nigerian woman having a quiet moment by a serene lake, with birds flying above and nature surrounding them",
        "handsome Nigerian man visiting beautiful Nigerian woman's home, greeting her mother, while traditional Nigerian décor sets the atmosphere",
        "handsome Nigerian man and beautiful Nigerian woman sitting on a cozy porch, discussing the future, with the sun setting in the background",
        "handsome Nigerian man presenting beautiful Nigerian woman with a beautiful necklace during their engagement ceremony, both smiling with love",
        "handsome Nigerian man's family arriving at beautiful Nigerian woman's home, warmly greeted by her parents, both families exchanging gifts",
        "beautiful Nigerian woman helping her mother prepare traditional Nigerian dishes in the kitchen, laughter filling the air",
        "handsome Nigerian man's tech gadgets and laptop placed on a table, while he demonstrates his work to local Nigerians in a small office",
        "handsome Nigerian man giving a motivational speech at a local event, inspiring young Nigerians to pursue careers in technology",
        "A group of young Nigerians attending a solar energy workshop led by handsome Nigerian man, taking notes attentively",
        "handsome Nigerian man and beautiful Nigerian woman in traditional Nigerian wedding attire, standing side by side during the wedding ceremony, exchanging loving glances",
        "handsome Nigerian man kneeling down to propose to beautiful Nigerian woman during a traditional marriage ceremony, with family members cheering",
        "beautiful Nigerian woman's mother lovingly helping her into her wedding dress, giving her daughter words of wisdom and encouragement",
        "handsome Nigerian man's family members dancing joyfully at the traditional Nigerian wedding reception, clapping along with the beat",
        "beautiful Nigerian woman's family singing traditional songs as part of the wedding ceremony, with elders giving blessings",
        "handsome Nigerian man and beautiful Nigerian woman walking hand in hand through a vibrant Nigerian market, where they are greeted by the friendly locals",
        "handsome Nigerian man and beautiful Nigerian woman posing for a photo with elders of both families, smiling proudly at the successful union",
        "handsome Nigerian man and beautiful Nigerian woman sitting at a grand feast with their families, enjoying a traditional Nigerian meal of jollof rice and suya",
        "handsome Nigerian man and beautiful Nigerian woman holding hands during the traditional marriage vows, surrounded by colorful flowers and family members",
        "handsome Nigerian man and beautiful Nigerian woman exchanging heartfelt letters during the ceremony, expressing their love for each other",
        "handsome Nigerian man and beautiful Nigerian woman smiling lovingly at each other as they share their first dance as husband and wife",
        "The sun setting over a traditional Nigerian village, with handsome Nigerian man and beautiful Nigerian woman standing together, holding hands, gazing into the horizon",
        "handsome Nigerian man sharing a moment with his father before the ceremony, receiving advice about love and marriage",
        "beautiful Nigerian woman laughing joyfully as her friends and family tease her before the wedding, in a fun and lighthearted moment",
        "handsome Nigerian man's friends and family arriving at the wedding venue, eagerly greeting the bride's family",
        "The couple surrounded by their friends, all smiling and clinking glasses in a joyful wedding toast",
        "A close-up of the traditional Nigerian wedding rings being exchanged, sparkling under the warm sunlight",
        "handsome Nigerian man and beautiful Nigerian woman having a moment of prayer together, hands held tightly, praying for a successful marriage",
        "beautiful Nigerian woman walking down the aisle in her traditional Nigerian wedding attire, her face glowing with happiness",
        "handsome Nigerian man and beautiful Nigerian woman exchanging a soft, romantic kiss under the wedding arch, with family and friends applauding",
        "beautiful Nigerian woman's mother giving her daughter a loving, emotional hug before the ceremony begins",
        "handsome Nigerian man and beautiful Nigerian woman visiting a local solar energy project site, learning about renewable energy sources together",
        "handsome Nigerian man teaching a class of young Nigerians about technology and solar energy in a modern classroom",
        "handsome Nigerian man and beautiful Nigerian woman sitting with their families, discussing future plans for their business and their marriage",
        "beautiful Nigerian woman helping handsome Nigerian man set up a new solar-powered device for the community, both working together as a team",
        "handsome Nigerian man and beautiful Nigerian woman having a joyful conversation with the local community members during a cultural festival",
        "handsome Nigerian man's cousins teaching beautiful Nigerian woman how to dance a traditional Nigerian dance at the wedding reception",
        "handsome Nigerian man and beautiful Nigerian woman exchanging a deep look during their wedding vows, promising each other love and loyalty",
        "handsome Nigerian man and beautiful Nigerian woman dancing joyfully under a canopy of fairy lights, with guests cheering them on",
        "handsome Nigerian man and beautiful Nigerian woman in the midst of a lively traditional Nigerian ceremony, surrounded by colorful fabric and decorations",
        "handsome Nigerian man's tech presentation at a Nigerian university, inspiring young minds with his passion for innovation",
        "beautiful Nigerian woman sharing a sweet moment with her younger siblings during the wedding preparation, laughing together",
        "handsome Nigerian man and beautiful Nigerian woman cutting their wedding cake together, with a crowd of family and friends cheering them on",
        "beautiful Nigerian woman, with her radiant smile, holding a bouquet of bright flowers, as she prepares for her wedding",
        "handsome Nigerian man and beautiful Nigerian woman posing for a photo with their wedding party, all wearing traditional Nigerian attire",
        "handsome Nigerian man and beautiful Nigerian woman surrounded by family, as they walk through a flower-filled garden on their wedding day",
        "handsome Nigerian man and beautiful Nigerian woman sharing a romantic kiss in front of a traditional Nigerian hut during their wedding",
        "handsome Nigerian man and beautiful Nigerian woman holding hands while walking down a beautiful, flower-lined path after the ceremony",
        "handsome Nigerian man and beautiful Nigerian woman exchanging gifts during the traditional Nigerian wedding ceremony, showing their affection for each other",
        "beautiful Nigerian woman and her mother sitting together, reflecting on the joyous occasion, while the wedding preparations continue",
        "handsome Nigerian man smiling as he listens to stories from the elders about love, marriage, and tradition",
        "handsome Nigerian man and beautiful Nigerian woman laughing as they share an inside joke during their wedding reception",
        "beautiful Nigerian woman and her friends sitting together, talking about the upcoming wedding with excitement",
        "handsome Nigerian man and beautiful Nigerian woman receiving a blessing from an elder of the family, hands raised in prayer",
        "handsome Nigerian man and beautiful Nigerian woman greeting their guests at the wedding reception, smiling as they receive words of congratulations",
        "beautiful Nigerian woman and her family playing traditional Nigerian wedding games, laughing and enjoying the day",
        "handsome Nigerian man and beautiful Nigerian woman sharing a private moment under the stars after the wedding ceremony, enjoying the quiet beauty of the night",
        "handsome Nigerian man's family setting up a large wedding tent, excitedly preparing for the ceremony with beautiful decorations",
        "beautiful Nigerian woman, with her friends, dancing around the fire during a traditional Nigerian pre-wedding celebration",
        "handsome Nigerian man and beautiful Nigerian woman cutting traditional wedding foods, like pounded yam and egusi soup, and serving them to guests",
        "handsome Nigerian man and beautiful Nigerian woman taking part in a traditional Nigerian wedding ceremony, with family members watching proudly",
        "handsome Nigerian man and beautiful Nigerian woman exchanging a meaningful glance before the ceremony begins, sharing their love with each other",
        "handsome Nigerian man and beautiful Nigerian woman laughing together as they engage in playful wedding games with their families",
        "handsome Nigerian man and beautiful Nigerian woman dancing to live Nigerian music at their wedding reception, surrounded by excited guests",
        "handsome Nigerian man and beautiful Nigerian woman praying together during the ceremony, seeking blessings for their new life together",
        "handsome Nigerian man and beautiful Nigerian woman sharing a sweet moment, holding hands and looking at the crowd with joy and pride",
        "beautiful Nigerian woman’s friends teasing her playfully during the bridal shower before the wedding, everyone laughing",
        "handsome Nigerian man helping his family members put up decorations for the wedding, ensuring everything is perfect",
        "handsome Nigerian man and beautiful Nigerian woman sharing a quiet moment at a traditional Nigerian wedding venue, gazing at the decorations",
        "beautiful Nigerian woman laughing and talking with her friends as they help her get ready for the wedding ceremony",
        "handsome Nigerian man and beautiful Nigerian woman preparing their solar-powered devices for their new business venture, planning to change lives in Nigeria",
        "handsome Nigerian man receiving a warm welcome from the elders during the traditional wedding ceremony, all smiling together",
        "handsome Nigerian man and beautiful Nigerian woman laughing while trying to balance plates of food at their traditional Nigerian wedding feast",
        "handsome Nigerian man and beautiful Nigerian woman surrounded by family and friends, sharing a moment of joy and celebration during their wedding",
        "handsome Nigerian man and beautiful Nigerian woman enjoying a peaceful, intimate moment while watching the sunset on their wedding day",
        "handsome Nigerian man arriving at the airport in Nigeria, looking excited and nervous to reunite with beautiful Nigerian woman.",
        "beautiful Nigerian woman greeting handsome Nigerian man at the airport with a warm, loving embrace.",
        "handsome Nigerian man and beautiful Nigerian woman taking a walk through a Nigerian village, holding hands, talking about their dreams.",
        "beautiful Nigerian woman cooking traditional Nigerian food in the kitchen, her mom helping her, while handsome Nigerian man looks on with admiration.",
        "handsome Nigerian man showing beautiful Nigerian woman how to code on his laptop, teaching her about technology.",
        "beautiful Nigerian woman and handsome Nigerian man enjoying a Nigerian festival together, dancing and laughing with friends and family.",
        "handsome Nigerian man and beautiful Nigerian woman posing for a photo, smiling broadly, while traditional Nigerian decorations surround them.",

        "handsome Nigerian man and beautiful Nigerian woman watching the sunset together, sitting on a traditional Nigerian wooden bench",
        "handsome Nigerian man and beautiful Nigerian woman at a Nigerian wedding reception, sharing their first dance as husband and wife",
        "handsome Nigerian man and beautiful Nigerian woman exchanging vows, standing in front of a vibrant Nigerian floral arrangement",
        "beautiful Nigerian woman, surrounded by bridesmaids, all laughing and enjoying their time before the wedding ceremony",
        "handsome Nigerian man and beautiful Nigerian woman walking down a red carpet at their wedding reception, surrounded by cheers and applause",
        "beautiful Nigerian woman receiving a bouquet from a family member during her wedding, smiling with excitement and gratitude",
        "handsome Nigerian man sharing a private moment with beautiful Nigerian woman before their wedding ceremony, exchanging love-filled glances",
        "handsome Nigerian man and beautiful Nigerian woman receiving blessings from their elders at the traditional wedding ceremony",
        "handsome Nigerian man presenting beautiful Nigerian woman with a custom-made gift during their wedding, both smiling with love",
        "handsome Nigerian man and beautiful Nigerian woman dancing together in a traditional Nigerian dance circle at their wedding reception",
        "beautiful Nigerian woman and handsome Nigerian man taking part in a community wedding celebration, with locals dancing and singing joyfully",
        "handsome Nigerian man and beautiful Nigerian woman surrounded by their close friends, all raising glasses for a wedding toast",
        "handsome Nigerian man and beautiful Nigerian woman sitting together on a bench under a tree, having an intimate conversation about their future",
        "handsome Nigerian man walking beautiful Nigerian woman down the aisle, with guests admiring their elegant wedding outfits",
        "handsome Nigerian man and beautiful Nigerian woman receiving a ceremonial blessing from their parents at the wedding reception",
        "handsome Nigerian man and beautiful Nigerian woman enjoying a traditional Nigerian meal together, seated with family and friends",
        "beautiful Nigerian woman, with her bridal party, preparing for the wedding ceremony, laughing and enjoying the moment",
        "handsome Nigerian man and beautiful Nigerian woman posing with their families in front of a grand wedding stage",
        "handsome Nigerian man and beautiful Nigerian woman making their grand entrance at their wedding reception, greeted by cheers from the crowd",
        "handsome Nigerian man and beautiful Nigerian woman exchanging a romantic kiss at their wedding, surrounded by flowers and decorations",
        "handsome Nigerian man and beautiful Nigerian woman sharing a sweet moment at their wedding reception, holding hands and smiling",
        "handsome Nigerian man and beautiful Nigerian woman standing at the front of the church, surrounded by friends and family, ready to begin their journey as a married couple",
        "handsome Nigerian man and beautiful Nigerian woman dancing together at their wedding reception, with a Nigerian band playing traditional music",
        "handsome Nigerian man and beautiful Nigerian woman laughing as they enjoy a peaceful moment together, watching the sunset by the beach",
        "handsome Nigerian man and beautiful Nigerian woman joining their families in the traditional Nigerian wedding ceremony, surrounded by colorful decorations",
        "handsome Nigerian man and beautiful Nigerian woman walking hand in hand through the lively streets of Nigeria, smiling and greeting locals",
        "handsome Nigerian man and beautiful Nigerian woman relaxing together on their honeymoon, enjoying a quiet moment in a beautiful Nigerian landscape",
        "handsome Nigerian man and beautiful Nigerian woman exchanging words of love and devotion, standing in front of their wedding guests",
        "handsome Nigerian man and beautiful Nigerian woman enjoying a boat ride together, smiling and laughing with each other",
        "handsome Nigerian man and beautiful Nigerian woman visiting a traditional Nigerian village, learning about local culture and customs",
        "handsome Nigerian man and beautiful Nigerian woman enjoying a serene afternoon in a beautiful Nigerian park, relaxing together",
        "handsome Nigerian man and beautiful Nigerian woman sitting on a bench in a Nigerian garden, holding hands and reflecting on their wedding day",
        "handsome Nigerian man and beautiful Nigerian woman walking through a Nigerian marketplace, exploring vibrant colors and sounds around them",
        "handsome Nigerian man and beautiful Nigerian woman enjoying a moment of quiet reflection, surrounded by the natural beauty of Nigeria",
        "handsome Nigerian man and beautiful Nigerian woman sharing a laugh as they prepare to take their wedding photos in a beautiful Nigerian setting",
        "handsome Nigerian man and beautiful Nigerian woman standing on a Nigerian cliff, enjoying the panoramic view of the landscape below",
        "handsome Nigerian man and beautiful Nigerian woman sitting side by side on a blanket under the stars, talking about their dreams for the future",
        "handsome Nigerian man and beautiful Nigerian woman smiling at each other during the traditional Nigerian wedding ceremony, both looking radiant",
        "handsome Nigerian man and beautiful Nigerian woman dancing together at the heart of a traditional Nigerian wedding party",
        "handsome Nigerian man and beautiful Nigerian woman celebrating their wedding with traditional Nigerian music and dance",
        "handsome Nigerian man and beautiful Nigerian woman sharing a romantic, candle-lit dinner together after their wedding ceremony",
        "handsome Nigerian man and beautiful Nigerian woman exchanging smiles as they take their wedding vows, both deeply in love",
        "handsome Nigerian man and beautiful Nigerian woman at a Nigerian wedding reception, greeting their guests with warmth and love",
        "handsome Nigerian man and beautiful Nigerian woman sitting by the fireplace in a cozy Nigerian home, enjoying each other’s company",
        "handsome Nigerian man and beautiful Nigerian woman traveling together to a scenic Nigerian destination, with nature in the background",
        "handsome Nigerian man and beautiful Nigerian woman talking to elders about love, marriage, and tradition during the pre-wedding rituals",
        "handsome Nigerian man and beautiful Nigerian woman surrounded by vibrant flowers and traditional Nigerian decor, ready for their big day",
        "handsome Nigerian man and beautiful Nigerian woman sitting on a Nigerian bench in a peaceful park, holding hands and enjoying the moment",
        "handsome Nigerian man and beautiful Nigerian woman exchanging romantic gifts during their traditional Nigerian wedding ceremony",
        "handsome Nigerian man and beautiful Nigerian woman sharing a moment of joy with their wedding guests, laughing and dancing together",
        "handsome Nigerian man and beautiful Nigerian woman smiling warmly as they welcome their family and friends to their wedding reception",
        "handsome Nigerian man and beautiful Nigerian woman standing together, holding hands, under a Nigerian wedding arch adorned with flowers",
        "handsome Nigerian man and beautiful Nigerian woman sitting in front of a beautiful Nigerian waterfall, sharing a peaceful moment",
        "handsome Nigerian man and beautiful Nigerian woman gazing into each other’s eyes, their love evident as they prepare for their wedding",
        "handsome Nigerian man and beautiful Nigerian woman walking down the aisle together at their Nigerian wedding, side by side with love and joy",
        "handsome Nigerian man and beautiful Nigerian woman surrounded by family members, sharing an intimate moment before the wedding ceremony begins",
        "handsome Nigerian man and beautiful Nigerian woman dancing under the stars, with Nigerian music filling the air at their wedding reception"
    ]

    while True:
        random.shuffle(prompts)  # Shuffle the prompts before processing
        for i in range(0, len(prompts), 4):
            batch = prompts[i:i + 4]
            for prompt in batch:
                try:
                    generate_image(prompt)
                except Exception as e:

                    print(f"Error generating image for prompt '{prompt}': {e}")
            time.sleep(61)  # Wait for 1 minute before processing the next batch