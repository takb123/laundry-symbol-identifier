build:
	npx tailwindcss -i static/base.css -o static/styles.css

run:
	uvicorn main:app --reload
