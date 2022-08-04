test:
		sudo docker-compose up -d
		pytest --disable-warnings || true
		sudo docker-compose down
#test:
#		docker-compose up -d
#		pytest --disable-warnings || true
#		docker-compose down