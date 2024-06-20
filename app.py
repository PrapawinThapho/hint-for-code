from flask import Flask,render_template,request
from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config["SECRET_KEY"] = "key"
Bootstrap(app)

class fform(FlaskForm):
    q0 = TextAreaField("รหัส")
    submit0 = SubmitField("ตรวจสอบรหัส")
    q1 = TextAreaField("คำถาม1")
    submit1 = SubmitField("ส่งคำตอบ")
    q2 = TextAreaField("คำถาม2")
    submit2 = SubmitField("ส่งคำตอบ")
    q3 = TextAreaField("คำถาม3")
    submit3 = SubmitField("ส่งคำตอบ")
    q4 = TextAreaField("คำถาม4")
    submit4 = SubmitField("ส่งคำตอบ")
    q5 = TextAreaField("คำถาม5")
    submit5 = SubmitField("ส่งคำตอบ")
    q6 = TextAreaField("คำถาม6")
    submit6 = SubmitField("ส่งคำตอบ")
    q7 = TextAreaField("คำถาม7")
    submit7 = SubmitField("ส่งคำตอบ")
    q8 = TextAreaField("คำถาม8")
    submit8 = SubmitField("ส่งคำตอบ")
    q9 = TextAreaField("คำถาม9")
    submit9 = SubmitField("ส่งคำตอบ")
    q10 = TextAreaField("คำถาม10")
    submit10 = SubmitField("ส่งคำตอบ")

word = ["_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ "]
@app.route("/", methods=["GET", "POST"])
def index():
    q1 = False
    q2 = False
    q3 = False
    q4 = False
    q5 = False
    q6 = False
    q7 = False
    q8 = False
    q9 = False
    q10 = False
    pas = False
    hint1 = False
    hint2 = False
    form = fform()
    if form.validate_on_submit():
            if form.submit0.data:
                pas = form.q0.data
                form.q0.data = ""
                if pas == "yedmaekrit":
                     hint1 = True
                elif pas == "tirkeamdey":
                     hint2 = True
                else:
                     hint1 = "a"
            elif form.submit1.data:
                q1 = form.q1.data
                form.q1.data = ""
                if q1 == "ก๋วยเตี๋ยว":
                     word[0] = "y"
            elif form.submit2.data:
                q2 = form.q2.data
                form.q2.data = ""
                if q2 == "43":
                     word[1] = "e"
            elif form.submit3.data:
                q3 = form.q3.data
                form.q3.data = ""
                if q3 == "แม่":
                     word[2] = "d"
            elif form.submit4.data:
                q4 = form.q4.data
                form.q4.data = ""
                if q4 == "183":
                     word[3] = "m"
            elif form.submit5.data:
                q5 = form.q5.data
                form.q5.data = ""
                if q5 == "เจ้านาย":
                     word[4] = "a"
            elif form.submit6.data:
                q6 = form.q6.data
                form.q6.data = ""
                if q6 == "เขม":
                     word[5] = "e"
            elif form.submit7.data:
                q7 = form.q7.data
                form.q7.data = ""
                if q7 == "แดง":
                     word[6] = "k"
            elif form.submit8.data:
                q8 = form.q8.data
                form.q8.data = ""
                if q8 == "20":
                     word[7] = "r"
            elif form.submit9.data:
                q9 = form.q9.data
                form.q9.data = ""
                if q9 == "แครอท":
                     word[8] = "i"
            elif form.submit10.data:
                q10 = form.q10.data
                form.q10.data = ""
                if q10 == "pocky":
                     word[9] = "t"
    return render_template("index.html", form = form, q1 = q1, q2 = q2, q3 = q3, q4 = q4, q5 = q5, q6 = q6, q7 = q7, q8 = q8, q9 = q9, q10 = q10, word = word, pas = pas, hint1 = hint1, hint2 = hint2)

if __name__ == "__main__":
    app.run(debug=True)