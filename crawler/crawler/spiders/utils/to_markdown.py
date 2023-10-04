import re


def clean_content(soup):
    # Get all of the content tags
    content_tags = soup.find_all(["meta", "h1", "h2", "h3", "p", "a"])

    # Clean the content by removing any HTML tags and whitespace
    clean_content = []
    for tag in content_tags:
        clean_content.append(tag.text.strip())

    # as string
    text = " ".join(clean_content)

    # Define a regex pattern to match Spanish words (words with accented characters)
    pattern = r"\b[áéíóúüñÁÉÍÓÚÜÑa-zA-Z\s]+\b"

    # Find all matches in the text
    matches = re.findall(pattern, text)

    # Join the matches into a single string with spaces
    spanish_text = " ".join(matches)

    # remove salt lines
    spanish_text = spanish_text.replace("\n", " ")

    # remove multiple spaces
    spanish_text = re.sub(" +", " ", spanish_text)

    return spanish_text
