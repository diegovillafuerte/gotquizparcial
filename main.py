from flask import Flask, render_template, request, redirect, url_for, flash
import math
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def bienvenida():
	try:
		if request.method  == 'POST':
			nombre = request.form['nombre']
			return redirect(url_for('iniciaQuiz', name = nombre))
		else:
			return render_template("bienvenida.html")
	except Exception as e:
		print(e)
		flash("Ocurrió un error, por favor intentalo de nuevo")
		return render_template("bienvenida.html")

@app.route("/inicio/<string:name>/", methods=['GET', 'POST'])
def iniciaQuiz(name):
	return "Esta función debe contener el quiz"

@app.route("/fin/<string:name>/<string:personaje>/<string:imagen>")
def finQuiz(name, personaje, imagen):
	try:
		return render_template("resultado.html", name = name, personaje = personaje, imagen = imagen)
	except Exception as e:
		print(e)
		print("El error ocurrió en la función finQuiz de main.py")
		flash("Ocurrió un error, por favor intentalo de nuevo")
		return render_template("bienvenida.html")

def calculaPersonaje(response):
	# Calculate Factor I Surgency or Extraversion
	f1 = 0
	f1 = f1 + int(response['p1'])
	f1 = f1 - int(response['p6'])
	f1 = f1 + int(response['p11'])
	f1 = f1 - int(response['p16'])
	f1 = math.floor((f1 + 8)*100/16)

	# Calculate Factor II Agreeableness 
	f2 = 0
	f2 = f2 + int(response['p2'])
	f2 = f2 - int(response['p7'])
	f2 = f2 + int(response['p12'])
	f2 = f2 - int(response['p17'])
	f2 = math.floor((f2 + 8)*100/16)

	# Calculate Factor III Conscientiousness
	f3 = 0
	f3 = f3 + int(response['p3'])
	f3 = f3 - int(response['p8'])
	f3 = f3 + int(response['p13'])
	f3 = f3 - int(response['p18'])
	f3 = math.floor((f3 + 8)*100/16)

	# Calculate Factor IV Neuroticism
	f4 = 0
	f4 = f4 + int(response['p4'])
	f4 = f4 - int(response['p9'])
	f4 = f4 + int(response['p14'])
	f4 = f4 - int(response['p19'])
	f4 = math.floor((f4 + 8)*100/16)

	# Calculate Factor V Intellect or Imagination
	f5 = 0
	f5 = f5 + int(response['p5'])
	f5 = f5 - int(response['p10'])
	f5 = f5 - int(response['p15'])
	f5 = f5 - int(response['p20'])
	f5 = math.floor((f5 + 14)*100/16)

	# [Extraversion. agreeableness, Conscientiousness, Neuroticism, Intelect]
	resp = [f1, f2, f3, f4, f5]
	redondeado = [str(round(i/100)) for i in resp]
	print(redondeado)
	res = ''.join(redondeado)
	print(res)

	personaje = 'White walker'
	imagen = 'walker'

	if res == '11101' or res == '11001' or res == '11111':
		personaje = 'Tyrion Lannister'
		imagen = 'tyrion'

	elif res == '11000' or res == '01100':
		personaje = 'Jon Snow'
		imagen = 'john'

	elif res == '11110' or res == '11011' or res == '11010':
		personaje = 'Daenerys Stormborn of House Targaryen, the First of Her Name, Queen of the Andals and the First Men, Protector of the Seven Kingdoms, the Mother of Dragons, the Khaleesi of the Great Grass Sea, the Unburnt, the Breaker of Chains'
		imagen = 'daenerys'

	elif res == '00001':
		personaje = 'Lord Varys'
		imagen = 'varys'

	elif res == '10011' or res == '00100' or res == '00010':
		personaje = 'Drogon'
		imagen = 'drogon'

	elif res == '10010' or res == '00011':
		personaje = 'King Joffrey I Baratheon'
		imagen = 'jeoffrey'

	elif res == '10111' or res == '10110' or res == '10001':
		personaje = 'Cersei Lannister'
		imagen = 'cersei'

	elif res == '01110' or res == '01001' or res == '01000':
		personaje = 'Arya Stark'
		imagen = 'arya'

	elif res == '11100' or res == '01101':
		personaje = 'Sam tarly'
		imagen = 'sam'

	elif res == '10101' or res == '10100' or res == '00101':
		personaje = 'Lord Peter Baelish'
		imagen = 'baelish'

	elif res == '01111' or res == '01011' or res == '01010':
		personaje = 'Sansa Stark'
		imagen = 'sansa'

	elif res == '00110' or res == '00111':
		personaje = 'Ramsay Bolton'
		imagen = 'ramsay'

	return personaje, imagen

if __name__ == "__main__":
	app.debug = True
	app.secret_key = 'Está es mi llave super secreta'
	app.run()