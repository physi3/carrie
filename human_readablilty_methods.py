"Methods to help with human readablilty"

def list_foramtting(list_for_formatting):
    "Formats list in a comma, comma, and format."
    string = ""
    for count, value in enumerate(list_for_formatting):
        if count >= 1 and count <= len(list_for_formatting)-2:
            string += ", "
        elif count == len(list_for_formatting)-1:
            string += " and "
        string += value
    return string
