from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def mainIndex():
	president = 'Chris Roma'
	currentProject = {'company': 'FliteTest', 'plane': "Mini Cruiser", 'cost': 15}
	flyingP = True
	videos = [{'title': 'R/C with Dogs', 'vidLink': 'y0U_25vKpDs', 'description': 'Hoffy is a puppy at heart with the body of full grown dog. In other words, he\'s kind of insane.'}, 
		{'title': 'Quad Copter Shootout', 'vidLink': 'mNLqpBFwOXY', 'description': 'The guys comparing their experiences flying the different quads'}, 
		{'title': 'Argonay Miniquad Racecourse', 'vidLink': 'JpVY09Ce5C8', 'Description': 'We had the honor of flying with the Airgonay RC Club in their breathtaking miniquad racecourse. '}, 
		{'title': "Microwave Plane", 'vidLink': 'vF5UMQl9NUQ', 'description': "Attempting to pop popcorn in a microwave in the air!"}]
	return render_template('index.html', posts=videos, president=president, flyingP=flyingP, project=currentProject)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8080, debug=True)
