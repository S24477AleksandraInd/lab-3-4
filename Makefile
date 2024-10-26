requirements:
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt

assets:
	mkdir -p .assets
	curl -o .assets/CollegeDistance.csv https://vincentarelbundock.github.io/Rdatasets/csv/AER/CollegeDistance.csv