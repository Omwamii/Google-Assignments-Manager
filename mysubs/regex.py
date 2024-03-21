import re

# List of strings
def get_course_code(course_string: str) -> str:
    """ Extracts the course code from the course name """
    # Regular expression pattern
    pattern = r'.*?(CSC\s*_*?\d{3}).*?'

    # Loop through the strings and apply regex substitution
    match = re.match(pattern, course_string)
    if match:
        # new_strings.append(match.group(1))
        split_s = match.group(1)
        split = split_s.split(' ')
        if len(split) == 1:
            match = split_s[:3] + ' ' + split_s[-3:]
        else:
            match = split_s
        return match
    return course_string  # no match found