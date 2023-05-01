from flask import Flask, render_template, request
import openai

app = Flask(__name__)

openai.api_key = "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"

@app.route('/', methods=['GET', 'POST'])
def index():
    prompt = ""
    result = ""

    if request.method == 'POST' and 'generate' in request.form:
        prompt = request.form['prompt']
        model_engine = "text-davinci-002"
        temperature = 0.7
        max_tokens = 1024
        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        result = response['choices'][0]['text'].replace("\n", "<br>")

    return render_template('index.html', prompt=prompt, result=result)


if __name__ == '__main__':
    app.run(debug=True)
