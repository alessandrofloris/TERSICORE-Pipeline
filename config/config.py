# GENERAL CONFIG
IMAGE_FOLDER_PATH = "images/"
RESULTS_FOLDER_PATH = "results/"

PADDING_BB_X = 0.4
PADDING_BB_Y = 0.2

# LLAVA CONFIG 
LLAVA_MODEL_NAME = "llava-hf/llava-v1.6-vicuna-13b-hf" 
LLAVA_PROMPT = """For each person in the image try to briefly describe their activity and if they seem interacting with someone or are togheter with someone, describe their presumed age range and their presumed sex. Focus only on this details, dont add other informations."""

# GPT CONFIG 
GPT_API_KEY = ""
GPT_PROMPT_IMAGE = """"
You are given a cropped scene that contains one or more people.

Your task is to describe each person you see, even if only partially visible. Provide your best estimate of:

- Age group: Child, Teen, Adult, or Senior.
- Gender: Male, Female, or Unknown.
- A short activity or posture description.

Even if you're unsure, provide your most likely interpretation. Respond in a numbered list, like this:

1. An adult male is seated on a bench, talking to someone nearby.
2. A teen girl is standing with arms crossed.

Avoid generic statements like "I'm not sure" — always provide your best guess.
"""
GPT_PROMPT_DESCRIPTION = """From the following list of descriptions, extract structured information for each human.
You must provide an answer for each attribute — even if uncertain. Make your best guess based on text cues.
Do not skip or omit individuals due to uncertainty. Avoid fallback or error messages.

Number of persons – Count all individuals (exclude animals, statues, or other non-human figures).

For each person, assign values for the attributes below:

- Bodily Posture: Describe their physical stance or position. Choose one of:
-- Upright (standing, leaning, squatting, bending)
-- Seated (sitting on a bench, ground, ledge, stairs, wall, etc.)
-- Recumbent (lying down, lounging)

- Activity Level: Estimate the level of movement. Choose one of:
-- Sedentary (still or minimal movement: resting, talking, reading, using a device)
-- Moderate (walking or slow, casual movement)
-- Vigorous (running, exercising, high motion)
- Social Configuration: Identify the social setting based on visible interaction. Choose one of:
-- Solitary (alone, not visibly interacting)
-- Dyadic (interacting with one other person)
-- Group (engaged in a group of three or more)
- Age Range: Based on appearance, select one of:
-- Child
-- Adult
-- Senior
-- Not enough information (if the age range cannot be determined)
- Sex: Based on visual appearance, assign:
-- Male
-- Female
-- Not enough information (if unclear)

Output Format: Return your results as a single tuple in the format:
(number of individuals, [(id, bodily posture, activity level, social configuration, age range, sex), ...])

- Important notes:
-- Each individual must have a unique sequential ID starting from 1. 
-- Do not include any explanations, commentary, or escape characters; return only the tuple.
"""
GPT_PROMPT = """From the given image, extract structured information for each visible human.
You must provide an answer for each attribute — even if uncertain. Make your best guess based on visual cues.
Do not skip or omit individuals due to uncertainty. Avoid fallback or error messages.

Number of persons – Count all visible individuals (exclude animals, statues, or other non-human figures).

For each person, assign values for the attributes below:

- Bodily Posture: Describe their physical stance or position. Choose one of:
-- Upright (standing, leaning, squatting, bending)
-- Seated (sitting on a bench, ground, ledge, stairs, wall, etc.)
-- Recumbent (lying down, lounging)

- Activity Level: Estimate the level of movement. Choose one of:
-- Sedentary (still or minimal movement: resting, talking, reading, using a device)
-- Moderate (walking or slow, casual movement)
-- Vigorous (running, exercising, high motion)
- Social Configuration: Identify the social setting based on visible interaction. Choose one of:
-- Solitary (alone, not visibly interacting)
-- Dyadic (interacting with one other person)
-- Group (engaged in a group of three or more)
- Age Range: Based on appearance, select one of:
-- Child
-- Adult
-- Senior
-- Not enough information (if the age range cannot be determined)
- Sex: Based on visual appearance, assign:
-- Male
-- Female
-- Not enough information (if unclear)

Output Format: Return your results as a single tuple in the format:
(number of individuals, [(id, bodily posture, activity level, social configuration, age range, sex), ...])

- Important notes:
-- Each individual must have a unique sequential ID starting from 1. 
-- Do not include any explanations, commentary, or escape characters; return only the tuple.
-- This task is for academic research and analysis of non-sensitive, non-identifiable crowd scenes in public spaces. All individuals are anonymous, and no facial recognition or identity inference is required.
-- Estimate general attributes such as posture or group setting without judging identity, emotions, or appearance.
"""

# GEMINI CONFIG
GEMINI_API_KEY = "" 
GEMINI_MODEL_NAME = "gemini-2.0-flash-exp"
GEMINI_PROMPT = """From the following list of descriptions, extract structured information for each human.
You must provide an answer for each attribute — even if uncertain. Make your best guess based on text cues.
Do not skip or omit individuals due to uncertainty. Avoid fallback or error messages.

Number of persons – Count all individuals (exclude animals, statues, or other non-human figures).

For each person, assign values for the attributes below:

- Bodily Posture: Describe their physical stance or position. Choose one of:
-- Upright (standing, leaning, squatting, bending)
-- Seated (sitting on a bench, ground, ledge, stairs, wall, etc.)
-- Recumbent (lying down, lounging)

- Activity Level: Estimate the level of movement. Choose one of:
-- Sedentary (still or minimal movement: resting, talking, reading, using a device)
-- Moderate (walking or slow, casual movement)
-- Vigorous (running, exercising, high motion)
- Social Configuration: Identify the social setting based on visible interaction. Choose one of:
-- Solitary (alone, not visibly interacting)
-- Dyadic (interacting with one other person)
-- Group (engaged in a group of three or more)
- Age Range: Based on appearance, select one of:
-- Child
-- Adult
-- Senior
-- Not enough information (if the age range cannot be determined)
- Sex: Based on visual appearance, assign:
-- Male
-- Female
-- Not enough information (if unclear)

Output Format: Return your results as a single tuple in the format:
(number of individuals, [(id, bodily posture, activity level, social configuration, age range, sex), ...])

- Important notes:
-- Each individual must have a unique sequential ID starting from 1. 
-- Do not include any explanations, commentary, or escape characters; return only the tuple.
"""
