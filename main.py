from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def speak():
  return render_template('index.html')
@app.route('/result', methods=['POST'])
def output():
    import speech_recognition as sr
    r=sr.Recognizer()
    a='invalid' 
    with sr.Microphone() as source:
      print("Speak anything")
      r.adjust_for_ambient_noise(source)
      audio = r.listen(source)
      
    try:
      text=r.recognize_google(audio)
      return render_template('result.html',b=text)
    except:
      return render_template('result.html',b=a)
   
if __name__=='__main__':
  app.run(debug=True)