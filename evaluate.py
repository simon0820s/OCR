# Function input: binary-img output: String result of Optical Character Recognition
def run(input_name, input_id, result):
    # Test name absolute match
    test1 = all(word in result for word in input_name)
    # Test ID match
    test2 = input_id in result
    # Boolean value if match test1 or test2
    validation = test1 or test2
    return validation
