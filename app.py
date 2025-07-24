# from flask import Flask, render_template, request, jsonify
# import time
# from algorithms import bubble_sort, merge_sort, selection_sort, linear_search, binary_search

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/process', methods=['POST'])
# def process():
#     data = request.json
#     array = data.get('array')
#     operation = data.get('operation')
#     algorithm = data.get('algorithm')
#     number = data.get('number', None)

#     start_time = time.time()
#     result = None

#     if operation == 'sorting':
#         if algorithm == 'bubble_sort':
#             result = bubble_sort(array)
#         elif algorithm == 'merge_sort':
#             result = merge_sort(array)
#         elif algorithm == 'selection_sort':
#             result = selection_sort(array)
#     elif operation == 'searching' and number is not None:
#         if algorithm == 'linear_search':
#             result = linear_search(array, number)
#         elif algorithm == 'binary_search':
#             result = binary_search(array, number)

#     end_time = time.time()
#     execution_time = end_time - start_time

#     return jsonify({
#         'result': result,
#         'time': execution_time
#     })


# if __name__ == '__main__':
#     app.run(debug=True)




#  font end me changes


from flask import Flask, render_template, request, jsonify
import time
from algorithms import bubble_sort, merge_sort, selection_sort, linear_search, binary_search

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    array = data.get('array')
    operation = data.get('operation')
    algorithm = data.get('algorithm')
    number = data.get('number', None)

    start_time = time.time()
    result = {'result': None, 'steps': []}  # Adding steps to the result for detailed output

    if operation == 'sorting':
        if algorithm == 'bubble_sort':
            result = bubble_sort(array)
        elif algorithm == 'merge_sort':
            result = merge_sort(array)
        elif algorithm == 'selection_sort':
            result = selection_sort(array)
    elif operation == 'searching' and number is not None:
        if algorithm == 'linear_search':
            result = linear_search(array, number)
        elif algorithm == 'binary_search':
            result = binary_search(array, number)

    end_time = time.time()
    execution_time = end_time - start_time

    return jsonify({
        'result': result,
        'time': execution_time
    })

if __name__ == '__main__':
    app.run(debug=True)
