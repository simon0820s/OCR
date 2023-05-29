def run(input_name, input_id, result):
    test1 = all(word in result for word in input_name)
    test2 = input_id in result
    validation = test1 or test2
    return validation
