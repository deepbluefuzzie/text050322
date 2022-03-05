#!/usr/bin/env python
# coding: utf-8

# In[1]:


from textblob import TextBlob

from flask import Flask

app = Flask(__name__)

from flask import render_template, request

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        print(text)
        r = TextBlob(text).sentiment
        return(render_template("index.html", results=r))
    else:
        return(render_template("index.html", results="2"))


# In[ ]:


if __name__=="__main__":
    app.run()


# In[ ]:




