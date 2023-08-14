def process_input(input_string):
    elements = input_string.split('|')
    result = []

    for element in elements:
        and_parts = element.split(',')
        and_expression = " and ".join(and_parts)
        result.append(f"({and_expression})")

    return result

input_string = "x,y|y,z|a,b"
output_list = process_input(input_string)
print(output_list)
