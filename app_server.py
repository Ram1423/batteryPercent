from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the data
df = pd.read_excel('example_modified_copy.xlsx')
df_interpol = pd.read_excel('new_ans.xlsx')
@app.route('/')
def index():
    return "Hello World"
# Endpoint to receive record_create_timestamp as input and return state_of_charge
@app.route('/predict', methods=['POST'])
def predict_soc():
    req_data = request.get_json()
    timestamp=req_data['record_create_timestamp']
    row=df_interpol[df_interpol['record_create_timestamp']==timestamp]
    soc=row['state_of_charge'].iloc[0]

    return '''<h1>
    The battery power is {}.
    </h1>'''.format(soc)

# if __name__ == '__main__':
#     app.run()
