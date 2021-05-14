from flask import Flask, render_template,redirect,request,url_for,flash
from werkzeug import datastructures
import wtforms
from wtforms import form


class CalculateForm(wtforms.Form):
    hissefiyati = wtforms.FloatField("Hisse halka arz fiyatı",validators= [wtforms.validators.DataRequired(message="Lütfen geçerli bir fiyat giriniz (küsüratlı fiyatlarda . kullanınız!)")],render_kw={"placeholder": "0.00₺"})
    tavanserisi = wtforms.IntegerField("Tavan serisi (gün)",validators= [wtforms.validators.DataRequired(message="Lütfen geçerli bir gün sayısı giriniz")],render_kw={"placeholder": "0"})


    

app = Flask(__name__)
app.secret_key="tavanserisi"


@app.route("/", methods=["GET","POST"])
def anasayfa():

    form = CalculateForm(request.form)
    
    

    if request.method=="POST" and form.validate():
        hissefiyati = form.hissefiyati
        tavanserisi = form.tavanserisi
        

        
        totaltavan=tavanserisi.data
        miktar=0
        hissefiyatiyeni = hissefiyati.data
        tavanserisiyeni = tavanserisi.data



        while(tavanserisiyeni>0):
            miktar=(hissefiyatiyeni*10)/100
            hissefiyatiyeni+=miktar
            hissesonuc=hissefiyatiyeni
            tavanserisiyeni-=1

        
        hissesonuc=str(round(hissesonuc,2)) 
        totaltavan=str(totaltavan)   
        flash("Hisse halka arz sonrası "+totaltavan+" gün tavan serisi yaptığı takdirde "+hissesonuc+"₺ "+"fiyatına ulaşmış olur.","dark")
    
    
    return render_template("anasayfa.html",form=form)










if __name__=="__main__":
    app.run(debug=True)