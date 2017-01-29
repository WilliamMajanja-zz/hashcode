import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='(%d/%m/%Y %H:%M:%S)')
logger = logging.getLogger(__name__)

"""" Load lines from input file to lines
    Return: array of lines
"""
def load_file(filename):
    with open(filename) as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

"""" Generator of ingredients added to list
    Return: list of ingredients
"""
def generate_ingredients(input):
    pizza = input[1:]
    pizza_list = list()
    for row in pizza:
        for col in row:
            pizza_list.append(col)
    return pizza_list

"""" Generator of config
    Return: hash of configs
"""
def generate_config(input):
    line = input[0].split()
    return {
        'rows': line[0],
        'cols': line[1],
        'min_ingredients': line[2],
        'max_cells': line[3],
    }

if __name__ == '__main__':
    logger.info('Loading data...')
    file_data   = load_file('example.in')
    logger.info('- Data loaded')
    ingredients = generate_ingredients(file_data)
    logger.info('- Ingredients loaded')
    config      = generate_config(file_data)
    logger.info('- Config loaded')
