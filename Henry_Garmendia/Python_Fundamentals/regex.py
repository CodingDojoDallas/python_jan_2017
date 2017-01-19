import re

#ASSIGNMENT: REGEX
#  .	Matches any character except a new line.
#  \w 	Matches any letter or digit.
#  +	The pattern before it can appear 1 or more times.
#  *	The pattern can appear any number of times, including none.

# re.search(pattern, string) is a function that scans a string for a specific regex pattern and returns a match object

def get_matching_words(regex):
	words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

	return [word for word in words if re.search(regex, word)]

# All words that contain a “v”
print get_matching_words(r'v')

# All words that contain a double-“s”
print get_matching_words(r'ss')
print get_matching_words(r's{2}')

# All words that end with an “e”
print get_matching_words(r'e$')

# All words that contain an “b”, any character, then another “b”
print get_matching_words(r'b.b')

# All words that contain an “b”, at least one character, then another “b”
print get_matching_words(r'b*b')
print get_matching_words(r"b.+b")

# All words that contain an “b”, any number of characters (including zero), then another “b”
print get_matching_words(r"b\w*b")
print get_matching_words(r"b.*b")

# All words that include all five vowels in order
print get_matching_words(r"a.*e.*i.*o.*u.*")

# All words that only use the letters in “regular expression” (each letter can appear any number of times)
print get_matching_words(r"^[regularxpsion]*$")

# All words that contain a double letter
print get_matching_words(r's{2}')
print get_matching_words(r"(.)\1")