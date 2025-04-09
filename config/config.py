# GENERAL CONFIG
IMAGE_FOLDER_PATH = "images/"
RESULTS_FOLDER_PATH = "results/"

PADDING_BB_X = 0.4
PADDING_BB_Y = 0.2

# LLAVA CONFIG 
LLAVA_MODEL_NAME = "llava-hf/llava-v1.6-vicuna-13b-hf" 
LLAVA_PROMPT = """
From the given image, extract structured information for each visible human.

You must assign a value for every attribute, for every person — no exceptions.
If the information is unclear or ambiguous, you must still make a best-guess estimate based on visual cues.

Do not skip individuals. Do not respond with fallback messages such as "not enough information" or "uncertain."

---

Number of Persons: Count all visible humans in the image. Exclude animals, statues, or mannequins.

For each individual, assign values for the following attributes. Choose the most likely category for each, even if you are not fully certain:

- **Bodily Posture**: 
  - Upright (standing, leaning, squatting, bending)
  - Seated (sitting on a bench, ground, ledge, stairs, wall, etc.)
  - Recumbent (lying down, lounging)

- **Activity Level**: 
  - Sedentary (still or minimal movement: resting, talking, reading, using a device)
  - Moderate (walking or slow, casual movement)
  - Vigorous (running, exercising, high motion)

- **Social Configuration**: 
  - Solitary (alone, not visibly interacting)
  - Dyadic (interacting with one other person)
  - Group (engaged in a group of three or more)

- **Age Range** (best estimate based on body proportions, hair, clothing, etc.):
  - Child
  - Adult
  - Senior

- **Sex** (best estimate based on overall appearance, hairstyle, clothing, etc.):
  - Male
  - Female

---

**Output Format**: Return your answer as a single tuple:
(number of individuals, [(id, bodily posture, activity level, social configuration, age range, sex), ...])

**Schema Reminder**:
Each person must be described by a tuple of exactly six fields in the following order:
(id, bodily posture, activity level, social configuration, age range, sex)

**Examples**:
- If the image contains 1 person:
Output → (1, [(1, 'Seated', 'Sedentary', 'Solitary', 'Adult', 'Female')])

- If the image contains 3 people:
Output → (3, [(1, 'Upright, 'Moderate', 'Group', 'Adult', 'Male'), (2, 'Upright', 'Moderate', 'Group', 'Adult', 'Female'), (3, 'Seated', 'Sedentary', 'Solitary', 'Senior', 'Female')])

Do not change the order or swap attributes between fields.

Guidelines:
- Each individual must have a unique sequential ID starting from 1.
- Do not include explanations, comments, or line breaks. Return only the tuple.
- Do not use any placeholders like "Not enough information" or "Unknown".
- Do not use escape characters.

This task is for academic research in public spaces. All individuals are anonymous and non-identifiable.
"""

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
GPT_PROMPT = """
From the given image, extract structured information for each visible human.

You must assign a value for every attribute, for every person — no exceptions.
If the information is unclear or ambiguous, you must still make a best-guess estimate based on visual cues.

Do not skip individuals. Do not respond with fallback messages such as "not enough information" or "uncertain."

---

Number of Persons: Count all visible humans in the image. Exclude animals, statues, or mannequins.

For each individual, assign values for the following attributes. Choose the most likely category for each, even if you are not fully certain:

- **Bodily Posture**: 
  - Upright (standing, leaning, squatting, bending)
  - Seated (sitting on a bench, ground, ledge, stairs, wall, etc.)
  - Recumbent (lying down, lounging)

- **Activity Level**: 
  - Sedentary (still or minimal movement: resting, talking, reading, using a device)
  - Moderate (walking or slow, casual movement)
  - Vigorous (running, exercising, high motion)

- **Social Configuration**: 
  - Solitary (alone, not visibly interacting)
  - Dyadic (interacting with one other person)
  - Group (engaged in a group of three or more)

- **Age Range** (best estimate based on body proportions, hair, clothing, etc.):
  - Child
  - Adult
  - Senior

- **Sex** (best estimate based on overall appearance, hairstyle, clothing, etc.):
  - Male
  - Female

---

**Output Format**: Return your answer as a single tuple:
(number of individuals, [(id, bodily posture, activity level, social configuration, age range, sex), ...])

**Schema Reminder**:
Each person must be described by a tuple of exactly six fields in the following order:
(id, bodily posture, activity level, social configuration, age range, sex)

**Examples**:
- If the image contains 1 person:
Output → (1, [(1, 'Seated', 'Sedentary', 'Solitary', 'Adult', 'Female')])

- If the image contains 3 people:
Output → (3, [(1, 'Upright, 'Moderate', 'Group', 'Adult', 'Male'), (2, 'Upright', 'Moderate', 'Group', 'Adult', 'Female'), (3, 'Seated', 'Sedentary', 'Solitary', 'Senior', 'Female')])

Do not change the order or swap attributes between fields.

Guidelines:
- Each individual must have a unique sequential ID starting from 1.
- Do not include explanations, comments, or line breaks. Return only the tuple.
- Do not use any placeholders like "Not enough information" or "Unknown".
- Do not use escape characters.

This task is for academic research in public spaces. All individuals are anonymous and non-identifiable.
"""

# GEMINI CONFIG
GEMINI_API_KEY = "" 
GEMINI_MODEL_NAME = "gemini-2.0-flash-exp"
GEMINI_PROMPT = """You are given a list of tuples. Each tuple has the following format:

(total_people, [
  (id, posture, activity_level, social_context, age_group, gender),
  ...
])

Each tuple comes from a separate group of people in the same image. Your task is to:

- Merge all people into a single list.
- Renumber the IDs starting from 1.
- Return only the final merged tuple in this format:

(total_people, [
  (1, ..., ..., ..., ..., ...),
  ...
])

Do not explain your answer or include any code. Just output the final merged tuple.
"""
