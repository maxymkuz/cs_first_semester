def calculate_expression(expression):
    """
    str -> int
    Return the result of arithmetic calculations in expression entered as text.
    >>> calculate_expression("Скільки буде 8 відняти 3?")
    5
    >>> calculate_expression("Скільки буде 7 додати 3 помножити на 5?")
    22
    >>> calculate_expression("Скільки буде 10 поділити на -2 додати 11 мінус -3?")
    9
    >>> calculate_expression("Скільки буде 3 в кубі?")
    'Неправильний вираз!'
    """
    spaces_number = 0
    arr_of = ["додати", 'відняти', 'мінус', 'поділити на', 'помножити на']
    for i in arr_of:
        num_of_spaces += expression.count(i) * 2

    expression = expression.replace('Скільки буде ','')
    expression = expression.replace('додати','+')
    expression = expression.replace('відняти','-')
    expression = expression.replace('мінус','-')
    expression = expression.replace('поділити на','/')
    expression = expression.replace('помножити на','*')
    expression = expression.replace('?','')
    
    try:
        if num_of_spaces > expression.count(" "):
            return "Неправильний вираз!"
        res = eval(expression)
        return int(res)
    except:
        return "Неправильний вираз!"